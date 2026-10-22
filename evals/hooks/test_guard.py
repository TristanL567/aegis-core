"""Tests for the AEGIS guard: .claude/hooks/aegis_guard.py and .githooks/commit-msg.

Run: python evals/hooks/test_guard.py
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
GUARD = REPO / ".claude" / "hooks" / "aegis_guard.py"

TICKET = """id: T-001
goal: Something.
epic: T-E1
allowed_areas:
  - .aegis/tickets/T-001.yaml
  - src/            # a directory
  - docs/a.md
must_not_touch:
  - src/secret/
verify:
  - true
"""


def run(mode, payload, cwd=None, args=()):
    p = subprocess.run([sys.executable, str(GUARD), mode, *args], input=json.dumps(payload),
                       capture_output=True, text=True, cwd=cwd)
    return p.returncode, p.stderr


class Repo:
    def __init__(self, active="T-001", ticket=TICKET):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / ".git").mkdir()
        (self.root / ".aegis" / "tickets").mkdir(parents=True)
        if ticket is not None:
            (self.root / ".aegis" / "tickets" / "T-001.yaml").write_text(ticket)
        if active:
            (self.root / ".aegis" / "active-ticket").write_text(active + "\n")

    def edit(self, rel, tool="Write"):
        key = "notebook_path" if tool == "NotebookEdit" else "file_path"
        return run("edit", {"hook_event_name": "PreToolUse", "tool_name": tool, "cwd": str(self.root),
                            "tool_input": {key: str(self.root / rel)}})

    def bash(self, command, tool="Bash"):
        return run("bash", {"hook_event_name": "PreToolUse", "tool_name": tool, "cwd": str(self.root),
                            "tool_input": {"command": command}})

    def commit(self, message):
        f = self.root / "COMMIT_EDITMSG"
        f.write_text(message)
        return run("commit-msg", {}, cwd=self.root, args=[str(f)])

    def substop(self, message):
        return run("subagent-stop", {"hook_event_name": "SubagentStop", "cwd": str(self.root),
                                     "last_assistant_message": message})

    def approve(self):
        (self.root / ".aegis" / "verdicts").mkdir(exist_ok=True)
        (self.root / ".aegis" / "verdicts" / "T-001").write_text("APPROVED 2026-10-22T10:00\n")

    def verdict(self):
        f = self.root / ".aegis" / "verdicts" / "T-001"
        return f.read_text() if f.exists() else ""


class EditGuard(unittest.TestCase):
    def test_in_scope_directory_and_exact(self):
        r = Repo()
        self.assertEqual(r.edit("src/app.py")[0], 0)
        self.assertEqual(r.edit("docs/a.md", tool="Edit")[0], 0)

    def test_outside_scope_denied_with_reason(self):
        code, err = Repo().edit("docs/b.md")
        self.assertEqual(code, 2)
        self.assertIn("allowed_areas", err)

    def test_must_not_touch_wins(self):
        code, err = Repo().edit("src/secret/key.py")
        self.assertEqual(code, 2)
        self.assertIn("must_not_touch", err)

    def test_aegis_dir_allowed_but_not_verdicts(self):
        r = Repo()
        self.assertEqual(r.edit(".aegis/tickets/T-002.yaml")[0], 0)
        code, err = r.edit(".aegis/verdicts/T-001")
        self.assertEqual(code, 2)
        self.assertIn("verdict", err)

    def test_notebook(self):
        self.assertEqual(Repo().edit("notes/x.ipynb", tool="NotebookEdit")[0], 2)

    def test_no_active_ticket_allows(self):
        self.assertEqual(Repo(active=None).edit("anything.txt")[0], 0)

    def test_missing_ticket_fails_open(self):
        code, err = Repo(ticket=None).edit("anything.txt")
        self.assertEqual(code, 0)
        self.assertIn("warning", err.lower())

    def test_file_outside_repo_allowed(self):
        r = Repo()
        code, _ = run("edit", {"tool_name": "Write", "cwd": str(r.root),
                               "tool_input": {"file_path": str(Path(tempfile.gettempdir()) / "x.txt")}})
        self.assertEqual(code, 0)

    def test_flow_list_and_backslashes(self):
        r = Repo(ticket="id: T-001\nallowed_areas: [src/, 'docs/a.md']\nmust_not_touch: []\n")
        self.assertEqual(r.edit("src\\deep\\f.py")[0], 0)
        self.assertEqual(r.edit("docs/b.md")[0], 2)

    def test_column_zero_list_items(self):
        r = Repo(ticket="id: T-001\nallowed_areas:\n- src/\nmust_not_touch:\n- src/secret/\n")
        self.assertEqual(r.edit("src/a.py")[0], 0)
        self.assertEqual(r.edit("src/secret/k.py")[0], 2)

    def test_bom_in_active_ticket(self):
        r = Repo(active=None)
        (r.root / ".aegis" / "active-ticket").write_bytes("﻿T-001\n".encode("utf-8"))
        self.assertEqual(r.edit("docs/b.md")[0], 2)


class StashGuard(unittest.TestCase):
    def test_stash_in_any_form(self):
        r = Repo(active=None)
        for c in ["git stash", "git stash push -u -m x", "cd x && git -C . stash pop", "git  stash list",
                  "git --no-pager stash list", "git --git-dir=.git stash", "git -c user.name=x stash",
                  "if true; then git stash; fi", "for i in 1; do git stash; done", "! git stash",
                  "time git stash", "env A=1 git stash", "git \\\nstash", 'cat <<< "x"\ngit stash']:
            self.assertEqual(r.bash(c)[0], 2, c)

    def test_stash_in_powershell(self):
        r = Repo()
        self.assertEqual(r.bash("git stash", tool="PowerShell")[0], 2)
        self.assertEqual(r.bash("git `\nstash", tool="PowerShell")[0], 2)

    def test_stash_words_in_text_are_not_stash(self):
        r = Repo()
        for c in ["grep stash notes.txt", 'git commit -m "[T-001] Hooks block git stash"',
                  "grep -rn 'never use git stash' AGENTS.md", "cat <<'EOF'\ngit stash\nEOF",
                  "git commit -m \"$(cat <<'EOF'\n[T-001] x\n\nUse the \"x option; git stash\nEOF\n)\""]:
            self.assertEqual(r.bash(c)[0], 0, c)

    def test_commits_are_left_to_git(self):
        self.assertEqual(Repo().bash('git commit -m "no prefix"')[0], 0)


class CommitMsg(unittest.TestCase):
    def test_needs_verdict(self):
        code, err = Repo().commit("[T-001] Add thing\n")
        self.assertEqual(code, 2)
        self.assertIn("APPROVED", err)

    def test_subject_and_verdict(self):
        r = Repo()
        r.approve()
        self.assertEqual(r.commit("[T-001] Add thing\n\nBody\n")[0], 0)
        self.assertEqual(r.commit("[T-E1] Epic fix\n")[0], 0)

    def test_wrong_subject(self):
        r = Repo()
        r.approve()
        code, err = r.commit("Add thing\n")
        self.assertEqual(code, 2)
        self.assertIn("[T-001]", err)

    def test_comment_lines_ignored(self):
        r = Repo()
        r.approve()
        self.assertEqual(r.commit("# Please enter the commit message\n\n[T-001] Add\n")[0], 0)

    def test_wip_needs_no_verdict(self):
        r = Repo()
        self.assertEqual(r.commit("[T-001] WIP half done\n")[0], 0)
        self.assertEqual(r.commit("WIP half done\n")[0], 2)

    def test_merge_in_progress(self):
        r = Repo()
        self.assertEqual(r.commit("Merge branch 'aegis/T-001'\n")[0], 2)
        (r.root / ".git" / "MERGE_HEAD").write_text("abc\n")
        self.assertEqual(r.commit("Merge branch 'aegis/T-001'\n")[0], 0)

    def test_merge_in_linked_worktree(self):
        r = Repo()
        shutil.rmtree(r.root / ".git")
        gitdir = r.root.parent / (r.root.name + "-gitdir")
        gitdir.mkdir()
        (gitdir / "MERGE_HEAD").write_text("abc\n")
        (r.root / ".git").write_text(f"gitdir: {gitdir}\n")
        self.assertEqual(r.commit("anything\n")[0], 0)
        shutil.rmtree(gitdir)

    def test_cherry_pick_and_revert_in_progress(self):
        for head in ("CHERRY_PICK_HEAD", "REVERT_HEAD"):
            r = Repo()
            (r.root / ".git" / head).write_text("abc\n")
            self.assertEqual(r.commit('Revert "[OTHER-9] x"\n')[0], 0, head)

    def test_fixup_and_squash_prefixes(self):
        r = Repo()
        r.approve()
        self.assertEqual(r.commit("fixup! [T-001] Add thing\n")[0], 0)
        self.assertEqual(r.commit("squash! [T-001] Add thing\n")[0], 0)
        self.assertEqual(r.commit("fixup! Add thing\n")[0], 2)

    def test_no_active_ticket(self):
        self.assertEqual(Repo(active=None).commit("anything\n")[0], 0)

    def test_bom_in_active_ticket(self):
        r = Repo(active=None)
        (r.root / ".aegis" / "active-ticket").write_bytes("﻿T-001\n".encode("utf-8"))
        r.approve()
        self.assertEqual(r.commit("[T-001] Add\n")[0], 0)


@unittest.skipUnless(shutil.which("git"), "git not installed")
class RealGit(unittest.TestCase):
    """Commits through the installed .githooks/commit-msg, in the forms agents use."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        shutil.copytree(REPO / ".claude" / "hooks", self.root / ".claude" / "hooks")
        shutil.copytree(REPO / ".githooks", self.root / ".githooks")
        (self.root / ".aegis" / "tickets").mkdir(parents=True)
        (self.root / ".aegis" / "tickets" / "T-001.yaml").write_text(TICKET)
        (self.root / ".gitignore").write_text(".aegis/active-ticket\n.aegis/verdicts/\n")
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.email", "t@example.invalid")
        self.git("config", "user.name", "t")
        self.git("add", "-A")
        self.git("commit", "-qm", "base")
        self.git("config", "core.hooksPath", ".githooks")
        (self.root / ".aegis" / "active-ticket").write_text("T-001\n")

    def tearDown(self):
        self.tmp.cleanup()

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.root, capture_output=True, text=True)

    def sh(self, script):
        (self.root / "src").mkdir(exist_ok=True)
        (self.root / "src" / "f.txt").write_text(os.urandom(4).hex())
        self.git("add", "-A")
        return subprocess.run(["sh", "-c", script], cwd=self.root, capture_output=True, text=True).returncode

    def approve(self):
        (self.root / ".aegis" / "verdicts").mkdir(exist_ok=True)
        (self.root / ".aegis" / "verdicts" / "T-001").write_text("APPROVED test\n")

    def test_forms_without_verdict(self):
        self.assertNotEqual(self.sh('git commit -qm "[T-001] Add"'), 0)
        self.assertEqual(self.sh("git commit -q \\\n  -m '[T-001] WIP split command'"), 0)

    def test_forms_with_verdict(self):
        self.approve()
        ok = ['git commit -qm "[T-001] Add"', "git commit -q -m \"$(cat <<'EOF'\n[T-001] Heredoc\n\nUse the \"x\nEOF\n)\"",
              "git commit -q -F - <<'EOF'\n[T-001] From stdin\nEOF", "if true; then git commit -qam '[T-001] Keyword'; fi"]
        bad = ['git commit -qm "Wrong subject"', "git commit -q \\\n  -m 'wrong subject'", "git commit -qam 'wrong'"]
        for c in ok:
            self.assertEqual(self.sh(c), 0, c)
        for c in bad:
            self.assertNotEqual(self.sh(c), 0, c)

    def test_conclude_merge_with_no_edit(self):
        self.git("switch", "-qc", "side")
        (self.root / "m.txt").write_text("side\n")
        self.git("add", "-A")
        self.git("commit", "-qm", "[T-001] WIP side")
        self.git("switch", "-q", "main")
        (self.root / "m.txt").write_text("main\n")
        self.git("add", "-A")
        self.git("commit", "-qm", "[T-001] WIP main")
        self.git("merge", "-q", "side")  # conflicts
        (self.root / "m.txt").write_text("both\n")
        self.git("add", "-A")
        self.assertEqual(self.git("commit", "--no-edit").returncode, 0)


@unittest.skipUnless(shutil.which("git"), "git not installed")
class Executable(unittest.TestCase):
    def test_git_hook_is_committed_executable(self):
        """Git on Unix skips hooks without the executable bit."""
        out = subprocess.run(["git", "ls-files", "-s", ".githooks/commit-msg"], cwd=REPO,
                             capture_output=True, text=True).stdout
        if not out:
            self.skipTest("not tracked yet")
        self.assertTrue(out.startswith("100755"), out)


class SubagentStop(unittest.TestCase):
    def test_records_approved_naming_ticket(self):
        r = Repo()
        r.substop("Ticket: T-001\nVERDICT: APPROVED\nRequest fit: fits")
        self.assertTrue(r.verdict().startswith("APPROVED"))

    def test_code_fence(self):
        r = Repo()
        r.substop("```text\nTicket: T-001\nVERDICT: APPROVED\n```")
        self.assertTrue(r.verdict().startswith("APPROVED"))

    def test_other_ticket_ignored(self):
        r = Repo()
        r.substop("Ticket: UI-001\nVERDICT: APPROVED")
        self.assertEqual(r.verdict(), "")

    def test_no_ticket_line_ignored(self):
        r = Repo()
        r.substop("VERDICT: APPROVED")
        self.assertEqual(r.verdict(), "")

    def test_fixes_required_clears(self):
        r = Repo()
        r.approve()
        r.substop("Ticket: T-001\nVERDICT: FIXES_REQUIRED")
        self.assertEqual(r.verdict(), "")

    def test_unrelated_message_keeps(self):
        r = Repo()
        r.approve()
        r.substop("Here is the summary you asked for.")
        self.assertTrue(r.verdict().startswith("APPROVED"))

    def test_never_blocks(self):
        self.assertEqual(Repo().substop("Ticket: T-001\nVERDICT: BLOCKED")[0], 0)

    def test_transcript_fallback_for_handback_tools(self):
        r = Repo()
        t = r.root / "agent.jsonl"
        entry = {"type": "assistant", "message": {"role": "assistant", "content": [
            {"type": "tool_use", "name": "SubagentHandback",
             "input": {"report": "Ticket: T-001\nVERDICT: APPROVED\nScope: clean"}}]}}
        t.write_text(json.dumps({"type": "user", "message": {"role": "user", "content": "go"}}) + "\n"
                     + json.dumps(entry) + "\n")
        run("subagent-stop", {"cwd": str(r.root), "last_assistant_message": "", "agent_transcript_path": str(t)})
        self.assertTrue(r.verdict().startswith("APPROVED"))


class Robustness(unittest.TestCase):
    def test_bad_json_fails_open(self):
        p = subprocess.run([sys.executable, str(GUARD), "bash"], input="not json", capture_output=True, text=True)
        self.assertEqual(p.returncode, 0)

    def test_unreadable_message_fails_open(self):
        r = Repo()
        self.assertEqual(run("commit-msg", {}, cwd=r.root, args=[str(r.root / "missing")])[0], 0)


if __name__ == "__main__":
    unittest.main(verbosity=1)

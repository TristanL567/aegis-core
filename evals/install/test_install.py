"""Tests for tools/install_hooks.py on real git repositories.

Run: python evals/install/test_install.py
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

CORE = Path(__file__).resolve().parents[2]
SCRIPT = CORE / "tools" / "install_hooks.py"
TICKET = "id: T-001\nallowed_areas:\n  - src/\n  - .aegis/tickets/T-001.yaml\nmust_not_touch: []\n"


@unittest.skipUnless(shutil.which("git"), "git not installed")
class Install(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.global_config = Path(self.tmp.name) / "global.gitconfig"
        self.global_config.write_text("")
        self.env = dict(os.environ, GIT_CONFIG_GLOBAL=str(self.global_config))  # never the user's own
        self.repo = Path(self.tmp.name) / "repo"
        self.repo.mkdir()
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.email", "t@example.invalid")
        self.git("config", "user.name", "t")
        (self.repo / "README.md").write_text("x\n")
        self.git("add", "-A")
        self.git("commit", "-qm", "base")

    def tearDown(self):
        self.tmp.cleanup()

    def git(self, *args, cwd=None):
        return subprocess.run(["git", *args], cwd=cwd or self.repo, capture_output=True, text=True, env=self.env)

    def install(self, *extra, target=None):
        p = subprocess.run([sys.executable, str(SCRIPT), str(CORE), str(target or self.repo), *extra],
                           capture_output=True, text=True, env=self.env)
        return p.returncode, p.stdout

    def start_ticket(self, root=None):
        root = root or self.repo
        (root / ".aegis" / "tickets").mkdir(parents=True, exist_ok=True)
        (root / ".aegis" / "tickets" / "T-001.yaml").write_text(TICKET)
        (root / ".aegis" / "active-ticket").write_text("T-001\n")

    def commit(self, subject, root=None):
        root = root or self.repo
        (root / "src").mkdir(exist_ok=True)
        f = root / "src" / "f.txt"
        f.write_text(f.read_text() + "x" if f.exists() else "x")
        self.git("add", "src", cwd=root)
        return self.git("commit", "-qm", subject, cwd=root).returncode

    def test_fresh_repo(self):
        code, out = self.install()
        self.assertEqual(code, 0, out)
        for rel in (".claude/hooks/aegis-guard.sh", ".claude/hooks/aegis_guard.py", ".githooks/commit-msg"):
            self.assertTrue((self.repo / rel).exists(), rel)
        self.assertEqual(self.git("config", "core.hooksPath").stdout.strip(), ".githooks")
        ignore = (self.repo / ".gitignore").read_text()
        for line in (".aegis/active-ticket", ".aegis/verdicts/", ".claude/worktrees/"):
            self.assertIn(line, ignore)
        self.start_ticket()
        self.assertNotEqual(self.commit("[T-001] no verdict"), 0)
        self.assertEqual(self.commit("[T-001] WIP ok"), 0)

    def test_rerun_changes_nothing(self):
        self.install()
        before = {p: p.read_bytes() for p in self.repo.rglob("*") if p.is_file() and ".git" not in p.parts}
        code, out = self.install()
        after = {p: p.read_bytes() for p in self.repo.rglob("*") if p.is_file() and ".git" not in p.parts}
        self.assertEqual(before, after)
        self.assertIn("up to date", out)
        settings = json.loads((self.repo / ".claude" / "settings.json").read_text())
        self.assertEqual(len(settings["hooks"]["PreToolUse"]), 2)

    def test_existing_pre_commit_hook_keeps_running(self):
        hooks = Path(self.git("rev-parse", "--path-format=absolute", "--git-path", "hooks").stdout.strip())
        (hooks / "pre-commit").write_text("#!/bin/sh\necho ran > \"$(git rev-parse --show-toplevel)/pre-commit-ran\"\n")
        (hooks / "pre-commit").chmod(0o755)
        code, out = self.install()
        self.assertEqual(self.git("config", "core.hooksPath").returncode, 1, "hooksPath must stay unset")
        self.assertTrue((hooks / "commit-msg").exists(), out)
        self.start_ticket()
        self.assertNotEqual(self.commit("[T-001] no verdict"), 0)
        self.assertEqual(self.commit("[T-001] WIP ok"), 0)
        self.assertTrue((self.repo / "pre-commit-ran").exists())

    def test_existing_commit_msg_hook_is_chained(self):
        hooks = Path(self.git("rev-parse", "--path-format=absolute", "--git-path", "hooks").stdout.strip())
        own = "#!/bin/sh\necho own >> \"$(git rev-parse --show-toplevel)/own-ran\"\nexit 0\n"
        (hooks / "commit-msg").write_text(own)
        (hooks / "commit-msg").chmod(0o755)
        self.install()
        self.install()  # idempotent
        text = (hooks / "commit-msg").read_text()
        self.assertEqual(text.count("aegis-guard.sh"), 1)
        self.assertIn("echo own", text)
        self.start_ticket()
        self.assertNotEqual(self.commit("[T-001] no verdict"), 0)
        self.assertEqual(self.commit("[T-001] WIP ok"), 0)
        self.assertTrue((self.repo / "own-ran").exists())

    def test_settings_merged_and_kept(self):
        (self.repo / ".claude").mkdir()
        mine = {"permissions": {"allow": ["Bash(npm test)"]},
                "hooks": {"PreToolUse": [{"matcher": "Bash", "hooks": [{"type": "command", "command": "echo mine"}]}]}}
        (self.repo / ".claude" / "settings.json").write_text(json.dumps(mine))
        self.install()
        self.install()
        s = json.loads((self.repo / ".claude" / "settings.json").read_text())
        self.assertEqual(s["permissions"], mine["permissions"])
        commands = [h["command"] for g in s["hooks"]["PreToolUse"] for h in g["hooks"]]
        self.assertIn("echo mine", commands)
        self.assertEqual(sum("aegis-guard.sh" in c for c in commands), 2)
        self.assertIn("SubagentStop", s["hooks"])

    def test_update_replaces_older_aegis_files(self):
        self.install()
        old = self.repo / ".claude" / "hooks" / "aegis_guard.py"
        old.write_text('"""AEGIS guard, an older version."""\n')
        code, out = self.install()
        self.assertEqual(old.read_bytes(), (CORE / ".claude" / "hooks" / "aegis_guard.py").read_bytes())
        self.assertIn("updated", out)

    def test_repos_own_githooks_commit_msg_is_kept(self):
        own = "#!/bin/sh\n# the team's own message check\nexit 0\n"
        (self.repo / ".githooks").mkdir()
        (self.repo / ".githooks" / "commit-msg").write_text(own)
        self.git("config", "core.hooksPath", ".githooks")
        code, out = self.install()
        text = (self.repo / ".githooks" / "commit-msg").read_text()
        self.assertIn("the team's own message check", text)
        self.assertIn("aegis-guard.sh", text)
        self.start_ticket()
        self.assertNotEqual(self.commit("[T-001] no verdict"), 0)

    def test_rerun_keeps_repos_own_chained_hook(self):
        own = "#!/bin/sh\n# the team's own message check\nexit 0\n"
        (self.repo / ".githooks").mkdir()
        (self.repo / ".githooks" / "commit-msg").write_text(own)
        self.git("config", "core.hooksPath", ".githooks")
        self.install()
        code, out = self.install()
        text = (self.repo / ".githooks" / "commit-msg").read_text()
        self.assertIn("the team's own message check", text, out)
        self.assertEqual(text.count("aegis-guard.sh"), 1)

    def test_global_hooks_path_is_left_alone(self):
        shared = Path(self.tmp.name) / "shared-hooks"
        shared.mkdir()
        (shared / "pre-commit").write_text("#!/bin/sh\nexit 0\n")
        self.git("config", "--global", "core.hooksPath", str(shared))
        code, out = self.install()
        self.assertEqual(code, 0, out)
        self.assertFalse((shared / "commit-msg").exists())
        self.assertIn("not active", out.lower())
        self.assertEqual(self.git("config", "--local", "core.hooksPath").returncode, 1)

    def test_tilde_global_hooks_path_is_left_alone(self):
        home = Path(self.tmp.name) / "home"
        (home / ".githooks").mkdir(parents=True)
        self.env["HOME"] = str(home)
        self.git("config", "--global", "core.hooksPath", "~/.githooks")
        code, out = self.install()
        self.assertEqual(code, 0, out)
        self.assertIn("not active", out.lower())
        self.assertFalse((self.repo / "~").exists())
        self.assertFalse((home / ".githooks" / "commit-msg").exists())

    def test_hook_files_are_committed_executable(self):
        self.install()
        self.git("add", "-A")
        modes = self.git("ls-files", "-s", ".githooks/commit-msg", ".claude/hooks/aegis-guard.sh").stdout
        self.assertEqual([l.split()[0] for l in modes.splitlines()], ["100755", "100755"], modes)

    def test_update_replaces_stale_aegis_settings(self):
        (self.repo / ".claude").mkdir()
        old = {"hooks": {"PreToolUse": [
            {"matcher": "Bash", "hooks": [{"type": "command", "command": "sh old/.claude/hooks/aegis-guard.sh bash"}]},
            {"matcher": "Bash", "hooks": [{"type": "command", "command": "echo mine"}]}]},
            "note": "Grüße"}
        (self.repo / ".claude" / "settings.json").write_text(json.dumps(old, ensure_ascii=False), encoding="utf-8")
        self.install()
        text = (self.repo / ".claude" / "settings.json").read_text(encoding="utf-8")
        s = json.loads(text)
        commands = [h["command"] for g in s["hooks"]["PreToolUse"] for h in g["hooks"]]
        self.assertNotIn("sh old/.claude/hooks/aegis-guard.sh bash", commands)
        self.assertIn("echo mine", commands)
        self.assertIn("Bash|PowerShell", [g.get("matcher") for g in s["hooks"]["PreToolUse"]])
        self.assertIn("Grüße", text)

    def own_hook(self, data):
        hooks = Path(self.git("rev-parse", "--path-format=absolute", "--git-path", "hooks").stdout.strip())
        (hooks / "commit-msg").write_bytes(data)
        (hooks / "commit-msg").chmod(0o755)
        return hooks / "commit-msg"

    def test_hook_in_another_language_is_left_alone(self):
        hook = self.own_hook(b"#!/usr/bin/env python\nimport sys\nsys.exit(0)\n")
        before = hook.read_bytes()
        code, out = self.install()
        self.assertEqual(code, 0, out)
        self.assertEqual(hook.read_bytes(), before)
        self.assertIn("not active", out.lower())
        (self.repo / "o.txt").write_text("o")
        self.git("add", "o.txt")
        self.assertEqual(self.git("commit", "-qm", "still commits").returncode, 0)

    def test_hook_not_utf8_is_left_alone_and_nothing_breaks(self):
        hook = self.own_hook(b"#!/bin/sh\n# Pr\xfcfung\nexit 0\n")
        before = hook.read_bytes()
        code, out = self.install()
        self.assertEqual(code, 0, out)
        self.assertEqual(hook.read_bytes(), before)
        self.assertIn("not active", out.lower())

    def test_line_endings_are_kept(self):
        gitignore = self.repo / ".gitignore"
        gitignore.write_bytes(b"node_modules/\r\ndist/\r\n")
        self.install()
        data = gitignore.read_bytes()
        self.assertTrue(data.startswith(b"node_modules/\r\ndist/\r\n"), data)
        self.assertNotIn(b"\n", data.replace(b"\r\n", b""))  # CRLF file stays CRLF
        gitignore.write_bytes(b"a/\nb/\n")
        self.install()
        self.assertNotIn(b"\r\n", gitignore.read_bytes())  # LF file stays LF

    def test_old_aegis_line_is_upgraded(self):
        old = b'#!/bin/sh\nsh "$(git rev-parse --show-toplevel)/.claude/hooks/aegis-guard.sh" commit-msg "$1" || exit $?  # AEGIS\nexit 0\n'
        hook = self.own_hook(old)
        self.install()
        text = hook.read_text()
        self.assertEqual(text.count("aegis-guard.sh"), 1)
        self.assertIn('[ ! -f "$g" ]', text)

    def test_own_hook_mentioning_aegis_is_kept(self):
        own = "#!/bin/sh\n# aegis-web: check commit message length\nexit 0\n"
        (self.repo / ".githooks").mkdir()
        (self.repo / ".githooks" / "commit-msg").write_text(own)
        self.git("config", "core.hooksPath", ".githooks")
        code, out = self.install()
        text = (self.repo / ".githooks" / "commit-msg").read_text()
        self.assertIn("aegis-web: check commit message length", text, out)
        self.assertIn("kept the repo's own file", out)

    def test_not_utf8_gitignore_changes_nothing(self):
        (self.repo / ".gitignore").write_bytes(b"caf\xe9/\n")
        code, out = self.install()
        self.assertEqual(code, 1, out)
        self.assertFalse((self.repo / ".githooks").exists())

    def test_local_hooks_path_outside_repo(self):
        outside = Path(self.tmp.name) / "outside-hooks"
        outside.mkdir()
        self.git("config", "core.hooksPath", str(outside))
        code, out = self.install()
        self.assertFalse((outside / "commit-msg").exists())
        self.assertIn("not active", out.lower())
        self.assertIn('[ ! -f "$g" ]', out)  # the line to add by hand is printed

    def test_wrong_source_changes_nothing(self):
        p = subprocess.run([sys.executable, str(SCRIPT), str(self.tmp.name), str(self.repo)],
                           capture_output=True, text=True, env=self.env)
        self.assertEqual(p.returncode, 1, p.stdout)
        self.assertIn("not an aegis-core checkout", p.stdout)
        self.assertFalse((self.repo / ".githooks").exists())

    def test_dry_run_matches_real_run(self):
        self.git("config", "core.hooksPath", str((self.repo / ".githooks").resolve()))
        code, dry = self.install("--dry-run")
        code, real = self.install()
        self.assertEqual([l.removeprefix("would ") for l in dry.splitlines() if "commit check" in l],
                         [l for l in real.splitlines() if "commit check" in l])

    def test_branch_without_aegis_files_still_commits(self):
        hooks = Path(self.git("rev-parse", "--path-format=absolute", "--git-path", "hooks").stdout.strip())
        (hooks / "pre-commit").write_text("#!/bin/sh\nexit 0\n")
        self.git("switch", "-qc", "old")
        self.git("switch", "-q", "main")
        self.install()
        self.git("add", "-A")
        self.git("commit", "-qm", "install AEGIS")
        self.git("switch", "-q", "old")
        self.assertFalse((self.repo / ".claude" / "hooks" / "aegis-guard.sh").exists())
        (self.repo / "o.txt").write_text("o")
        self.git("add", "o.txt")
        self.assertEqual(self.git("commit", "-qm", "work on an old branch").returncode, 0)

    def test_wrongly_shaped_settings_changes_nothing(self):
        (self.repo / ".claude").mkdir()
        for bad in ('{"hooks": null}', "[]", '{"hooks": {"PreToolUse": {}}}',
                    '{"hooks": {"PreToolUse": [{"matcher": "Bash", "hooks": ["echo hi"]}]}}'):
            (self.repo / ".claude" / "settings.json").write_text(bad)
            code, out = self.install()
            self.assertEqual(code, 1, bad)
            self.assertFalse((self.repo / ".githooks").exists(), bad)
            self.assertFalse((self.repo / ".claude" / "hooks").exists(), bad)

    def test_dormant_hooks_are_reported(self):
        (self.repo / ".githooks").mkdir()
        (self.repo / ".githooks" / "pre-push").write_text("#!/bin/sh\nexit 0\n")
        code, out = self.install()
        self.assertIn("pre-push", out)

    def test_husky(self):
        (self.repo / ".husky" / "_").mkdir(parents=True)
        self.git("config", "core.hooksPath", ".husky/_")
        code, out = self.install()
        self.assertTrue((self.repo / ".husky" / "commit-msg").exists(), out)
        self.assertFalse((self.repo / ".husky" / "_" / "commit-msg").exists())

    def test_linked_worktree(self):
        hooks = Path(self.git("rev-parse", "--path-format=absolute", "--git-path", "hooks").stdout.strip())
        (hooks / "pre-commit").write_text("#!/bin/sh\nexit 0\n")
        wt = Path(self.tmp.name) / "wt"
        self.git("worktree", "add", "-q", "-b", "side", str(wt))
        code, out = self.install(target=wt)
        self.assertEqual(code, 0, out)
        self.assertTrue((hooks / "commit-msg").exists(), out)
        self.start_ticket(wt)
        self.assertNotEqual(self.commit("[T-001] no verdict", root=wt), 0)

    def test_invalid_settings_changes_nothing(self):
        (self.repo / ".claude").mkdir()
        (self.repo / ".claude" / "settings.json").write_text("{not json")
        code, out = self.install()
        self.assertEqual(code, 1)
        self.assertFalse((self.repo / ".githooks").exists())

    def test_dry_run_changes_nothing(self):
        code, out = self.install("--dry-run")
        self.assertEqual(code, 0)
        self.assertIn("would", out)
        self.assertFalse((self.repo / ".githooks").exists())
        self.assertEqual(self.git("config", "core.hooksPath").returncode, 1)


if __name__ == "__main__":
    unittest.main(verbosity=1)

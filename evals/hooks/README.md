# AEGIS hooks: tests (AEGIS-020)

There are two kinds of hook. Both run `.claude/hooks/aegis_guard.py` through
`aegis-guard.sh`, which starts whichever Python works.

| Hook | Wired in | Enforces |
|---|---|---|
| Claude Code PreToolUse, Edit/Write/MultiEdit/NotebookEdit | `.claude/settings.json` | Edits stay inside the active ticket's `allowed_areas` and outside `must_not_touch`. Verdict files can't be edited. |
| Claude Code PreToolUse, Bash/PowerShell | `.claude/settings.json` | No `git stash`. |
| Claude Code SubagentStop | `.claude/settings.json` | Records a validator's `Ticket: <ID>` / `VERDICT:` in `.aegis/verdicts/<ID>`. |
| git `commit-msg` | `.githooks/`, installed per clone with `git config core.hooksPath .githooks` | The subject starts with `[<ID>] ` (or the epic ID), and an APPROVED verdict is recorded. `[<ID>] WIP` commits, `fixup!`/`squash!` prefixes, and the commit that concludes a merge, cherry-pick or revert are exempt. |

**Why git checks the commits.** In three validation rounds, the first design
read commit messages out of the shell command. Each round found another way
of writing a commit that it misread: heredocs, `-am`, shell keywords, line
continuations, `--no-edit` merges. Git's commit-msg hook gets the final
message as a file, so it needs no parsing, and it also works for other tools
and for a human at the terminal.

## Tests

```bash
python evals/hooks/test_guard.py
```

The 40 tests cover:
- **Edits:** scope, must_not_touch, `.aegis/`, verdict files, flow-list and
  column-0 lists, an active-ticket file with a BOM.
- **Stash:** every form the validators found, including global options,
  shell keywords, Bash `\` and PowerShell backtick line continuations, and
  `<<<`. "git stash" inside quotes, heredoc text or a grep pattern is not
  blocked.
- **commit-msg:** subject, verdict, WIP, `fixup!`/`squash!`, comment lines,
  merges in a normal and a linked worktree, cherry-picks and reverts in
  progress, no active ticket. A further test checks that the committed hook
  is executable (mode 100755): git on Unix skips hooks that aren't.
- **Real git:** commits run through the installed hook, using heredoc,
  `-F -`, `-am`, line-continuation and `if ...; then` forms, plus a
  conflicted merge concluded with `git commit --no-edit`.
- **SubagentStop:** including reading the verdict from the subagent's
  transcript when a hand-back tool carries the report.
- **Failing open:** unreadable input, an unreadable message file, a missing
  ticket file (for edits).

## Live check (2026-10-22, Claude Code 2.1.295, Windows, Git Bash)

The setup:
- a fresh repo with ticket `HK-001`: `src/` allowed, `src/locked.txt` in
  must_not_touch;
- the hooks copied in, and `core.hooksPath .githooks` set;
- one `claude -p --model sonnet --permission-mode acceptEdits` session.

| Step | Result | Checked on disk |
|---|---|---|
| Edit `src/locked.txt` with the Edit tool (separate session) | blocked: "in must_not_touch of ticket HK-001" | file unchanged |
| `git stash` | blocked | stash list empty |
| Commit `[HK-001] change a` without a verdict | blocked by git: "no APPROVED verdict recorded" | no commit |
| Commit `[HK-001] WIP set aside` | allowed | in `git log` |
| Stub subagent replies `Ticket: HK-001` / `VERDICT: APPROVED` | verdict recorded | `.aegis/verdicts/HK-001`: `APPROVED <time> by subagent general-purpose` |
| Commit `[HK-001] change a again`, split with a `\` continuation | allowed | in `git log` |
| Commit `no ticket id` | blocked by git: "subject must start with [HK-001]" | no commit |

In the main session, asked to change `src/locked.txt` without being told which
tool to use, the agent used `sed` in Bash. That isn't guarded, so the file
changed. That's why the Edit-tool step was run separately.

## What the hooks don't enforce

- **The verdict gate is a speed bump.** Any subagent that prints the two
  lines records a verdict, as the stub shows, and an agent could write the
  file through Bash. It stops a commit that forgot validation, not deliberate
  cheating. The edit guard denies Edit/Write on verdict files, AGENTS.md
  forbids forging one (from AEGIS-021), and the file names the subagent type,
  which the human can check.
- **A verdict is not tied to the content.** Changes made after APPROVED can
  be committed without validating again.
- **Writes through Bash are not guarded,** such as `sed -i` or `>`. The live
  check above shows an agent doing exactly that.
- **A finished ticket stays active** until `.aegis/active-ticket` is cleared,
  and so does its verdict. AEGIS-021 tells agents to clear it.
- **A squash merge (`git merge --squash`, then commit) needs a `[<ID>]`
  subject.** Git's proposed message is refused.
- **The git hook needs `core.hooksPath`** (or a call from an existing
  commit-msg hook), and `--no-verify` skips it.
- **Desktop app hand-back:** reading the verdict from the transcript is
  unit-tested and was checked offline on real transcripts, but not seen live.
- **Without Python, or in tools other than Claude Code, the Claude Code hooks
  don't run.** The git hook needs Python too. The written rules still apply.

## How the hooks run

- Hooks run in Git Bash on Windows, and `$CLAUDE_PROJECT_DIR` is set.
- A Windows checkout with `core.autocrlf=true` gives the scripts CRLF line
  endings, and Git Bash still runs them.
- A session loads its Claude Code hooks when it starts.

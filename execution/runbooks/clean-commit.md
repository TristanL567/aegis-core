# Clean Commit Runbook

Use this runbook after one ticket has completed its worker step and validator gate. It describes how to prepare a clean, scoped commit for exactly one ticket at a time.

This runbook is operator guidance only. Canonical role behavior remains in `skills/`, and canonical ticket and swarm rules remain in `contracts/`.

## Preconditions

- The current ticket has completed the loop `master -> worker -> validator -> master`.
- The validator result is approving, or an explicit human override is included in the carried-forward ticket context.
- The ticket envelope includes the ticket ID, goal, allowed areas, must-not-touch areas, acceptance criteria, and verification expectations.
- No other ticket is being staged, committed, merged, or pushed in the same action.

## Scope Review

Start from the repository root and inspect the current branch and worktree:

```powershell
git branch --show-current
git status --short
```

Confirm the branch matches the ticket context before preparing a commit. If the branch is not the expected ticket or integration branch, stop and ask the master or human operator for routing.

Treat dirty worktree entries as shared state. Preserve unrelated files exactly as they are:

- Do not delete, revert, format, move, or stage unrelated files.
- Do not use broad cleanup commands to make the worktree look clean.
- Do not run `git add -A`, `git add .`, or broad pathspecs unless the current ticket explicitly owns every affected path.
- If unrelated dirty files are present, note them in the completion envelope and stage only the ticket-owned files.

Review the ticket scope before staging:

```powershell
git diff --name-only
git diff --stat
git diff -- <allowed path>
```

Every changed path selected for commit must be allowed by the current ticket. If a required change appears outside the allowed areas, stop and return the conflict to the master.

## Validation Review

Record validation before staging or committing. Run the command or commands specified by the ticket. For this repository, the common skill library validator is:

```powershell
py -3.10 .\tools\validate_skill_library.py
```

For each validation command, capture:

- the exact command;
- whether it passed or failed;
- the relevant output summary;
- any skipped validation and the reason it was skipped.

Do not commit if required validation failed unless a human explicitly approves committing a known failing state.

## Staging

Stage only files allowed by the current ticket. Prefer explicit file paths:

```powershell
git add -- execution/runbooks/clean-commit.md prompts/05-finish/clean-commit.md
```

After staging, review both the staged file list and staged diff:

```powershell
git diff --cached --name-only
git diff --cached --stat
git diff --cached
```

Check that:

- every staged file is allowed by the current ticket;
- the staged diff implements only the current ticket goal;
- no unrelated dirty worktree entries were staged;
- generated or scaffold files were not added unless the ticket explicitly required them;
- validation results are available for the staged state.

If an unrelated file was staged by mistake, unstage only that file:

```powershell
git restore --staged -- <path>
```

Do not revert the file unless the ticket owns it and the operator explicitly intends to discard that ticket change.

## Commit Message

When a master-agent assignment has `commit_required: true`, the master-agent
commits finished assigned work to the assignment branch. The commit message must
match the assigned ticket ID, and the commit must include only ticket-owned
files.

Canonical ticket-bound commit format:

```text
[TICKET-ID] concise description
```

The description must be 72 characters or fewer.

Example:

```text
[AEGIS-MERGE-006] add clean commit guidance
```

Use the completion report, not the commit message, for acceptance criteria and
validation details.

Create the commit only after staged diff review passes:

```powershell
git commit -m "[TICKET-ID] concise description"
```

Use the assigned ticket ID and a concise description of the actual change.

## Post-Commit Check

After committing, inspect the result:

```powershell
git status --short
git log -1 --stat
```

Confirm:

- the new commit contains only ticket-owned files;
- unrelated dirty worktree entries are still present and unstaged if they existed before;
- post-commit status has no unexpected staged files;
- the completion envelope includes the commit SHA if a commit was made.

If an unexpected file was committed, stop and ask for human guidance before rewriting history.

## Merge and Push After a Ticket Series

Do not merge or push while preparing an individual ticket commit. Merge and push are later operator actions after a reviewed ticket series is complete.

When the reviewed ticket series is ready to integrate:

1. Confirm all tickets in the series have completed validation and clean commits.
2. Confirm the worktree status and preserve unrelated dirty files.
3. Switch to `main` only when the operator has approved integration.
4. Merge `Development` into `main`:

```powershell
git switch main
git merge Development
```

5. Re-run the required validation commands on `main`.
6. Review the merge result:

```powershell
git status --short
git log --oneline --max-count 5
```

7. Push only after validation and human/operator review:

```powershell
git push origin main
```

If conflicts, failing validation, or unexpected dirty files appear during integration, stop and route the issue back through the master instead of forcing the merge or push.

# Clean Commit

Use this prompt to ask an agent or operator to prepare a scoped commit for one completed AEGIS ticket.

```text
You are preparing a clean commit for one AEGIS ticket.

Load and follow operator guidance from:
- execution/runbooks/clean-commit.md

Use the canonical field definitions from:
- contracts/ticket-contract.md
- contracts/swarm-contract.md

Ticket envelope:
<paste original ticket envelope here>

Worker output:
<paste complete worker output here>

Validator output:
<paste complete validator output here>

Current repository context:
- Branch: <paste current branch here>
- HEAD: <paste current HEAD here>
- Known unrelated dirty worktree entries: <paste entries here, or "none">

Rules:
- Prepare a commit for this ticket only.
- Do not start, plan, stage, commit, merge, or push another ticket.
- Do not perform merge or push as part of this prompt.
- Preserve unrelated dirty worktree entries exactly as they are.
- Stage only files allowed by the current ticket.
- Do not stage files outside the ticket allowed areas.
- Do not use broad staging commands such as `git add -A` or `git add .` unless every affected path is explicitly allowed by this ticket.
- Do not delete, revert, format, or modify unrelated worktree files.
- If any required change is outside the ticket write scope, stop and report the blocker.

Before staging, check and report:
- current branch with `git branch --show-current`;
- worktree state with `git status --short`;
- changed files with `git diff --name-only`;
- scoped diff or diff stat for the ticket-owned files.

Validation:
- Run the validation commands required by the ticket.
- Include the exact command, pass/fail result, and short output summary.
- If validation cannot be run, state why and do not claim it passed.

Staging:
- Stage only ticket-owned files with explicit paths.
- Review staged files with `git diff --cached --name-only`.
- Review staged content with `git diff --cached --stat` and, when needed, `git diff --cached`.
- Confirm no unrelated dirty worktree entry was staged.

Commit-message guidance:
- Include the ticket ID.
- Include the ticket goal.
- Include the acceptance criteria satisfied by the commit.
- Include validation evidence.

Recommended commit message format:

<TICKET-ID>: <short goal>

- Goal: <one sentence describing the ticket objective>
- Acceptance: <criterion or grouped criteria satisfied>
- Validation: <command and result>

Post-commit checks if a commit is made:
- Run `git status --short`.
- Run `git log -1 --stat`.
- Confirm the commit contains only files allowed by the current ticket.
- Confirm unrelated dirty worktree entries remain preserved.

Later merge/push guidance:
- Do not merge or push for this ticket.
- After a reviewed ticket series is complete, an operator may merge `Development` into `main`, re-run validation on `main`, review the merge result, and push only after approval.

Return the standard envelope with these fields:
- status
- summary
- artifacts
- findings
- next_recommended_role
- changed_files
- verification

For `changed_files`, list only files staged or committed for this ticket. For `verification`, include commands run, pass/fail status, and a short note. If no commit was made, state why.
```

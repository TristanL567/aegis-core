---
id: clean-commit
stage: finish
mode: any
audience: human
target_role: skills/roles/master/
pairs_with:
  - prompts/05-finish/completion-report.md
  - prompts/04-validate/conformance-check.md
requires:
  - contracts/kernel.md
  - contracts/ticket-contract.md
  - execution/runbooks/clean-commit.md
returns:
  - commit readiness report
  - standard role envelope
---

# Clean Commit

## When to use

Use this prompt after completion reporting when one ticket's validated changes
are ready for scoped commit preparation.

## Preconditions

- Validator approval or human override is recorded.
- Completion report exists.
- The operator wants a ticket-bound commit.

## Prompt

```text
Prepare a clean AEGIS ticket-bound commit.

Use:
- contracts/kernel.md
- contracts/ticket-contract.md Master-Agent Assignment Commits
- execution/runbooks/clean-commit.md

Required commit format:
[TICKET-ID] concise description

The description must be 72 characters or fewer.

Ticket envelope:
[TICKET_ENVELOPE]

Completion report:
[COMPLETION_REPORT]

Repository state:
- branch: [BRANCH]
- head: [HEAD]
- unrelated dirty worktree entries: [DIRTY_WORKTREE]

Rules:
- Stage only ticket-owned files with explicit paths.
- Preserve unrelated dirty files exactly as they are.
- Do not merge, push, or open a pull request.
- Stop if any staged or changed path is outside allowed_areas or inside
  must_not_touch.

Return commit readiness evidence before or after committing, depending on the
operator instruction.
```

## Expected response

- Commit readiness report.
- Staged or committed file list.
- Verification evidence.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | master | `prompts/05-finish/close-epic.md` |
| completed | human | stop |
| fixes_required | master | `prompts/04-validate/drift-correction.md` |
| blocked | human | `prompts/06-control/halt.md` |

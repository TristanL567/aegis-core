---
id: halt
stage: control
mode: any
audience: human
target_role: none
pairs_with:
  - prompts/06-control/status-report.md
  - prompts/06-control/recover-context.md
requires:
  - contracts/kernel.md
  - contracts/epic-contract.md
returns:
  - halt summary
  - standard role envelope
---

# Halt

## When to use

Use this prompt to stop a session safely while preserving enough state for a
future recovery.

## Preconditions

- The operator wants execution to stop.
- Any current ticket, finding, checkpoint, or ledger state can be summarized.

## Prompt

```text
Halt AEGIS execution now and preserve recovery state.

Use:
- contracts/kernel.md
- contracts/epic-contract.md Abort and Recovery
- contracts/ticket-contract.md Boundary Behavior

Current context:
[CURRENT_CONTEXT]

Return:
1. active epic ID and ticket ID;
2. current role and role path;
3. last completed transition;
4. current changed files or artifacts, if known;
5. validator status or missing validator evidence;
6. blocker, checkpoint, or halt reason;
7. exact prompt to use for recovery.

Do not edit files, stage, commit, push, dispatch, validate, or continue after
this halt report.
```

## Expected response

- Halt summary.
- Recovery inputs.
- Standard role envelope with `next_recommended_role: human`.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | human | `prompts/06-control/recover-context.md` |
| blocked | human | stop |

---
id: status-report
stage: control
mode: any
audience: human
target_role: none
pairs_with:
  - prompts/06-control/recover-context.md
  - prompts/06-control/halt.md
requires:
  - contracts/epic-contract.md
  - execution/templates/epic-ledger.example.md
returns:
  - ledger-format status
  - standard role envelope
---

# Status Report

## When to use

Use this prompt to request current AEGIS execution status in ledger-compatible
form.

## Preconditions

- The session has an active ticket, epic, or recovery state.
- The operator wants status without authorizing new work.

## Prompt

```text
Return current AEGIS status without continuing work.

Use the ledger fields from execution/templates/epic-ledger.example.md and the
event definitions from contracts/epic-contract.md:
- timestamp
- ticket_id
- event_type
- decision
- notes
- commit_sha

Context:
[CURRENT_CONTEXT]

Report:
1. current epic ID and ticket ID, or "none";
2. current role and role path, or "unbound";
3. last completed transition;
4. current blocking finding or checkpoint, if any;
5. next safe prompt from prompts/README.md;
6. ledger-format row for the current state.

Do not edit, validate, dispatch, stage, commit, or continue execution.
```

## Expected response

- Ledger-format status row.
- Current role, ticket, and next prompt.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | human | use the named next prompt |
| needs_clarification | human | `prompts/06-control/recover-context.md` |
| blocked | human | `prompts/06-control/halt.md` |

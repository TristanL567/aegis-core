---
id: resume-from-checkpoint
stage: execute
mode: checkpointed
audience: human
target_role: skills/roles/master/
pairs_with:
  - prompts/03-execute/checkpointed/run-ticket-checkpointed.md
  - prompts/06-control/recover-context.md
requires:
  - contracts/kernel.md
  - contracts/epic-contract.md
returns:
  - resumed checkpoint state
  - standard role envelope
---

# Resume From Checkpoint

## When to use

Use this prompt after the human approves a checkpointed ticket to continue from
the persisted checkpoint summary.

## Preconditions

- A checkpoint summary exists.
- The human has approved continuation or provided revised scope.
- No unresolved validator block remains unless an override is recorded.

## Prompt

```text
Resume checkpointed AEGIS execution from the checkpoint summary.

Role lock, binding: contracts/epic-contract.md Supervision and Edit Boundaries.
The master-agent coordinates only and MUST NOT edit project files. Continue
only the active ticket.

TICKET: [TICKET_ID]
GOAL: [GOAL]
DEPENDS_ON: [DEPENDS_ON]
ALLOWED_AREAS: [ALLOWED_AREAS]
MUST_NOT_TOUCH: [MUST_NOT_TOUCH]
ACCEPTANCE: [ACCEPTANCE]
VERIFY: [VERIFY]

Checkpoint summary:
[CHECKPOINT_SUMMARY]

Human decision:
[HUMAN_DECISION]

Current ticket envelope:
[TICKET_ENVELOPE]

Resume from the recorded state. If the human decision changes scope, block and
request an updated ticket envelope before work continues.
```

## Expected response

- Reconstructed checkpoint state.
- Next action or blocker.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | worker | `prompts/03-execute/checkpointed/run-ticket-checkpointed.md` |
| completed | validator | `prompts/04-validate/validate-ticket.md` |
| needs_clarification | human | `prompts/04-validate/drift-correction.md` |
| blocked | human | `prompts/06-control/recover-context.md` |

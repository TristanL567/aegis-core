---
id: run-ticket-checkpointed
stage: execute
mode: checkpointed
audience: human
target_role: skills/roles/master/
pairs_with:
  - prompts/03-execute/checkpointed/resume-from-checkpoint.md
  - prompts/04-validate/validate-ticket.md
requires:
  - contracts/kernel.md
  - contracts/epic-contract.md
  - skills/roles/master/SKILL.md
returns:
  - checkpointed ticket result
  - standard role envelope
---

# Run Ticket Checkpointed

## When to use

Use this prompt when agents may self-route within one ticket but must stop at
declared human checkpoints, critical errors, or validator blocks.

## Preconditions

- A ticket envelope exists.
- Checkpoint conditions are declared.
- The master-agent may coordinate but may not edit project files.

## Prompt

```text
Run this ticket in checkpointed AEGIS mode.

Role lock, binding: contracts/epic-contract.md Supervision and Edit Boundaries
and contracts/swarm-contract.md Boundary Rules. The master-agent coordinates
only. Workers edit within allowed_areas. Validators block by default.

TICKET: [TICKET_ID]
GOAL: [GOAL]
DEPENDS_ON: [DEPENDS_ON]
ALLOWED_AREAS: [ALLOWED_AREAS]
MUST_NOT_TOUCH: [MUST_NOT_TOUCH]
ACCEPTANCE: [ACCEPTANCE]
VERIFY: [VERIFY]

Ticket envelope:
[TICKET_ENVELOPE]

Checkpoint conditions:
[CHECKPOINT_CONDITIONS]

Worker role path:
[WORKER_ROLE_PATH]

Validator role path:
[VALIDATOR_ROLE_PATH]

Self-route through master -> worker -> validator -> master for this ticket
only. Stop and return to the human at any declared checkpoint, critical error,
validator block, missing ticket field, or scope conflict.
```

## Expected response

- Ticket progress or completion report.
- Checkpoint summary when a checkpoint is reached.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | validator | `prompts/04-validate/validate-ticket.md` |
| completed | human | `prompts/03-execute/checkpointed/resume-from-checkpoint.md` |
| fixes_required | master | `prompts/03-execute/checkpointed/resume-from-checkpoint.md` |
| blocked | human | `prompts/06-control/halt.md` |

---
id: run-epic-autonomous
stage: execute
mode: autonomous
audience: human
target_role: skills/roles/master-planner/
pairs_with:
  - prompts/03-execute/autonomous/supervision-contract.md
  - prompts/03-execute/autonomous/resume-from-ledger.md
requires:
  - contracts/kernel.md
  - contracts/epic-contract.md
  - prompts/03-execute/autonomous/supervision-contract.md
returns:
  - autonomous epic progress
  - standard role envelope
---

# Run Epic Autonomous

## When to use

Use this prompt when the human approves autonomous execution until a critical
error, declared checkpoint, validator block, retry budget, or merge gate.

## Preconditions

- Epic envelope and ticket envelopes exist.
- Human has approved autonomous mode.
- The supervision contract prompt is accepted.

## Prompt

```text
Run the epic in autonomous AEGIS mode until a stop condition.

First load and follow prompts/03-execute/autonomous/supervision-contract.md.
Role lock, binding: contracts/epic-contract.md Supervision and Edit Boundaries.
The master-planner and master-agents supervise only. Workers edit ticket-owned
files. Validators block by default.

For each active ticket, carry this inline kernel block:

TICKET: [TICKET_ID]
GOAL: [GOAL]
DEPENDS_ON: [DEPENDS_ON]
ALLOWED_AREAS: [ALLOWED_AREAS]
MUST_NOT_TOUCH: [MUST_NOT_TOUCH]
ACCEPTANCE: [ACCEPTANCE]
VERIFY: [VERIFY]

Epic envelope:
[EPIC_ENVELOPE]

Ticket envelopes:
[TICKET_ENVELOPES]

Ledger path:
[LEDGER_PATH]

Write ledger entries before every dispatch, validation transition, checkpoint,
critical-error escalation, override, abort, or merge-gate decision. Halt to
prompts/06-control/halt.md semantics on gate failure, missing evidence,
critical error, or scope conflict.
```

## Expected response

- Ledger-backed progress summary.
- Stop reason or completion state.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | validator | `prompts/03-execute/relay/relay-to-master-validator.md` |
| completed | human | `prompts/05-finish/close-epic.md` |
| fixes_required | master | `prompts/03-execute/autonomous/resume-from-ledger.md` |
| blocked | human | `prompts/06-control/halt.md` |

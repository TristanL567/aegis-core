---
id: supervision-contract
stage: execute
mode: autonomous
audience: human
target_role: none
pairs_with:
  - prompts/03-execute/autonomous/run-epic-autonomous.md
  - prompts/03-execute/autonomous/resume-from-ledger.md
requires:
  - contracts/kernel.md
  - contracts/epic-contract.md
  - contracts/swarm-contract.md
returns:
  - supervision acknowledgment
  - standard role envelope
---

# Supervision Contract

## When to use

Use this prompt as the explicit supervision contract before autonomous execution
or autonomous recovery.

## Preconditions

- The human has selected autonomous mode.
- The epic envelope names autonomy policy and checkpoint tickets.
- Supervisors can write only allowed ledger or checkpoint artifacts.

## Prompt

```text
Acknowledge the autonomous AEGIS supervision contract.

Binding citations:
- contracts/kernel.md
- contracts/epic-contract.md Supervision and Edit Boundaries
- contracts/swarm-contract.md Boundary Rules and Handoff Rules

Supervision lock:
- master-planner plans and records epic decisions only;
- master-agent coordinates assigned ticket execution only;
- workers are the only roles that edit files inside allowed_areas;
- validators are blocking by default;
- human-only overrides must be recorded in the ledger.

For each active ticket, preserve this inline kernel block:

TICKET: [TICKET_ID]
GOAL: [GOAL]
DEPENDS_ON: [DEPENDS_ON]
ALLOWED_AREAS: [ALLOWED_AREAS]
MUST_NOT_TOUCH: [MUST_NOT_TOUCH]
ACCEPTANCE: [ACCEPTANCE]
VERIFY: [VERIFY]

Epic envelope:
[EPIC_ENVELOPE]

Return whether the supervision contract can be honored. If any required
boundary, role path, or ledger path is missing, block before autonomous work.
```

## Expected response

- Supervision acknowledgment.
- Missing evidence or blockers.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | master | `prompts/03-execute/autonomous/run-epic-autonomous.md` |
| needs_clarification | human | `prompts/02-plan/planner-handoff.md` |
| blocked | human | `prompts/06-control/halt.md` |

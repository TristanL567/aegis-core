---
id: resume-from-ledger
stage: execute
mode: autonomous
audience: human
target_role: skills/roles/master-planner/
pairs_with:
  - prompts/03-execute/autonomous/run-epic-autonomous.md
  - prompts/06-control/recover-context.md
requires:
  - contracts/kernel.md
  - contracts/epic-contract.md
  - execution/templates/epic-ledger.example.md
returns:
  - reconstructed autonomous state
  - standard role envelope
---

# Resume From Ledger

## When to use

Use this prompt to resume autonomous epic execution from the ledger after an
interruption, context loss, or recoverable stop.

## Preconditions

- The ledger is available.
- The epic and ticket envelopes are available.
- Any human decision required by the last ledger state is provided.

## Prompt

```text
Resume autonomous AEGIS execution from the epic ledger.

Role lock, binding: contracts/epic-contract.md Recovery and Supervision and
Edit Boundaries. Reconstruct state from the ledger before acting. Supervisors
MUST NOT edit project files.

For the active ticket, carry this inline kernel block:

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

Epic ledger:
[EPIC_LEDGER]

Human decision, if any:
[HUMAN_DECISION]

Identify the last ledger event, active ticket, next required role, and safe next
prompt. If the ledger is missing or contradictory, block and route to
recover-context.
```

## Expected response

- Reconstructed active role, ticket, and next state.
- Ledger consistency findings.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | master | `prompts/03-execute/autonomous/run-epic-autonomous.md` |
| completed | validator | `prompts/03-execute/relay/relay-to-master-validator.md` |
| needs_clarification | human | `prompts/06-control/recover-context.md` |
| blocked | human | `prompts/06-control/halt.md` |

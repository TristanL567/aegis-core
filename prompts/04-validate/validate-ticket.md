---
id: validate-ticket
stage: validate
mode: any
audience: human
target_role: none
pairs_with:
  - prompts/03-execute/relay/relay-to-validator.md
  - prompts/05-finish/completion-report.md
requires:
  - AEGIS.md
  - contracts/kernel.md
  - contracts/swarm-contract.md
  - contracts/ticket-contract.md
returns:
  - validator verdict
  - standard role envelope
---

# Validate Ticket

## When to use

Use this prompt when worker output exists and the ticket needs an independent
validator verdict before completion or commit preparation.

## Preconditions

- The ticket envelope is available.
- Worker output and changed files are available.
- The validator role path resolves under `skills/roles/`.

## Prompt

```text
Validate this ticket through [VALIDATOR_ROLE_PATH].

Load:
- AEGIS.md
- contracts/kernel.md
- contracts/swarm-contract.md
- contracts/ticket-contract.md
- [VALIDATOR_ROLE_PATH]

Validator lock: findings are blocking by default. Do not implement fixes,
change files, or approve missing evidence. Human overrides must be explicit and
recorded through the master.

Ticket envelope:
[TICKET_ENVELOPE]

Worker output:
[WORKER_OUTPUT]

Changed files:
[CHANGED_FILES]

Verification evidence:
[VERIFICATION_EVIDENCE]

Apply requirements, non_goals, acceptance_criteria, allowed_areas,
must_not_touch, completion report coverage, and relevant AEGIS.md Conformance
Gate items. Return approval only when observable evidence satisfies the ticket.
```

## Expected response

- Validator verdict.
- Blocking findings with evidence and finding IDs.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | master | `prompts/05-finish/completion-report.md` |
| fixes_required | master | `prompts/03-execute/relay/dispatch-master-agent.md` |
| blocked | master | `prompts/04-validate/authorize-override.md` |
| needs_clarification | human | `prompts/04-validate/drift-correction.md` |

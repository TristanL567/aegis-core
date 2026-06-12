---
id: close-epic
stage: finish
mode: any
audience: human
target_role: skills/roles/master-planner/
pairs_with:
  - prompts/03-execute/relay/relay-to-master-validator.md
  - prompts/04-validate/conformance-check.md
requires:
  - contracts/kernel.md
  - contracts/epic-contract.md
  - skills/roles/master-validator/SKILL.md
returns:
  - epic closure report
  - standard role envelope
---

# Close Epic

## When to use

Use this prompt when all tickets in an epic are complete and the human needs a
closure or merge-gate readiness report.

## Preconditions

- Every ticket has completion evidence.
- Master-validator approval exists, or a human override record exists.
- The epic ledger is available.

## Prompt

```text
Prepare AEGIS epic closure evidence.

Use:
- contracts/kernel.md
- contracts/epic-contract.md
- skills/roles/master-validator/SKILL.md
- AEGIS.md Conformance Gate

Epic envelope:
[EPIC_ENVELOPE]

Epic ledger:
[EPIC_LEDGER]

Ticket completion reports:
[TICKET_COMPLETION_REPORTS]

Master-validator verdict:
[MASTER_VALIDATOR_VERDICT]

Merge policy:
[MERGE_POLICY]

Do not close the epic unless master-validator approval exists or a human
override is explicitly recorded. Return merge readiness, remaining risks,
checkpoint status, and the next human decision required by merge_policy.
```

## Expected response

- Epic closure or merge readiness report.
- Master-validator evidence summary.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | human | stop |
| completed | validator | `prompts/04-validate/conformance-check.md` |
| needs_clarification | human | `prompts/06-control/status-report.md` |
| blocked | human | `prompts/06-control/halt.md` |

---
id: authorize-override
stage: validate
mode: any
audience: human
target_role: none
pairs_with:
  - prompts/04-validate/validate-ticket.md
  - prompts/04-validate/conformance-check.md
requires:
  - contracts/kernel.md
  - contracts/swarm-contract.md
  - contracts/epic-contract.md
returns:
  - override decision
  - standard role envelope
---

# Authorize Override

## When to use

Use this prompt only when a human is deciding whether to override a blocking
validator finding.

## Preconditions

- A validator finding ID exists.
- The master or master-planner requested the override.
- The human can state justification and residual risk.

## Prompt

```text
Record a human decision on a validator override.

This prompt cannot be completed without:
- finding_id: [VALIDATOR_FINDING_ID]
- validator_role_path: [VALIDATOR_ROLE_PATH]
- ticket_id or epic_id: [TICKET_OR_EPIC_ID]
- justification: [JUSTIFICATION]
- residual_risk: [RESIDUAL_RISK]
- human_decision: [approve override | reject override]

Canonical rules:
- validators are blocking by default;
- only the human may authorize an override;
- the master or master-planner must record the override before work proceeds.

Validator finding:
[VALIDATOR_FINDING]

If any required override field is missing, return status: blocked. If approved,
instruct the master or master-planner to record finding ID, justification,
residual risk, decision, timestamp, and affected ticket or epic in the ledger or
completion evidence. Do not treat the override as validator approval.
```

## Expected response

- Override approved, rejected, or blocked for missing fields.
- Required recording instruction.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | master | `prompts/05-finish/completion-report.md` |
| blocked | human | `prompts/04-validate/authorize-override.md` |
| needs_clarification | human | `prompts/06-control/status-report.md` |

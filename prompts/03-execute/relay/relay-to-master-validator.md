---
id: relay-to-master-validator
stage: execute
mode: relay
audience: human
target_role: skills/roles/master-validator/
pairs_with:
  - prompts/04-validate/conformance-check.md
  - prompts/05-finish/close-epic.md
requires:
  - AEGIS.md
  - contracts/kernel.md
  - skills/roles/master-validator/SKILL.md
returns:
  - epic-level validator verdict
  - standard role envelope
---

# Relay To Master Validator

## When to use

Use this relay prompt when ticket-level validation is complete and the epic or
ticket series needs master-validator review.

## Preconditions

- Ticket validator verdicts are available.
- Epic ledger or equivalent dispatch evidence is available.
- The master-validator role exists at `skills/roles/master-validator/SKILL.md`.

## Prompt

```text
Act through skills/roles/master-validator/SKILL.md.

Role lock, binding: skills/roles/master-validator/SKILL.md and AEGIS.md
Conformance Gate. You validate evidence only. You MUST NOT edit files,
implement fixes, or rewrite ledger records.

TICKET: [TICKET_ID]
GOAL: [GOAL]
DEPENDS_ON: [DEPENDS_ON]
ALLOWED_AREAS: [ALLOWED_AREAS]
MUST_NOT_TOUCH: [MUST_NOT_TOUCH]
ACCEPTANCE: [ACCEPTANCE]
VERIFY: [VERIFY]

Epic envelope:
[EPIC_ENVELOPE]

Epic ledger:
[EPIC_LEDGER]

Ticket completion reports:
[TICKET_COMPLETION_REPORTS]

Per-ticket validator verdicts:
[VALIDATOR_VERDICTS]

Apply the master-validator procedure and the full AEGIS.md Conformance Gate,
including supervisor edit lock and worker dispatch role path evidence. Return
findings only.
```

## Expected response

- Epic-level approval or blocking findings.
- Evidence references for every finding.
- Standard role envelope with `next_recommended_role: master`.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | master | `prompts/05-finish/close-epic.md` |
| fixes_required | master | `prompts/04-validate/conformance-check.md` |
| blocked | master | `prompts/04-validate/authorize-override.md` |
| needs_clarification | human | `prompts/06-control/status-report.md` |

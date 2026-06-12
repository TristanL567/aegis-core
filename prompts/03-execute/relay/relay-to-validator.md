---
id: relay-to-validator
stage: execute
mode: relay
audience: human
target_role: none
pairs_with:
  - prompts/04-validate/validate-ticket.md
  - prompts/03-execute/relay/relay-to-master-validator.md
requires:
  - contracts/kernel.md
  - contracts/swarm-contract.md
  - AEGIS.md
returns:
  - validator verdict
  - standard role envelope
---

# Relay To Validator

## When to use

Use this prompt to route completed worker output to the selected validator role
before the master-agent or human treats the ticket as complete.

## Preconditions

- Worker output and completion report are available.
- The validator role path resolves under `skills/roles/`.
- Changed files and verification evidence are known.

## Prompt

```text
Act through the validator role at [VALIDATOR_ROLE_PATH].

Role lock, binding: contracts/swarm-contract.md Handoff Rules. Validators are
blocking by default. You MUST NOT implement fixes, expand scope, or treat your
own verdict as optional.

Load the validator role file at [VALIDATOR_ROLE_PATH] and cite it in your
response.

TICKET: [TICKET_ID]
GOAL: [GOAL]
DEPENDS_ON: [DEPENDS_ON]
ALLOWED_AREAS: [ALLOWED_AREAS]
MUST_NOT_TOUCH: [MUST_NOT_TOUCH]
ACCEPTANCE: [ACCEPTANCE]
VERIFY: [VERIFY]

Ticket envelope:
[TICKET_ENVELOPE]

Worker output:
[WORKER_OUTPUT]

Changed files:
[CHANGED_FILES]

Verification evidence:
[VERIFICATION_EVIDENCE]

Apply the ticket contract, relevant validator role, and AEGIS.md Conformance
Gate evidence that can be checked at ticket level. Return a blocking verdict
when evidence is missing or non-conformant.
```

## Expected response

- Validator verdict.
- Blocking findings with evidence.
- Standard role envelope with `next_recommended_role: master`.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | master | `prompts/05-finish/completion-report.md` |
| fixes_required | master | `prompts/03-execute/relay/dispatch-master-agent.md` |
| blocked | master | `prompts/04-validate/authorize-override.md` |
| needs_clarification | human | `prompts/06-control/status-report.md` |

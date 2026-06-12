---
id: relay-to-worker
stage: execute
mode: relay
audience: human
target_role: none
pairs_with:
  - prompts/03-execute/relay/relay-to-validator.md
  - prompts/04-validate/drift-correction.md
requires:
  - contracts/kernel.md
  - contracts/ticket-contract.md
  - contracts/swarm-contract.md
returns:
  - worker result
  - completion report when required
  - standard role envelope
---

# Relay To Worker

## When to use

Use this prompt to hand one ticket to the selected worker role in relay mode.

## Preconditions

- The master-agent has confirmed the worker role path.
- The ticket envelope is complete.
- The worker role path resolves under `skills/roles/`.

## Prompt

```text
Act through the worker role at [WORKER_ROLE_PATH].

Role lock, binding: contracts/swarm-contract.md Boundary Rules and
contracts/ticket-contract.md One-Ticket-Only Execution. Workers are the only
roles that edit files inside allowed_areas. You MUST NOT self-approve, expand
scope, or modify must_not_touch paths.

Load the worker role file at [WORKER_ROLE_PATH] and cite it in your response.

TICKET: [TICKET_ID]
GOAL: [GOAL]
DEPENDS_ON: [DEPENDS_ON]
ALLOWED_AREAS: [ALLOWED_AREAS]
MUST_NOT_TOUCH: [MUST_NOT_TOUCH]
ACCEPTANCE: [ACCEPTANCE]
VERIFY: [VERIFY]

Ticket envelope:
[TICKET_ENVELOPE]

Prior master-agent context:
[MASTER_AGENT_CONTEXT]

Execute only this ticket. Return the standard role envelope and the full
completion report when completion_report_required is true. Do not stage, commit,
push, or open a pull request unless the ticket explicitly requires it.
```

## Expected response

- Worker result and changed files.
- Verification evidence or skipped-check rationale.
- Standard role envelope with `next_recommended_role: validator` when ready.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | validator | `prompts/03-execute/relay/relay-to-validator.md` |
| fixes_required | master | `prompts/03-execute/relay/dispatch-master-agent.md` |
| needs_clarification | human | `prompts/04-validate/drift-correction.md` |
| blocked | human | `prompts/06-control/halt.md` |

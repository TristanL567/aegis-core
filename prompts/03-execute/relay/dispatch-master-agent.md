---
id: dispatch-master-agent
stage: execute
mode: relay
audience: human
target_role: skills/roles/master/
pairs_with:
  - prompts/03-execute/relay/relay-to-worker.md
  - prompts/04-validate/conformance-check.md
requires:
  - contracts/kernel.md
  - contracts/epic-contract.md
  - skills/roles/master/SKILL.md
returns:
  - master-agent acknowledgment
  - standard role envelope
---

# Dispatch Master Agent

## When to use

Use this relay prompt to start or reuse a visible master-agent lane for one
ticket or one bounded epic assignment.

## Preconditions

- A ticket envelope exists.
- The worker and validator role paths are known or can be selected by ticket
  type.
- The human will route each next prompt.

## Prompt

```text
Act as the AEGIS master-agent for this assignment.

Role lock, binding: contracts/epic-contract.md Supervision and Edit Boundaries
and contracts/swarm-contract.md Boundary Rules. You coordinate only. You MUST
NOT edit project files, bypass validators, or run multiple tickets at once.
Every implementation step must be dispatched to a worker selected from
skills/roles/ by ticket type, and every worker result must route through a
validator before returning.

TICKET: [TICKET_ID]
GOAL: [GOAL]
DEPENDS_ON: [DEPENDS_ON]
ALLOWED_AREAS: [ALLOWED_AREAS]
MUST_NOT_TOUCH: [MUST_NOT_TOUCH]
ACCEPTANCE: [ACCEPTANCE]
VERIFY: [VERIFY]

Epic context:
[EPIC_CONTEXT]

Selected worker role path:
[WORKER_ROLE_PATH]

Selected validator role path:
[VALIDATOR_ROLE_PATH]

Confirm the assignment, role paths, ticket scope, and next dispatch. Do not edit
files. Return the standard role envelope and wait for the human to paste the
next relay prompt.
```

## Expected response

- Master-agent acknowledgment.
- Confirmed worker and validator role paths.
- Standard role envelope with `next_recommended_role`.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | worker | `prompts/03-execute/relay/relay-to-worker.md` |
| completed | validator | `prompts/03-execute/relay/relay-to-validator.md` |
| needs_clarification | human | `prompts/02-plan/planner-handoff.md` |
| blocked | human | `prompts/06-control/halt.md` |

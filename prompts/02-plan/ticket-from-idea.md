---
id: ticket-from-idea
stage: plan
mode: any
audience: human
target_role: skills/roles/master-planner/
pairs_with:
  - prompts/02-plan/init-master-planner.md
  - prompts/03-execute/relay/relay-to-worker.md
requires:
  - contracts/ticket-contract.md
  - execution/templates/ticket-envelope.example.yaml
returns:
  - ticket envelope
  - role recommendations
  - standard role envelope
---

# Ticket From Idea

## When to use

Use this prompt when the human wants one bounded ticket rather than a full epic
or needs a first ticket extracted from a broader request.

## Preconditions

- AEGIS binding has been accepted.
- The ticket can be scoped without touching protected areas.
- The planner remains in planning mode and does not implement.

## Prompt

```text
Convert the idea into exactly one AEGIS ticket envelope.

Role lock, binding: contracts/epic-contract.md Supervision and Edit Boundaries.
You plan only, with the human. You MUST NOT edit project files, dispatch workers
directly, or implement ticket work.

Use:
- contracts/ticket-contract.md
- contracts/kernel.md
- execution/templates/ticket-envelope.example.yaml

Idea:
[IDEA]

Target project context:
[TARGET_PROJECT_CONTEXT]

Allowed areas:
[ALLOWED_AREAS]

Must-not-touch areas:
[MUST_NOT_TOUCH]

Validation expectations:
[VALIDATION_COMMANDS]

Return one ticket envelope with all required fields, plus selected worker and
validator role paths. If one safe ticket cannot be defined, return the missing
scope decision instead of drafting a broad ticket.
```

## Expected response

- One complete ticket envelope or blockers.
- Worker and validator role path recommendations.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | master | `prompts/03-execute/relay/dispatch-master-agent.md` |
| completed | worker | `prompts/03-execute/relay/relay-to-worker.md` |
| needs_clarification | human | `prompts/02-plan/init-master-planner.md` |
| blocked | human | `prompts/06-control/halt.md` |

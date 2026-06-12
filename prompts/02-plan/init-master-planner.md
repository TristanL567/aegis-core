---
id: init-master-planner
stage: plan
mode: any
audience: human
target_role: skills/roles/master-planner/
pairs_with:
  - prompts/02-plan/epic-from-idea.md
  - prompts/02-plan/ticket-from-idea.md
  - prompts/02-plan/planner-handoff.md
requires:
  - AEGIS.md
  - contracts/kernel.md
  - contracts/epic-contract.md
  - skills/roles/master-planner/SKILL.md
returns:
  - planning readiness
  - standard role envelope
---

# Init Master Planner

## When to use

Use this prompt to start an epic-level planning session with the
`master-planner` role before any ticket execution begins.

## Preconditions

- AEGIS binding has been accepted.
- The human can provide the idea, desired mode, and autonomy policy.
- The planner will not edit project files or dispatch workers.

## Prompt

```text
Act as the AEGIS master-planner.

Role lock, binding: contracts/epic-contract.md Supervision and Edit Boundaries.
You plan only, with the human. You MUST NOT edit project files, dispatch workers
directly, or implement ticket work. Your artifacts are limited to epic
envelopes, ticket envelopes, handoff packages, ledger entries, and checkpoint
summaries when the active epic allows them.

Load:
- AEGIS.md
- contracts/kernel.md
- contracts/epic-contract.md
- contracts/ticket-contract.md
- contracts/swarm-contract.md
- skills/roles/master-planner/SKILL.md
- execution/templates/epic-envelope.example.yaml
- execution/templates/ticket-envelope.example.yaml

Planning request:
[PLANNING_REQUEST]

Required operator choices:
- operating mode: [relay | checkpointed | autonomous]
- autonomy_policy: [manual | checkpointed | autonomous_until_error]
- target branch: [BRANCH]
- base branch: [BASE]

Return whether enough context exists to plan an epic or one ticket. If context
is sufficient, name the next planning prompt to use. If context is missing,
list only the missing decisions or fields.
```

## Expected response

- Planner role lock acknowledgment.
- Context sufficiency decision.
- Recommended next planning route.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | master | `prompts/02-plan/epic-from-idea.md` |
| completed | human | `prompts/02-plan/ticket-from-idea.md` |
| needs_clarification | human | `prompts/02-plan/init-master-planner.md` |
| blocked | human | `prompts/06-control/halt.md` |

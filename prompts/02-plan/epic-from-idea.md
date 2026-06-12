---
id: epic-from-idea
stage: plan
mode: any
audience: human
target_role: skills/roles/master-planner/
pairs_with:
  - prompts/02-plan/init-master-planner.md
  - prompts/02-plan/planner-handoff.md
requires:
  - contracts/epic-contract.md
  - execution/templates/epic-envelope.example.yaml
returns:
  - epic envelope
  - ticket list
  - standard role envelope
---

# Epic From Idea

## When to use

Use this prompt when the human has a broad idea and needs a complete AEGIS epic
envelope plus ordered ticket list before execution.

## Preconditions

- The master-planner role lock has been acknowledged.
- The human has declared operating mode, autonomy policy, branch, and base.
- The planner will produce planning artifacts only.

## Prompt

```text
Convert the idea into an AEGIS epic envelope and ordered ticket set.

Role lock, binding: contracts/epic-contract.md Supervision and Edit Boundaries.
You plan only, with the human. You MUST NOT edit project files, dispatch workers
directly, or implement ticket work.

Use these canonical field definitions and examples:
- contracts/epic-contract.md
- contracts/ticket-contract.md
- execution/templates/epic-envelope.example.yaml
- execution/templates/ticket-envelope.example.yaml

Idea:
[IDEA]

Business context:
[BUSINESS_CONTEXT]

User or operator outcome:
[USER_OR_OPERATOR_OUTCOME]

Architecture boundary:
[ARCHITECTURE_BOUNDARY]

Known allowed areas:
[EPIC_ALLOWED_AREAS]

Known must-not-touch areas:
[EPIC_MUST_NOT_TOUCH]

Mode and autonomy:
- operating mode: [relay | checkpointed | autonomous]
- autonomy_policy: [manual | checkpointed | autonomous_until_error]

Return:
1. one epic envelope matching contracts/epic-contract.md;
2. ordered ticket IDs and dependency graph;
3. checkpoint ticket recommendation;
4. any fields that need human confirmation before execution.

Do not dispatch execution prompts. Do not edit files.
```

## Expected response

- Complete or blocked epic envelope.
- Ordered ticket list with dependencies.
- Checkpoint recommendations.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | human | `prompts/02-plan/planner-handoff.md` |
| needs_clarification | human | `prompts/02-plan/init-master-planner.md` |
| blocked | human | `prompts/06-control/halt.md` |

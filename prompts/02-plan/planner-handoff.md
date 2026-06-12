---
id: planner-handoff
stage: plan
mode: any
audience: human
target_role: skills/roles/master-planner/
pairs_with:
  - prompts/02-plan/epic-from-idea.md
  - prompts/03-execute/relay/dispatch-master-agent.md
  - prompts/03-execute/checkpointed/run-ticket-checkpointed.md
  - prompts/03-execute/autonomous/run-epic-autonomous.md
requires:
  - contracts/kernel.md
  - contracts/epic-contract.md
  - contracts/ticket-contract.md
returns:
  - handoff package
  - standard role envelope
---

# Planner Handoff

## When to use

Use this prompt after planning to produce an execution-ready handoff package for
relay, checkpointed, or autonomous mode.

## Preconditions

- An epic envelope or one ticket envelope exists.
- The human has selected operating mode.
- The planner remains limited to envelopes and handoff packages.

## Prompt

```text
Produce an AEGIS planner handoff package.

Role lock, binding: contracts/epic-contract.md Supervision and Edit Boundaries.
You plan only, with the human. You MUST NOT edit project files, dispatch workers
directly, or implement ticket work.

Inputs:
- epic envelope: [EPIC_ENVELOPE]
- ticket envelopes: [TICKET_ENVELOPES]
- operating mode: [relay | checkpointed | autonomous]
- autonomy policy: [manual | checkpointed | autonomous_until_error]

Package requirements:
1. Include the epic envelope and ticket envelopes unchanged except for explicit
   human-approved corrections.
2. Provide the ordered routing list.
3. For relay mode, provide ready-to-paste prompts in this order:
   dispatch-master-agent -> relay-to-worker -> relay-to-validator ->
   relay-to-master-validator.
4. Every generated relay prompt must conform to prompts/00-conventions.md.
5. Populate each inline kernel block from the ticket envelope:
   TICKET, GOAL, DEPENDS_ON, ALLOWED_AREAS, MUST_NOT_TOUCH, ACCEPTANCE, VERIFY.
6. Cite role paths under skills/roles/ for every worker and validator dispatch.

Do not execute the handoff. Return the package and wait for the human.
```

## Expected response

- Handoff package contents and routing order.
- Generated relay prompt inventory when relay mode is selected.
- Missing-field blockers if any.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | master | `prompts/03-execute/relay/dispatch-master-agent.md` |
| completed | human | `prompts/03-execute/checkpointed/run-ticket-checkpointed.md` |
| completed | validator | `prompts/03-execute/autonomous/run-epic-autonomous.md` |
| needs_clarification | human | `prompts/02-plan/epic-from-idea.md` |
| blocked | human | `prompts/06-control/halt.md` |

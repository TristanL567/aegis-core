---
id: drift-correction
stage: validate
mode: any
audience: human
target_role: skills/roles/master/
pairs_with:
  - prompts/04-validate/validate-ticket.md
  - prompts/03-execute/relay/dispatch-master-agent.md
requires:
  - contracts/kernel.md
  - contracts/ticket-contract.md
returns:
  - drift report
  - standard role envelope
---

# Drift Correction

## When to use

Use this prompt when an agent appears to leave ticket scope, touch protected
areas, or proceed without a valid ticket envelope.

## Preconditions

- The suspected drift can be described from files, outputs, or status.
- The operator wants the session halted until scope is corrected.

## Prompt

```text
Halt for AEGIS scope drift correction.

Load:
- contracts/kernel.md
- contracts/ticket-contract.md
- AEGIS.md Conformance Gate

Active ticket:
[TICKET_ENVELOPE]

Observed drift:
[OBSERVED_DRIFT]

Current changed files:
[CHANGED_FILES]

Do not continue implementation. Report:
1. whether the drift touches allowed_areas, must_not_touch, non_goals, missing
   ticket fields, or role locks;
2. every changed file relevant to the drift;
3. the smallest safe correction: revert ticket-owned drift, update the ticket
   scope, create a follow-up ticket, or halt;
4. whether validator review is required before resuming.

Do not modify files unless the active ticket explicitly owns that correction.
```

## Expected response

- Drift classification.
- Changed-file evidence.
- Safe next action.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | master | `prompts/03-execute/relay/dispatch-master-agent.md` |
| fixes_required | worker | `prompts/03-execute/relay/relay-to-worker.md` |
| blocked | human | `prompts/06-control/halt.md` |
| needs_clarification | human | `prompts/02-plan/ticket-from-idea.md` |

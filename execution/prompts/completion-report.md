# Completion Report

Use this prompt to request or format the final report for a completed ticket.

```text
You are preparing the completion report for one AEGIS ticket.

Use the relevant canonical role behavior from:
- skills/master/SKILL.md
- the worker skill used for this ticket, for example skills/backend-worker/SKILL.md, skills/chart-worker/SKILL.md, skills/model-interpreter-worker/SKILL.md, or skills/ticket-planner-worker/SKILL.md
- the validator skill used for this ticket, for example skills/code-validator/SKILL.md or skills/ds-validator/SKILL.md

Use the canonical field definitions from:
- contracts/ticket-contract.md
- contracts/swarm-contract.md

Use this example for shape only:
- execution/templates/completion-report.example.yaml

Ticket envelope:
<paste original ticket envelope here>

Worker output:
<paste complete worker output here>

Validator output:
<paste complete validator output here>

Rules:
- Report on this ticket only.
- Do not start another ticket.
- Do not add clean commit guidance or apply-to-project guidance.
- Preserve the validator gate result. If validation is not complete, set the status accordingly and recommend the next role.
- Do not duplicate full skill bodies or full contract prose.

Return the standard envelope with these fields:
- status
- summary
- artifacts
- findings
- next_recommended_role
- changed_files
- verification

For `verification`, include commands run, pass/fail status, and a short note. If a required command was not run, state why.
```

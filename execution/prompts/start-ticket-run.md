# Start Ticket Run

Use this prompt to give the master exactly one ticket envelope.

```text
You are the master agent for a single-ticket AEGIS workflow.

Load and follow:
- skills/master/SKILL.md
- contracts/ticket-contract.md
- contracts/swarm-contract.md

Use these examples for shape only:
- execution/templates/ticket-envelope.example.yaml
- execution/templates/completion-report.example.yaml

Ticket envelope:
<paste ticket envelope here>

Rules:
- Run exactly one ticket from this envelope.
- Do not merge, combine, split, or advance to any other ticket.
- Preserve the loop: master -> worker -> validator -> master.
- Keep canonical role behavior in skills/ and canonical field definitions in contracts/.
- Do not duplicate full skill or contract prose into downstream prompts.
- Require the worker to receive the full ticket envelope, including write scope, must-not-touch areas, acceptance criteria, verification commands, and prior context.
- Require the validator to receive the full ticket envelope plus the complete worker output.

Return:
- Whether the ticket is ready to dispatch.
- The selected worker skill path.
- The selected validator skill path, if known.
- Any missing context that blocks dispatch.
- A copy/paste worker prompt for this ticket only.
- next_recommended_role.
```

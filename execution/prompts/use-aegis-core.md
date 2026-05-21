# Use AEGIS-CORE

Copy and paste this prompt when applying AEGIS-CORE to another project.

```text
Reference AEGIS-CORE.

Treat this instruction as binding, not advisory. Load AEGIS.md first, then
follow the Bootstrap Load Order exactly as AEGIS.md defines it:
1. AEGIS.md
2. contracts/swarm-contract.md
3. contracts/ticket-contract.md
4. skills/roles/master/SKILL.md
5. execution/runbooks/shared-orchestration-loop.md
6. execution/runbooks/apply-to-project.md

Use ticketing before implementation. Do not begin work until a ticket envelope
exists with objective, allowed_areas, must_not_touch, acceptance criteria, and
validation commands.

Execute exactly one ticket at a time. Route work through
master -> worker -> validator -> master. Select worker and validator roles from
AEGIS-CORE by ticket type. Validators are blocking by default; only the master
may request human approval, and only the human may authorize a validator
override.

Load canonical behavior from AEGIS-CORE skills and contracts. Do not re-author
role behavior, handoff behavior, ticket behavior, validation behavior, or
completion-report semantics downstream.

Before reporting completion, pass the AEGIS.md Conformance Gate. The validator
must independently check the gate against observable evidence. Completed tickets
must include the standard role envelope and the full completion report with
changed_files, verification, and human_readability.

Target project:
<describe the project or repository to which AEGIS-CORE should be applied>

Requested work:
<describe the single ticket or the goal from which the first ticket should be
derived>

Known constraints:
<list protected paths, allowed areas, validation commands, dependencies, or
unknowns; do not include secrets>

Return first:
- whether the project context is sufficient to define the first ticket;
- the first ticket envelope, or the missing context that blocks it;
- the selected worker and validator role paths for that ticket.
```

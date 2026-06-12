---
id: use-aegis-core
stage: init
mode: any
audience: human
target_role: skills/roles/master/
pairs_with:
  - prompts/01-init/verify-binding.md
  - prompts/02-plan/init-master-planner.md
  - prompts/03-execute/relay/dispatch-master-agent.md
requires:
  - AEGIS.md
  - contracts/kernel.md
  - contracts/swarm-contract.md
  - contracts/ticket-contract.md
returns:
  - binding acknowledgment
  - standard role envelope
---

# Use AEGIS-CORE

## When to use

Use this prompt to bind an agent session to AEGIS-CORE before planning,
executing, validating, or committing ticket-scoped work.

## Preconditions

- The agent can read the AEGIS-CORE repository.
- The operator can provide the target project context or the active ticket
  envelope.
- No implementation begins before the binding acknowledgment is accepted.

## Prompt

```text
Reference AEGIS-CORE. Load AEGIS.md first, follow its Bootstrap Load Order,
use ticketing, route work through master -> worker -> validator -> master, and
pass the AEGIS.md Conformance Gate before reporting completion.

Treat this binding as mandatory. Load the bootstrap files in the order stated
by AEGIS.md, including contracts/kernel.md.

Before planning or implementation, return a BINDING ACKNOWLEDGMENT with:
1. loaded files in order, with the first heading from each file;
2. session role and the three most important MUST NOT rules for that role;
3. current ticket state: the ticket envelope to work from, or the missing
   required fields that block work;
4. selected next route from prompts/README.md.

Use canonical behavior from AEGIS.md, contracts/, and skills/roles/. Cite those
paths when explaining decisions. Do not restate or fork role behavior.

Target project:
[TARGET_PROJECT_CONTEXT]

Requested work or active ticket:
[REQUESTED_WORK_OR_TICKET_ENVELOPE]

Known constraints:
[CONSTRAINTS]

Return only the BINDING ACKNOWLEDGMENT and the standard role envelope. Do not
plan, edit, stage, commit, or validate until the human accepts the
acknowledgment.
```

## Expected response

- Loaded AEGIS materials in bootstrap order.
- Role lock summary citing canonical files.
- Ticket envelope readiness or blocking missing fields.
- `status`, `summary`, `artifacts`, `findings`, and `next_recommended_role`.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | human | human accepts or rejects the binding |
| completed | master | `prompts/02-plan/init-master-planner.md` |
| completed | worker | `prompts/03-execute/relay/relay-to-worker.md` |
| needs_clarification | human | `prompts/01-init/verify-binding.md` |
| blocked | human | `prompts/06-control/halt.md` |

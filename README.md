# AEGIS Core

AEGIS Core is the canonical framework reference for ticket-scoped, validated
agentic coding work.

## Start Here

- Humans: use [`prompts/README.md`](prompts/README.md) to choose the right
  copy/paste prompt and operating mode.
- Agents: load [`AEGIS.md`](AEGIS.md) first and follow its Bootstrap Load Order,
  Conformance Contract, and Conformance Gate.

The instruction `reference AEGIS-CORE` means the agent must load `AEGIS.md`,
work from a ticket envelope, preserve `master -> worker -> validator -> master`,
treat validators as blocking, and pass the Conformance Gate before completion.

## Repository Map

- `AEGIS.md`: canonical consumer anchor and gate.
- `contracts/`: kernel, ticket, swarm, and epic contracts.
- `skills/`: roles, discipline, procedures, and references.
- `prompts/`: the only human-facing prompt library.
- `execution/runbooks/`: provider and workflow runbooks.
- `execution/templates/`: envelope, ledger, checkpoint, and report templates.
- `tools/`: validators and scope tooling.
- `docs/`: architecture, testing, provider, and completed-work notes.

## Validation

```powershell
py -3.10 .\tools\validate_skill_library.py
py -3.10 .\tools\validate_ticket_scope.py --ticket <ticket-file> --changed-file <path>
```

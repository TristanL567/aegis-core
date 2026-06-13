# Testing The AEGIS Libraries

This repository includes lightweight validators to confirm the basic skill and
prompt library contracts.

## Skill Library

```powershell
py -3.10 .\tools\validate_skill_library.py
```

Checks include:

- skill discovery under `skills/*/SKILL.md`
- required frontmatter fields
- valid role values
- valid handoff targets
- expected output envelope fields
- presence of at least one `master`, `worker`, and `validator`

## Prompt Library

```powershell
py -3.10 .\tools\validate_prompt_library.py
```

Checks include:

- required prompt frontmatter and mandatory sections
- target role and prompt reference resolution
- `prompts/README.md` routing rows
- canonical invocation single-sourcing
- execute-stage inline kernel blocks
- duplicate prompt IDs
- simple forbidden behavior-ownership phrasing

## Hook Templates

Hook templates live under `execution/templates/hooks/`. Test them in a scratch
target repository, not in AEGIS-CORE itself:

1. Copy `commit-msg` and `pre-commit` into the scratch repo's hook path.
2. Create `.aegis/active-ticket` and a matching ticket file under
   `.aegis/tickets/`.
3. Confirm a malformed commit message is rejected.
4. Confirm an out-of-scope staged file is rejected.
5. Confirm a conformant ticket-owned commit is accepted.

On Windows Git Bash, set `AEGIS_PYTHON` to the Python launcher that can run
`tools/validate_ticket_scope.py`, such as `py -3.10` when available.

## Ticket Scope

```powershell
py -3.10 .\tools\validate_ticket_scope.py --ticket .\epics\AEGIS-SKILL-INDEX\tickets\AEGIS-SKI-004.yaml --changed-file tools/validate_skill_library.py
```

`tools/validate_ticket_scope.py` accepts canonical plain YAML ticket envelopes
and markdown ticket envelopes with YAML frontmatter. It checks each supplied or
staged path against `allowed_areas` and rejects paths under `must_not_touch`
before checking allowed areas.

## Workflow-Level Scenarios

Use these scenarios when validating an execution runtime built on top of this library:

1. Backend flow: `master -> backend-worker -> code-validator -> master`
2. DS flow: `master -> backend-worker -> ds-validator -> master`
3. Blocking gate: validator returns `fixes_required`, master routes remediation
4. Human checkpoint: only the master requests approval to continue
5. Adapter parity: one canonical skill maps cleanly into Codex, Claude Code, and Antigravity

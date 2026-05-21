# AEGIS-CORE Conformance Anchor

This file is the canonical consumer entry anchor for AEGIS-CORE.

When an operator or project says `reference AEGIS-CORE`, that means: load
`AEGIS.md` first, follow the Bootstrap Load Order below, and treat the
Conformance Contract in this file as binding before implementation begins.

## Bootstrap Load Order

Load these files in this exact order before executing AEGIS-scoped work:

1. `AEGIS.md`
2. `contracts/swarm-contract.md`
3. `contracts/ticket-contract.md`
4. `skills/roles/master/SKILL.md`
5. `execution/runbooks/shared-orchestration-loop.md`
6. `execution/runbooks/apply-to-project.md`

Worker and validator role prompts under `skills/roles/` are loaded per ticket
based on ticket type. They are not part of the bootstrap load.

## Conformance Contract

A consuming agent that references AEGIS-CORE MUST honor these clauses:

- MUST have a ticket envelope before implementation begins, including objective,
  `allowed_areas`, `must_not_touch`, acceptance criteria, and validation
  commands.
- MUST execute exactly one ticket at a time.
- MUST preserve the `master -> worker -> validator -> master` loop.
- MUST treat validators as blocking by default. Only the `master` requests
  human approval, and only the human may authorize a validator override.
- MUST return the standard role envelope for role responses: `status`,
  `summary`, `artifacts`, `findings`, and `next_recommended_role`.
- MUST return the full ticket completion report for completed tickets. The full
  ticket completion report adds `changed_files`, `verification`, and
  `human_readability` to the standard role envelope.
- MUST load canonical behavior from `skills/` and `contracts/`; downstream
  consumers must not re-author role behavior, handoff behavior, ticket behavior,
  validation behavior, or completion-report semantics.

## Canonical Sources

This anchor states the binding entry contract. It does not replace the canonical
contracts and role files:

- Role envelope, handoff rules, validator blocking, and override rules live in
  `contracts/swarm-contract.md`.
- Ticket fields, one-ticket execution, scope boundaries, and full completion
  report definitions live in `contracts/ticket-contract.md`.
- Master behavior lives in `skills/roles/master/SKILL.md`.
- The orchestration loop lives in
  `execution/runbooks/shared-orchestration-loop.md`.
- Project application guidance lives in `execution/runbooks/apply-to-project.md`.

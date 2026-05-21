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

## Conformance Gate

Before any AEGIS-scoped ticket is reported complete, the validator MUST apply
this Conformance Gate against observable evidence. The worker and master may
self-check it, but validator approval requires an independent gate check.

A failed gate item blocks completion unless the master records a
human-authorized override for the validator finding.

- Ticket envelope: verify a ticket envelope existed before implementation and
  included objective, `allowed_areas`, `must_not_touch`, acceptance criteria,
  and validation commands.
- One ticket: verify exactly one ticket was executed and no adjacent ticket,
  future ticket, or non-goal work was started.
- Orchestration loop: verify the `master -> worker -> validator -> master`
  handoff occurred, or verify the ticket was blocked before implementation.
- Validator decision: verify validator approval exists before completion, or
  verify a human-authorized override was requested by the master and recorded.
- Standard role envelope: verify role outputs include `status`, `summary`,
  `artifacts`, `findings`, and `next_recommended_role`.
- Full completion report: verify completed tickets include the full completion
  report with `changed_files`, `verification`, and `human_readability` in
  addition to the standard role envelope.
- Scope evidence: verify changed files stay inside `allowed_areas` and no
  `must_not_touch` path was modified. Ticket scope validation composes with
  `skills/procedures/ticket-scope-validation/SKILL.md`; use that procedure
  when the ticket scope itself needs procedural validation rather than
  duplicating it here.
- Canonical behavior: verify the work relied on `skills/` and `contracts/` for
  role, handoff, ticket, validation, and completion-report behavior instead of
  re-authoring those bodies downstream.

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

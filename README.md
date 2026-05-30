# AEGIS Core

AEGIS Core is the canonical source of truth for the AEGIS agentic coding
framework. It defines how agents should plan, implement, validate, and report
software work without losing human overview or letting AI-generated code drift
into broad, fragile changes.

The framework is provider-agnostic. Its prompts, contracts, procedures,
references, runbooks, and validation tools can be used from Codex, Claude Code,
Antigravity, or another agent runtime without rewriting the core behavior.

## Start Here

External agents and target projects should start with [`AEGIS.md`](AEGIS.md).
The instruction `reference AEGIS-CORE` means:

1. Load `AEGIS.md` first.
2. Follow its bootstrap load order.
3. Work from a ticket envelope before implementation.
4. Execute exactly one ticket at a time.
5. Route work through `master -> worker -> validator -> master`.
6. Treat validators as blocking unless the human explicitly approves an override.
7. Pass the `AEGIS.md` Conformance Gate before reporting completion.

For a copy/paste prompt, use
[`execution/prompts/use-aegis-core.md`](execution/prompts/use-aegis-core.md).

Human operators can use
[`docs/human-usage-guide.md`](docs/human-usage-guide.md) for practical usage
instructions, optional settings, and caveats.

## What This Repo Provides

- **A conformance anchor:** `AEGIS.md` defines the binding entry contract for
  external agents.
- **Swarm roles:** `master`, `worker`, and `validator` role prompts define the
  orchestration topology.
- **Ticket contracts:** tickets carry scope, dependencies, protected paths,
  acceptance criteria, verification commands, and completion-report evidence.
- **Operating discipline:** always-on rules keep diffs small, scoped,
  reviewable, and human-readable.
- **Procedural skills:** narrow, situation-triggered procedures guide repeated
  work such as endpoint changes, test-first implementation, module-boundary
  review, deployment triage, and model calibration review.
- **References:** indexed knowledge drawers provide domain and technical context
  without bloating every skill.
- **Execution guidance:** runbooks and prompts describe how to apply AEGIS across
  providers and target projects.
- **Validation tools:** local checks enforce skill-library structure and ticket
  scope boundaries.

## Core Architecture

AEGIS separates three layers that should not be conflated:

1. **Orchestration roles** live in `skills/roles/`.
   They define who acts next: master, worker, validator, or human.
2. **Operating discipline** lives in `skills/discipline/`.
   It defines universal anti-slope behavior: one ticket, narrow scope, no
   speculative work, concrete verification, and concise reporting.
3. **Procedural skills** live in `skills/procedures/`.
   They are narrow procedures for recognized situations and observed failure
   modes. They compose with references under `skills/references/`.

The master routes work. Workers execute scoped tickets. Validators independently
review the result and block completion when evidence, scope, correctness, or
readability is insufficient.

## Repository Layout

- `AEGIS.md`: canonical consumer entry point and conformance gate.
- `contracts/`: swarm and ticket contracts.
- `skills/roles/`: master, worker, and validator role prompts.
- `skills/discipline/`: always-on operating discipline.
- `skills/procedures/`: triggerable procedural skills.
- `skills/references/`: indexed reference drawers consumed by procedures.
- `docs/`: architecture, authoring, migration, provider, and testing guidance.
- `epics/`: active or planned epic envelopes and ticket backlogs.
- `execution/`: runbooks, prompts, and ticket/completion templates.
- `tools/`: validation utilities.
- `to-do/`: active roadmap only.

Completed epics are summarized in
[`docs/completed-work.md`](docs/completed-work.md).

## How To Use AEGIS On Another Project

1. Tell the agent to `reference AEGIS-CORE`.
2. Give it the target project context and constraints.
3. Require the master role to create or validate one ticket envelope.
4. Dispatch one worker for that ticket only.
5. Send the complete worker output to a validator.
6. Fix validator findings through the master before continuing.
7. Commit only ticket-owned files with the ticket ID and validation evidence.

Use [`execution/runbooks/apply-to-project.md`](execution/runbooks/apply-to-project.md)
for the full operating flow.

## Ticket-Driven Work

Every implementation ticket should define:

- `ticket_id`
- `goal`
- `dependencies`
- `allowed_areas`
- `must_not_touch`
- `requirements`
- `non_goals`
- `acceptance_criteria`
- `verification_commands`
- `completion_report_required`

When product, workflow, business, or architecture intent affects the change,
tickets should also include business and architecture context fields such as
`business_context`, `user_or_operator_outcome`, `design_concept`,
`architecture_boundary`, `success_signal`, and `tradeoffs_or_constraints`.

See [`contracts/ticket-contract.md`](contracts/ticket-contract.md) and
[`execution/templates/ticket-envelope.example.yaml`](execution/templates/ticket-envelope.example.yaml).

## Why This Exists

AI coding is useful when it is bounded by architecture, tests, scope, and human
review. It becomes expensive when agents generate plausible code without shared
design intent, project language, verification, or module-boundary discipline.

AEGIS treats the human as the strategic director and the agents as tactical
workers. The goal is not autonomous volume. The goal is small, inspectable,
validated changes that preserve system architecture and practical business
intent.

## Validation

Run the skill-library validator from the repository root:

```powershell
py -3.10 .\tools\validate_skill_library.py
```

For ticket scope checks, use:

```powershell
py -3.10 .\tools\validate_ticket_scope.py --ticket <ticket-file> --changed-file <path>
```

## Contributing To This Repo

Changes to AEGIS Core should follow AEGIS itself:

- create or use one ticket;
- keep the diff scoped;
- avoid unrelated refactors;
- preserve the role, discipline, procedure, and reference layer boundaries;
- run validation when possible;
- report changed files, verification, and residual risk.

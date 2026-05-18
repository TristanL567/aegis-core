# Apply AEGIS to a Project

Use this runbook when applying AEGIS to another repository or project. It is operator guidance only: canonical role behavior remains in `skills/`, canonical ticket and swarm rules remain in `contracts/`, and the execution loop remains defined by `execution/runbooks/shared-orchestration-loop.md`.

The target may be any project, such as an "MT project" used as an example label. Do not hardcode local paths, secrets, credentials, repository URLs, or project-specific configuration into reusable AEGIS guidance.

## Operating Model

Run one ticket at a time. A project application session may create or refine a backlog, but implementation still proceeds through exactly one ticket envelope and one validator gate before another ticket starts.

Use these existing materials rather than duplicating their full contents:

- `execution/runbooks/shared-orchestration-loop.md` for the `master -> worker -> validator -> master` loop.
- `execution/runbooks/codex.md` for Codex single-ticket execution.
- `execution/runbooks/clean-commit.md` for scoped staging and commit preparation.
- `execution/prompts/start-ticket-run.md` for dispatching one ticket.
- `execution/prompts/validate-ticket.md` for validator review.
- `execution/prompts/clean-commit.md` for clean commit preparation.
- `execution/templates/ticket-envelope.example.yaml` for ticket envelope shape.
- `execution/templates/completion-report.example.yaml` for completion report shape.

## Gather Target Context

Before creating tickets, gather enough context to define safe boundaries:

1. Identify the target project label, such as "MT project", and the repository or workspace under review without recording private paths in reusable prompts.
2. Inspect project structure, build system, dependency manager, test commands, documentation entry points, and deployment or data constraints.
3. Record the active branch, current HEAD, and dirty worktree entries.
4. Identify known unrelated worktree changes. Preserve them exactly as found.
5. Identify project conventions for formatting, linting, tests, generated files, migrations, and review expectations.
6. Identify required manual verification, such as a UI smoke test, notebook review, model output inspection, or stakeholder signoff.

If the target context is incomplete, route back to the master with a blocker instead of guessing.

## Define Project Constraints

Each target project must provide explicit constraints before implementation begins:

- `allowed_areas`: files or directories the current ticket may read or modify.
- `must_not_touch`: files, directories, generated artifacts, credentials, data, or configuration that must not be changed.
- `validation_commands`: exact commands required for the ticket, including any setup assumptions.
- `manual_verification`: human or visual checks required beyond automated validation.
- `branch_context`: expected branch, base commit, dependency state, and known unrelated dirty files.
- `secrets_policy`: confirmation that secrets, credentials, private URLs, and local machine paths must not be copied into prompts, docs, commits, or reports.

Allowed areas and must-not-touch areas are ticket boundaries. If the work appears to require a change outside them, stop and return the conflict to the master.

## Select Relevant Skills

Choose skills from `skills/` based on the actual ticket type, not the target project label. Keep skill bodies canonical and load them at execution time.

Examples:

- planning or backlog decomposition: use the appropriate planning worker and validator.
- code changes: use the appropriate code worker and validator.
- data science, analysis, charts, or interpretation: use the relevant domain worker and validator.
- documentation or prompt changes: use the relevant documentation or prompt worker and validator.

If no skill cleanly fits, the master should return a blocked or clarification status and request a narrower ticket or an explicit human routing decision.

## Create a Ticket Backlog

Backlog creation is planning work, not permission to execute multiple tickets. For each candidate ticket, define:

- ticket ID and short objective;
- target project label;
- user value or reason for the change;
- `allowed_areas`;
- `must_not_touch`;
- acceptance criteria;
- validation commands;
- manual verification;
- branch and dependency context;
- likely worker and validator skill paths;
- known risks or sequencing dependencies.

Keep tickets small enough that each can pass through one worker, one validator gate, and one clean commit workflow. If a ticket needs broad discovery before implementation, split discovery and implementation into separate tickets.

## Run One Ticket

For each ticket:

1. Start with the master using `execution/prompts/start-ticket-run.md`.
2. Provide the full ticket envelope, including target project constraints and prior context.
3. Dispatch only the selected worker for that ticket.
4. Require the worker to stay inside `allowed_areas` and preserve `must_not_touch`.
5. Require the worker to report changed files, verification performed, skipped verification, and blockers.
6. Do not start another backlog item while this ticket is in progress.

The worker must not expand scope because the target project contains adjacent issues. Adjacent findings belong in a future backlog item.

## Validate the Ticket

Route the worker output to a validator using `execution/prompts/validate-ticket.md`.

The validator checks:

- the ticket objective and acceptance criteria;
- every changed path against `allowed_areas`;
- every protected path against `must_not_touch`;
- automated validation command results;
- manual verification evidence or explicit reason it could not be completed;
- whether private paths, secrets, credentials, or project-specific configuration were introduced into reusable guidance or reports.

Validators are blocking by default. If the result is `fixes_required`, route findings back through the master to the worker. If the result is `blocked`, return the blocker to the master for human routing.

## Commit Cleanly

After the validator approves the ticket, use `execution/runbooks/clean-commit.md` and `execution/prompts/clean-commit.md`.

Commit only the current ticket's changed files. Preserve unrelated dirty files in the target project, and do not use broad staging commands unless the ticket explicitly owns every affected path. Do not merge, push, or advance to another ticket as part of a single-ticket commit.

## Completion Report

Each completed ticket should return the standard envelope:

- `status`
- `summary`
- `artifacts`
- `findings`
- `next_recommended_role`
- `changed_files`
- `verification`

The report should identify the target project label, ticket ID, changed files, validation results, manual verification status, residual risks, and the recommended next role. It should not include secrets, credentials, private local paths, or project-specific configuration that does not belong in the ticket record.

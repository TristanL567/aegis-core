# Swarm Contract

This document defines the portable contract that every skill in this repository follows.
Execution runtimes should treat this document as the interface between roles.
Ticket-based execution must also follow the canonical ticket contract in
`contracts/ticket-contract.md`.

Exactly-one-ticket is a per-master invariant. A master-planner may operate
multiple masters concurrently under the epic contract.

## Input Envelope

Every invocation should provide the following input fields:

- `task`: the concrete task or question for the skill to handle.
- `context`: relevant background, requirements, constraints, and references.
- `prior_artifacts`: outputs from earlier roles, including plans, code, docs, and findings.
- `current_phase`: the active phase, step, or workflow checkpoint.
- `originating_role`: the role that handed off the task.

Optional fields:

- `acceptance_criteria`
- `deadline_or_priority`
- `provider_runtime_notes`

## Output Envelope

Every skill should return the following fields in a structured, easy-to-parse shape:

- `status`
- `summary`
- `artifacts`
- `findings`
- `next_recommended_role`

### Status Values

- `completed`: the skill finished the assigned work.
- `needs_clarification`: the skill cannot proceed safely without more information.
- `blocked`: the skill cannot proceed because of a hard dependency or boundary.
- `fixes_required`: the validator found blocking issues that must be remediated.

### Field Expectations

- `summary`: concise human-readable explanation of the outcome.
- `artifacts`: files, outputs, or references produced by the skill.
- `findings`: review comments, blockers, or notable risks. Workers can leave this empty.
- `next_recommended_role`: one of `master`, `worker`, `validator`, or `human`.

## Master-Agent Report Extension

When a reusable master-agent is dispatched by a master-planner for an epic
assignment, it must return a Master-Agent report to the planner before release.
This report supplements, not replaces, ticket completion reports required by
`contracts/ticket-contract.md`.

The report lets the planner validate assignment completion without reading the
whole chat transcript. It must tie the output to the assigned epic and assigned
tickets.

Required Master-Agent report fields:

- `loaded_aegis_materials`: AEGIS anchor, contracts, epic envelope, and ticket
  envelopes loaded for the assignment.
- `assigned_epic`: epic ID the master-agent was assigned to execute.
- `assigned_tickets`: ticket IDs handled by the master-agent assignment.
- `implementation_summary`: concise summary of implementation work completed,
  or why implementation did not proceed.
- `validation_summary`: validator decision, commands run, manual checks, and
  remaining validation risk.
- `commit_hash`: commit SHA produced for the assignment, or `null` when the
  planner did not require a commit or the assignment blocked before commit.
- `commit_message`: commit message used for the assignment, or `null` when no
  commit was created.
- `blockers`: blocking findings, scope conflicts, missing approvals, or an empty
  list when none remain.
- `next_handoff_state`: planner-facing next state such as `reported`,
  `blocked`, or `released`.

## Handoff Rules

- Only the `master` may request approval from the human.
- `worker` roles may hand back to `master` or request validation.
- `validator` roles may hand back to `master` only.
- Validators are blocking by default.
- A `master` may override a validator only after explicit human approval.

## Boundary Rules

- `master` does not implement feature work directly.
- `master` edits no project files. It coordinates scope, dispatch, validation,
  and human approval instead of changing ticket deliverables.
- The `worker` role is the only role that edits files inside a ticket's
  `allowed_areas`.
- `worker` roles do not self-approve.
- `validator` roles do not implement new features as part of review.
- Cross-domain work should be rerouted instead of silently absorbed by the current role.
- Ticket workers execute only the assigned ticket and must honor the ticket's
  declared `allowed_areas`, `must_not_touch`, `requirements`, and `non_goals`.

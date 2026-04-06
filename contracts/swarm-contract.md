# Swarm Contract

This document defines the portable contract that every skill in this repository follows.
Execution runtimes should treat this document as the interface between roles.

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

## Handoff Rules

- Only the `master` may request approval from the human.
- `worker` roles may hand back to `master` or request validation.
- `validator` roles may hand back to `master` only.
- Validators are blocking by default.
- A `master` may override a validator only after explicit human approval.

## Boundary Rules

- `master` does not implement feature work directly.
- `worker` roles do not self-approve.
- `validator` roles do not implement new features as part of review.
- Cross-domain work should be rerouted instead of silently absorbed by the current role.

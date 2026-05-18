# Ticket Contract

This document defines the canonical contract for Aegis ticket-based execution.
Every ticket is a bounded unit of work that can be assigned, executed, reviewed,
and completed independently.

## Required Ticket Fields

Every ticket must define the following fields:

- `ticket_id`: stable identifier for the ticket.
- `goal`: concrete outcome the assigned role must achieve.
- `dependencies`: tickets, artifacts, approvals, external systems, or conditions required before execution can proceed.
- `allowed_areas`: explicit files, directories, systems, or domains the worker may read or modify for this ticket.
- `must_not_touch`: explicit files, directories, systems, or domains the worker must not modify.
- `requirements`: mandatory implementation, behavior, documentation, or process requirements.
- `non_goals`: work that is intentionally out of scope even if adjacent to the goal.
- `acceptance_criteria`: objective conditions a validator or master can use to decide whether the ticket is complete.
- `manual_verification_required`: boolean indicating whether human or manual verification is required.
- `manual_verification_steps`: ordered manual checks required when `manual_verification_required` is true.
- `verification_commands`: commands workers or validators should run when applicable.
- `completion_report_required`: boolean indicating whether the worker must return a completion report.

Fields may be empty only when emptiness is meaningful and explicit. For example,
`dependencies: []` means the ticket has no known dependencies.

## One-Ticket-Only Execution

- A worker executes exactly one assigned ticket at a time.
- A worker must not pull in requirements from adjacent tickets unless they are listed as dependencies and are necessary to complete the assigned ticket.
- A worker must keep changes inside `allowed_areas`.
- A worker must not modify `must_not_touch` areas, even when doing so would appear to simplify the task.
- A worker must treat `non_goals` as enforceable boundaries, not suggestions.
- A worker must stop and report a boundary issue when the ticket cannot be completed within its declared scope.
- A worker must not stage, commit, push, or open pull requests unless the ticket explicitly requires that action.

## Boundary Behavior

When a task appears to require touching a `must_not_touch` area, the worker must:

1. Pause work on that part of the task.
2. Avoid modifying the restricted area.
3. Report the boundary conflict in `findings`.
4. Return control to `master` with `status: blocked` or `status: needs_clarification`.
5. Describe the smallest scope change or follow-up ticket needed to proceed.

The worker may still complete independent in-scope portions of the ticket if doing
so does not create misleading partial completion or violate acceptance criteria.

## Completion Report

When `completion_report_required` is true, the worker must return a completion
report using the swarm output envelope and include these fields:

- `status`: final ticket state using the swarm contract status values.
- `summary`: concise description of what changed or why the ticket could not be completed.
- `artifacts`: changed files, created files, generated outputs, or relevant references.
- `findings`: blockers, boundary conflicts, skipped verification, risks, or notable follow-up items.
- `next_recommended_role`: recommended next role, usually `validator`, `master`, or `human`.
- `changed_files`: short list of file paths changed by the worker.
- `verification`: commands run, results observed, and manual verification status.

If verification could not be run, the report must say why and identify the
remaining risk.

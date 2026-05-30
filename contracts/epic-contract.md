# Epic Contract

This document defines the canonical contract for AEGIS epic-level planning and
multi-master dispatch. An epic is a bounded set of tickets that may be driven by
a `master-planner` while each dispatched master still executes exactly one ticket
at a time.

## Required Epic Fields

Every epic envelope must define:

- `epic_id`: stable identifier for the epic.
- `goal`: concrete outcome the epic should achieve.
- `branch`: integration branch used for the epic.
- `base`: base branch or ref that the epic eventually merges into.
- `autonomy_policy`: one of `manual`, `checkpointed`, or `autonomous_until_error`.
- `human_checkpoint_tickets`: ticket IDs where planner dispatch must pause for
  human review before continuing.
- `epic_allowed_areas`: files, directories, systems, or domains the epic may
  change across its ticket set.
- `epic_must_not_touch`: files, directories, systems, or domains no ticket in
  the epic may modify.
- `tickets`: ordered ticket IDs owned by the epic.
- `depends_on_epics`: epic IDs, artifacts, approvals, or conditions required
  before this epic can proceed.
- `merge_policy`: strategy, target base, and approval requirements for merging
  the epic branch.

Fields may be empty only when emptiness is meaningful and explicit, such as
`depends_on_epics: []`.

## Workspace Layout

An epic workspace lives under `epics/<epic_id>/` and contains:

- `envelope.yaml`: the epic envelope.
- `ledger.md`: the planner-owned decision and dispatch log.
- `tickets/<ticket_id>.yaml`: one ticket envelope per ticket.
- `checkpoint-summaries/<ticket_id>.yaml`: human checkpoint summary records.

## Autonomy Policy

`autonomy_policy` governs the inter-ticket gate only. It never suppresses
critical-error escalation and never bypasses the merge gate.

Allowed values:

- `manual`: planner pauses for human approval before dispatching every ticket.
- `checkpointed`: planner may continue between tickets, but must pause at every
  ticket listed in `human_checkpoint_tickets`.
- `autonomous_until_error`: planner may continue between tickets until a
  critical error, explicit checkpoint, exhausted retry budget, or merge gate is
  reached.

No other autonomy policy values are valid.

## Critical Errors

The following critical errors always escalate to the human through the
master-planner and are not subject to `autonomy_policy`:

- scope conflict unresolved by worker;
- `must_not_touch` violation at validation;
- validator returns `blocked`;
- merge conflict against `base`;
- unauthorized destructive git action;
- unauthorized secrets action.

## Dispatch Semantics

The master-planner dispatches master-agents with ticket envelopes from the epic
workspace. Each dispatched master remains governed by `contracts/ticket-contract.md`
and the per-master exactly-one-ticket invariant in `contracts/swarm-contract.md`.

Ticket envelopes dispatched by a master-planner must carry
`dispatched_by: master-planner`. When a receiving master sees that field, human
approval requests route back to the master-planner rather than directly to the
human. The planner then decides whether to continue, pause, retry, abort, or ask
the human, according to the epic envelope.

The master-planner owns:

- dispatch sequencing;
- validator-result intake;
- ledger writes;
- checkpoint enforcement;
- critical-error escalation;
- merge-gate preparation;
- final merge request to the human.

## Ledger

The epic ledger is the append-only planner decision log at
`epics/<epic_id>/ledger.md`. It is the human-readable audit trail for dispatch,
validation, checkpoint, human approval, merge, and abort decisions.

Each ledger line must contain:

- `timestamp`: when the planner recorded the event.
- `ticket_id`: ticket ID for ticket-scoped events, or the epic ID for
  epic-scoped events.
- `event_type`: one of the allowed event types below.
- `decision`: planner decision or observed transition.
- `notes`: concise source evidence, validator finding, checkpoint reason, human
  decision, or abort reason.
- `commit_sha`: related commit SHA, or `null` when no commit applies.

Allowed `event_type` values:

- `dispatched`: planner dispatched a master-agent with one ticket envelope.
- `validator_approved`: validator approved ticket output.
- `fixes_required`: validator returned fixes required for the ticket.
- `validator_blocked`: validator returned blocked for the ticket.
- `validator_needs_clarification`: validator returned needs clarification for
  the ticket.
- `checkpoint_hit`: a declared human checkpoint was reached.
- `human_approved`: human approved a checkpoint, retry, continuation, or merge.
- `human_overrode_validator`: human explicitly approved overriding a validator
  finding.
- `epic_merged`: epic branch was merged to base under `merge_policy`.
- `epic_aborted`: planner aborted the epic without merging to base.

## Retry and Escalation

`fixes_required` cycles on the same ticket are capped at five. The retry count is
per ticket and resets when that ticket is approved or escalated.

- For `fixes_required` events 1 through 4, the planner may route remediation
  back through the dispatched master-agent with the validator findings.
- On the fifth `fixes_required` event for the same ticket, the planner must
  escalate to itself with the validator findings and decide whether to ask the
  human, abort the epic, or create a follow-up plan.
- `validator_blocked` and `validator_needs_clarification` bypass the retry
  counter and route immediately to the planner.
- Critical errors bypass planner-only routing and surface to the human through
  the planner escalation envelope.

## Abort

When an epic is aborted:

- the planner writes an `epic_aborted` ledger entry with the abort reason;
- the epic branch is preserved and must not be deleted as part of abort;
- no merge to `base` occurs;
- the planner reports the last completed ticket, current in-flight ticket if
  any, blocking reason, and recommended recovery or follow-up.

## Recovery

Planner recovery uses the ledger as the source of truth. After interruption, the
planner reconstructs in-flight state from the last event in
`epics/<epic_id>/ledger.md`.

The planner must write the ledger entry before acting on a transition. This
ordering ensures recovery sees the intended next state even if the planner is
interrupted during dispatch, retry, checkpoint handling, abort, or merge.

## Merge Policy

The merge gate is always explicit. `merge_policy` must name the strategy, base,
whether an epic validator is required, and whether human approval is required.
Autonomy policy does not bypass the merge gate.

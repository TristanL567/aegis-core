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

## Merge Policy

The merge gate is always explicit. `merge_policy` must name the strategy, base,
whether an epic validator is required, and whether human approval is required.
Autonomy policy does not bypass the merge gate.

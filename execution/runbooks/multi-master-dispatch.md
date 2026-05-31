# Multi-Master Dispatch

This runbook describes the provider-agnostic loop for a `master-planner`
coordinating multiple master-agents across epic workspaces.

Canonical behavior lives in:

- `contracts/epic-contract.md` for epic envelope, ledger, retry, escalation,
  abort, recovery, and merge-gate semantics.
- `contracts/swarm-contract.md` for role envelope, handoff rules, validator
  blocking, and the per-master exactly-one-ticket invariant.

Provider-specific transport is out of scope here.

## Visible Master-Agent Chats

Visible chats correspond to reusable Master-Agents, not internal workers or
validators, unless a provider requires separate visible chats for those roles.
Reuse existing Master-Agent chats when possible so the operator sees stable
execution lanes rather than one chat per internal handoff.

When a Master-Agent assignment changes, rename the visible chat using:

```text
AEGIS Master-Agent | <EPIC-ID>
```

This is provider-agnostic naming guidance only. Do not implement
provider-specific thread or chat renaming in this runbook.

## Master-Agent Assignment Lifecycle

The planner owns project and epic scheduling, assignment dispatch, checkpoint
routing, and final integration. A Master-Agent is a reusable execution lane for
one current epic assignment; it does not own the epic.

Track each Master-Agent assignment through this lifecycle:

`idle -> assigned -> executing -> validating -> committed -> reported -> released`

- `idle`: no active assignment.
- `assigned`: the planner has assigned an epic/ticket packet.
- `executing`: the Master-Agent is carrying out the assigned ticket work.
- `validating`: validator review or validator response routing is in progress.
- `committed`: required assignment commit exists when `commit_required: true`.
- `reported`: the Master-Agent report has been returned to the planner.
- `released`: the planner has released the Master-Agent for reuse.

The planner does not implement worker tasks, validators remain blocking, and the
existing master role behavior inside each dispatched ticket is unchanged.

## Planner State Machine

The planner runs this loop:

`idle -> dispatched -> awaiting validator -> routing -> merging -> idle`

State transitions are written to `epics/<epic_id>/ledger.md` before they take
effect. This keeps recovery deterministic when the planner is interrupted.

- `idle`: no dispatch is in progress for the selected epic.
- `dispatched`: a master-agent has received one ticket envelope.
- `awaiting validator`: the planner waits for the master-agent's validator
  result.
- `routing`: the planner handles approval, fixes, block, clarification,
  checkpoint, retry, escalation, or abort.
- `merging`: the planner executes the merge gate for the epic branch.
- `idle`: the epic is complete, aborted, or ready for the next dispatch.

## Disjointness Check

A new in-flight epic may start only when its `epic_allowed_areas` do not
intersect any live epic's `epic_allowed_areas`.

Live epics are discovered by reading the last event of every
`epics/*/ledger.md`. Any epic whose last event is not `epic_merged` or
`epic_aborted` is live.

If two epics are not disjoint, `depends_on_epics` edges serialize them. The
planner does not dispatch the dependent epic until its dependency reaches
`epic_merged` or `epic_aborted` and the human approves any needed continuation.

## Workspace Configuration

Planner runtime configuration lives at `.aegis/planner-config.yaml` in the
workspace where epics run.

Fields:

- `concurrency_cap`: maximum number of live epics. Default: `2`.
- `per_epic_token_budget`: soft token budget per epic. Default:
  `null` (operator-managed).
- `per_epic_wall_clock_budget`: soft wall-clock budget per epic. Default:
  `null` (operator-managed).

Values are operator-configurable. The planner must treat budgets as dispatch
controls, not as permission to skip validator gates, checkpoints, or merge
policy.

## Dispatch Loop

1. Read `.aegis/planner-config.yaml`, the epic envelope, and the last ledger
   event for each live epic.
2. Apply the disjointness check and concurrency cap.
3. Select the next ready ticket for an eligible epic.
4. Write the ledger transition before dispatch.
5. Dispatch a master-agent with exactly one ticket envelope and
   `dispatched_by: master-planner`.
6. Wait for the master-agent's standard completion and validator result.
7. Write the ledger transition before routing the result.
8. Route according to `contracts/epic-contract.md`.

## Validator Return-Route Interception

Master validators return the standard envelope with
`next_recommended_role: master`. No validator `allowed_handoffs` edits are
required.

The planner intercepts that standard envelope at the master-agent boundary,
reads the validator status and findings, writes the ledger event, and routes the
epic forward:

- approved output may continue to the next ticket or checkpoint;
- `fixes_required` follows the retry budget;
- `blocked` and `needs_clarification` route immediately to the planner;
- critical errors surface to the human through the planner escalation envelope.

## Checkpoint Handling

When a ticket listed in `human_checkpoint_tickets` is reached, the planner:

1. writes a `checkpoint_hit` ledger event;
2. creates or updates the checkpoint summary for that ticket;
3. hands the checkpoint summary to the human;
4. waits for `human_approved` or another explicit human decision before
   continuing.

## Retry And Escalation

Retry and escalation follow `contracts/epic-contract.md`.

In summary, `fixes_required` cycles on the same ticket cap at five. The fifth
failure escalates to the planner with validator findings. `blocked` and
`needs_clarification` bypass retry and route to the planner immediately.
Critical errors surface to the human through the planner escalation envelope.

## Planner Recovery

On resume, the planner:

1. scans every `epics/*/ledger.md`;
2. reads the last event from each ledger;
3. treats any epic whose last event is not `epic_merged` or `epic_aborted` as
   in-flight;
4. reconstructs each in-flight epic state from the last event;
5. resumes from the next safe state transition, writing the next ledger event
   before acting.

## Merge Gate

At the merge gate, the planner:

1. writes the transition to `merging`;
2. rebases the epic branch onto `base`;
3. runs declared verification commands for the epic and final ticket state;
4. checks `merge_policy`;
5. pauses for human approval when `merge_policy.requires_human_approval` is
   `true`;
6. merges only after `merge_policy` is satisfied;
7. writes `epic_merged` after merge completion.

If rebase or merge conflicts occur, the conflict is a critical error and routes
to the human through the planner.

## Worked Example

Two epics can run in parallel when their allowed areas are disjoint:

```yaml
epic_id: AEGIS-DOCS-CLEANUP
epic_allowed_areas:
  - docs/
```

```yaml
epic_id: AEGIS-BACKEND-ENDPOINTS
epic_allowed_areas:
  - services/api/
  - tests/api/
```

These epics are disjoint because `docs/` does not intersect `services/api/` or
`tests/api/`. If a third epic declares `epic_allowed_areas: [services/]`, it
must not run concurrently with `AEGIS-BACKEND-ENDPOINTS`; the planner must add or
honor a `depends_on_epics` edge to serialize them.

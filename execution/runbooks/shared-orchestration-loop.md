# Shared Orchestration Loop

This runbook describes the common AEGIS execution loop for this repository. It is operator guidance only: canonical role behavior remains in `skills/`, and canonical handoff and ticket rules remain in `contracts/`.

## Loop

1. Load the relevant canonical skill from `skills/`.
2. Start with the `master`.
3. Dispatch the scoped task to the appropriate `worker`.
4. Send completed worker output to the appropriate `validator`.
5. Return validator findings or approval to the `master`.
6. Ask the human for approval only through the `master`.
7. Repeat until the ticket reaches a true completion checkpoint.

The loop is always `master -> worker -> validator -> master`. Operators and automation may adapt the transport for a provider, but the routing shape stays the same.

## Runtime Responsibilities

Execution runtime state should stay outside the canonical role definitions. During a ticket, the operator or automation layer is responsible for:

- discovering and loading current skill bodies from `skills/`;
- applying the relevant contracts from `contracts/`;
- keeping ticket state, artifacts, and changed-file references visible across handoffs;
- preserving transcripts or concise summaries needed for audit and later review;
- enforcing validator gating before work advances;
- making every next handoff explicit through the standard output envelope.

Reusable prompt or report shapes may live in `execution/templates/` as this execution area matures. Those templates should support the loop without redefining skills or contracts.

## Gate Policy

Validators are blocking by default. A worker never self-approves, and completed worker output does not advance until the appropriate validator returns an approving result.

If a validator returns `fixes_required`, route the findings back through the loop for remediation. The master may only override a validator after explicit human approval, and that approval should be recorded in the carried-forward ticket context.

## Boundaries

Each handoff must preserve the ticket objective, allowed areas, acceptance criteria, verification expectations, and relevant branch or dependency context. If the next required action would exceed the ticket boundary, return control to the `master` with the boundary conflict instead of expanding scope.

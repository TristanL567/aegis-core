# AEGIS Kernel

The kernel is the short, citable list of AEGIS non-negotiables. It restates
rules owned by the canonical contracts; the cited contract text remains
authoritative.

1. Start implementation only after a ticket envelope exists with goal,
   dependencies, `allowed_areas`, `must_not_touch`, acceptance criteria, and
   verification commands. Owner: `contracts/ticket-contract.md` Required Ticket
   Fields.
2. Execute exactly one ticket at a time; do not pull in adjacent-ticket work.
   Owner: `contracts/ticket-contract.md` One-Ticket-Only Execution.
3. Keep changed files inside `allowed_areas` and never modify `must_not_touch`.
   Owner: `contracts/ticket-contract.md` One-Ticket-Only Execution and Boundary
   Behavior.
4. Preserve the `master -> worker -> validator -> master` loop. Owner:
   `contracts/swarm-contract.md` Handoff Rules.
5. Treat validators as blocking; only the human may authorize a validator
   override requested by the master. Owner: `contracts/swarm-contract.md`
   Handoff Rules.
6. Return the standard role envelope on every role output: `status`, `summary`,
   `artifacts`, `findings`, and `next_recommended_role`. Owner:
   `contracts/swarm-contract.md` Output Envelope.
7. Return the full completion report for completed tickets. Owner:
   `contracts/ticket-contract.md` Completion Report.
8. Commit only against an active ticket, and use `[TICKET-ID] concise
   description` with a description of 72 characters or fewer. Owner:
   `contracts/ticket-contract.md` Master-Agent Assignment Commits.
9. Supervisors do not implement feature work directly. Owner:
   `contracts/swarm-contract.md` Boundary Rules; expanded supervisor locks are
   promoted by AEGIS-OVH-003.
10. When intent, dependencies, or boundaries are unclear, block for
    clarification before implementation. Owner: `contracts/ticket-contract.md`
    Boundary Behavior and `contracts/epic-contract.md` Critical Errors.

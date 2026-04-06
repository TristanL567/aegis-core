# Role Model

This library uses a strict three-role swarm model.

## Master

The master is the coordinator.

- Owns decomposition, sequencing, and handoffs.
- Talks to the human.
- Requests approvals.
- Decides whether work should loop back to a worker or move to validation.
- May override a validator only with explicit human approval.

## Workers

Workers are specialized executors.

- Implement or analyze within a narrow domain.
- Produce artifacts and a structured result.
- Respect declared boundaries.
- Hand off to the validator or back to the master.

## Validators

Validators are independent reviewers.

- Inspect output from workers.
- Return findings and a verdict.
- Block completion by default when issues are found.
- Route back to the master rather than directly controlling workers.

## Why This Split Exists

- It keeps human approvals in one place.
- It prevents workers from self-certifying.
- It makes providers with different execution models easier to support.
- It lets the execution runtime remain thin because the library itself encodes the role rules.

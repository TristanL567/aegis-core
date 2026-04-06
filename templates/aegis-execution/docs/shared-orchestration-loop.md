# Shared Orchestration Loop

All providers should follow the same high-level swarm pattern.

## Loop

1. Load the canonical library from the skill repo.
2. Start with the `master`.
3. Dispatch the scoped task to the appropriate `worker`.
4. Send completed worker output to the appropriate `validator`.
5. Return validator findings or approval to the `master`.
6. Ask the human for approval only through the `master`.
7. Repeat until the task reaches a true completion checkpoint.

## Runtime Responsibilities

- discover canonical skills
- keep task state and artifact references
- preserve transcripts or summaries
- enforce validator gating
- make the next handoff explicit

## Gate Policy

- Validators are blocking by default.
- The master may only override a validator after explicit human approval.
- Workers never self-approve.

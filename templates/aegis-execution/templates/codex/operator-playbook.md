# Codex Operator Playbook

Use this playbook in the execution repo to run the swarm manually or semi-manually.

## Session Start

- Load the canonical `master` skill from the library repo.
- Provide the task envelope.
- Ask the master to decide the next role.

## Worker Dispatch

- Load the chosen worker skill from the library repo.
- Include the task envelope and any prior artifacts.
- Require the standard output contract.

## Validation

- Load the right validator skill from the library repo.
- Provide the worker result and relevant artifacts.
- Require a blocking verdict when issues exist.

## Return to Master

- Give the validator result to the master.
- Let the master decide whether to request fixes, advance, or ask the human for approval.

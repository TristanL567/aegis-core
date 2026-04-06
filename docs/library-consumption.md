# Consuming This Library

External runtimes should treat this repository as a canonical prompt and contract library.

## Consumption Pattern

1. Discover skills under `skills/*/SKILL.md`.
2. Read the YAML frontmatter to identify the role and handoff rules.
3. Select the `master` skill for the initial task.
4. Route work to `worker` skills based on domain fit.
5. Route worker output through a `validator`.
6. Return the validator result to the `master`.
7. Ask the human for approval only through the `master`.

## Canonical vs Derived

Canonical content in this repo:

- role prompts,
- handoff contract,
- validator policy,
- provider adapter notes.

Derived content in an execution runtime:

- orchestration scripts,
- provider-specific wrappers,
- operator playbooks,
- state tracking,
- artifact persistence.

## Runtime Expectations

An execution runtime should provide:

- task state,
- artifact storage or references,
- provider-specific agent invocation,
- human approval handling,
- logging or transcript capture,
- retry and remediation loops.

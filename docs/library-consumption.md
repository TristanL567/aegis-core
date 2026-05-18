# Consuming This Library

External runtimes should treat this repository as the canonical Aegis framework
source for prompts, contracts, documentation, execution guidance, and validation
tools.

## Consumption Pattern

1. Discover skills under `skills/*/SKILL.md`.
2. Read the YAML frontmatter to identify the role and handoff rules.
3. Select the `master` skill for the initial task.
4. Route work to `worker` skills based on domain fit.
5. Route worker output through a `validator`.
6. Return the validator result to the `master`.
7. Ask the human for approval only through the `master`.

## Canonical vs Local Runtime

Canonical content in this repo:

- role prompts,
- handoff contract,
- validator policy,
- provider adapter notes,
- provider-agnostic execution and operator guidance,
- validation and maintenance tools.

Local or provider-specific runtime content can still be derived outside the
canonical framework when needed:

- orchestration scripts,
- provider-specific wrappers,
- operator playbooks,
- state tracking,
- artifact persistence.

Execution guidance should be documented in this repo under a planned dedicated
in-repo execution area. The existing `templates/aegis-execution/` scaffold
remains in place for now; this document does not imply files have moved or that a
separate execution repository is required.

## Runtime Expectations

An execution runtime should provide:

- task state,
- artifact storage or references,
- provider-specific agent invocation,
- human approval handling,
- logging or transcript capture,
- retry and remediation loops.

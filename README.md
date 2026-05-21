# Aegis Core Skill Library

This repository is the canonical source of truth for the Aegis swarm framework.
It stores provider-agnostic skills, shared contracts, framework docs, execution
guidance, and validation tools in one place.

## Consumer Entry

External consumers should start with `AEGIS.md` as the canonical entry point.
The instruction `reference AEGIS-CORE` means loading `AEGIS.md` first, following
its bootstrap order, and passing its Conformance Gate before completion.

## Core Model

- `master` coordinates work, talks to the human, and owns approvals.
- `worker` roles execute scoped tasks and produce artifacts.
- `validator` roles review worker output and block completion by default.

The library is authored in `Markdown + YAML frontmatter` so it can be adapted into
Codex, Claude Code, and Antigravity without changing the core prompt text.

## Repository Layout

- `skills/`: canonical skill definitions, split into stable layers.
- `skills/roles/`: canonical role prompt definitions, one role per folder.
- `skills/discipline/`: reserved for future discipline-layer skills.
- `skills/procedures/`: reserved for future procedural skills.
- `contracts/`: shared handoff and output contract for all skills.
- `docs/`: framework-level guidance for roles, gating, adapters, tests, and execution.
- `execution/`: dedicated guidance, prompts, and templates for operating the swarm across providers.
- `tools/`: validation utilities for discovery and frontmatter checks.

## Canonical Contract

Every skill must expose the following frontmatter fields:

- `name`
- `role`
- `description`
- `inputs_expected`
- `outputs_produced`
- `allowed_handoffs`
- `blocking_rules`
- `provider_notes`

Every skill response must produce the same output envelope:

- `status`
- `summary`
- `artifacts`
- `findings`
- `next_recommended_role`

Allowed statuses are:

- `completed`
- `needs_clarification`
- `blocked`
- `fixes_required`

## Validator Policy

Validators are blocking by default. A master can only override a validator finding when
the human explicitly approves the override.

## Execution Guidance

This repo owns canonical execution guidance as part of the framework. Runtime
implementation can still be provider-specific, but the operator guidance,
orchestration expectations, and execution documentation should live in this repo
under `execution/`.

The `execution/` area owns provider-agnostic runbooks, launch prompts, ticket
templates, clean-commit guidance, and apply-to-project guidance. The internal
boundary remains split across `contracts/`, `skills/roles/`,
`skills/discipline/`, `skills/procedures/`, `docs/`, `execution/`, and `tools/`.

## Validation

Run the library validator from the repository root:

```powershell
py -3.10 .\tools\validate_skill_library.py
```

The validator enumerates role skills under `skills/roles/`, checks the required
frontmatter, and verifies the basic role and handoff contract.

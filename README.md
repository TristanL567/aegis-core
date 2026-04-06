# Aegis Core Skill Library

This repository is the canonical source of truth for a portable swarm skill library.
It stores provider-agnostic role prompts, shared contracts, and adapter notes that can
be consumed by an external execution runtime.

## Core Model

- `master` coordinates work, talks to the human, and owns approvals.
- `worker` roles execute scoped tasks and produce artifacts.
- `validator` roles review worker output and block completion by default.

The library is authored in `Markdown + YAML frontmatter` so it can be adapted into
Codex, Claude Code, and Antigravity without changing the core prompt text.

## Repository Layout

- `skills/`: canonical skill definitions, one skill per folder.
- `contracts/`: shared handoff and output contract for all skills.
- `docs/`: library-level guidance for roles, gating, adapters, and tests.
- `templates/aegis-execution/`: scaffold for the separate execution/docs repo.
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

## Separate Execution Repo

This repo intentionally does not implement a runtime. Use the scaffold in
`templates/aegis-execution/` as the starting point for a second repository that:

- documents the orchestration loop,
- explains how to execute the swarm in each provider,
- and contains starter templates/configuration for Codex, Claude Code, and Antigravity.

## Validation

Run the library validator from the repository root:

```powershell
py -3.10 .\tools\validate_skill_library.py
```

The validator enumerates all skills, checks the required frontmatter, and verifies the
basic role and handoff contract.

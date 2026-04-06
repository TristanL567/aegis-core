# Aegis Execution Repo Template

This directory is a scaffold for the second repository that documents and operates the
swarm execution layer.

## Purpose

The execution repo is intentionally separate from the canonical skill library.

It should contain:

- orchestration docs,
- provider-specific operator instructions,
- starter templates and configuration,
- and lightweight runtime wrappers if you add them later.

It should not become the long-term source of truth for skill prompts.

## Suggested Workflow

1. Create a new repository for the execution layer.
2. Copy the contents of this directory into that repository.
3. Replace placeholder paths so the execution repo points back to the canonical skill library.
4. Add provider-specific local setup details as you learn them.

## Included Files

- `docs/setup-second-agent.md`
- `docs/shared-orchestration-loop.md`
- `docs/providers/codex.md`
- `docs/providers/claude-code.md`
- `docs/providers/antigravity.md`
- `templates/shared/`
- `templates/codex/`
- `templates/claude-code/`
- `templates/antigravity/`

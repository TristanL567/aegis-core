# Execution

This directory contains in-repo execution guidance used by operators and automation workers.

It contains launch prompts, ticket workflows, runbooks, clean commit guidance, reusable execution templates, and apply-to-project material. Content here helps someone carry out work using AEGIS conventions without redefining the canonical roles themselves.

Canonical role behavior remains in `skills/`, and canonical ticket and swarm rules remain in `contracts/`. The `execution/` area may reference those sources, but it should not replace them or become the source of truth for skill behavior or contracts.

## Areas

- `prompts/`: operator prompts and launch prompts for master startup, ticket execution, validation, completion reporting, clean commit preparation, apply-to-project work, and provider setup.
- `runbooks/`: repeatable execution procedures for shared orchestration, provider-specific operation, clean commits, and applying AEGIS to another project.
- `templates/`: reusable ticket envelope and completion report examples for execution workflows.

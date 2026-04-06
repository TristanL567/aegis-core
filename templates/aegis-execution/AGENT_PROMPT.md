# Aegis Execution Agent Prompt

You are working in the `aegis-execution` repository.

This repository is the execution-facing layer for the Aegis swarm. It is not the
canonical source of truth for skill behavior.

## Mission

Your job is to document, adapt, and operationalize the swarm for concrete execution
environments such as Codex, Claude Code, and Antigravity.

## This Repo Owns

- provider-specific setup instructions
- operator playbooks
- derived agent files
- execution templates
- optional lightweight wrappers or helper scripts

## Canonical Dependency

The canonical skill library lives in `aegis-core`.

Treat `aegis-core` as the source of truth for:

- role definitions
- shared contracts
- validator policy
- provider-agnostic prompt wording

## Non-Negotiable Rules

- Keep the orchestration loop as `master -> worker -> validator -> master`.
- Validators are blocking by default.
- Only the `master` requests approval from the human.
- Do not silently fork role behavior away from `aegis-core`.
- If a provider needs special handling, document it clearly in this repo.
- If you discover a needed canonical change, note it explicitly instead of changing the derived copy casually.

## How to Work Here

1. Read the execution repo README and provider docs first.
2. Confirm which files are derived from `aegis-core` and keep that distinction explicit.
3. Improve provider onboarding, operator steps, and execution templates.
4. Replace placeholder paths with real local paths when requested.
5. Keep execution guidance practical and easy to follow.

## When You Should Edit This Repo

Edit `aegis-execution` when the task changes:

- provider runbooks
- Codex workflows
- Claude Code derived agent files
- Antigravity session templates
- execution setup documentation
- helper scripts or wrappers that do not redefine canonical skill logic

## When You Should Send Work Back to Aegis Core

Route the change back to `aegis-core` if it affects:

- a skill's canonical frontmatter
- shared contract fields
- validator rules
- role boundaries
- canonical prompt text

## Reporting Style

When you finish, report:

- what execution-facing behavior changed
- which provider docs or templates changed
- whether `aegis-core` also needs an upstream canonical update

# Setup Guide for the Second Agent

Use this guide when you want a second agent to own the execution repo while this skill
library remains the canonical source of truth.

## Goal

The second agent should work in the execution repo only.

Its job is to:

- document how to run the swarm,
- adapt the canonical skills to each provider,
- add provider-specific templates and wrappers,
- and avoid rewriting the core prompts from the library repo.

## Before You Start

Make sure you have:

1. this library repo available locally,
2. a new second repository created for execution docs and templates,
3. the contents of `templates/aegis-execution/` copied into that second repo,
4. a known filesystem path to this library repo.

## Folder Ownership

Split ownership clearly:

- library repo: canonical prompts, contracts, role model, validator policy
- execution repo: provider runbooks, derived agent files, starter templates, optional wrappers

The second agent should not change the canonical prompts unless you explicitly send it
back to this repo.

## What to Tell the Second Agent

Give the second agent:

- the path to the execution repo,
- the path to this skill library repo,
- the rule that the library repo is canonical,
- the rule that validators are blocking by default,
- the orchestration loop: `master -> worker -> validator -> master`,
- and the requirement that only the `master` asks the human for approval.

## Recommended Bootstrap Prompt

Use a prompt like this when starting the second agent:

```text
You are working in the swarm execution repository.

Canonical skill library path:
[INSERT ABSOLUTE PATH TO THIS REPO]

Execution repo goal:
Build the execution-facing documentation, provider adapters, and starter templates for
running the swarm in Codex, Claude Code, and Antigravity.

Non-negotiable rules:
- The canonical prompts and contracts live in the skill library repo, not here.
- This repo may contain derived agent files, provider wrappers, and operator docs.
- Keep the orchestration loop as: master -> worker -> validator -> master.
- Validators are blocking by default.
- Only the master asks the human for approval.
- If a provider needs special handling, document it here without mutating the canonical prompt text.

Start by reviewing:
- README.md
- docs/shared-orchestration-loop.md
- docs/providers/
- templates/

Then:
1. Replace placeholder paths with the actual library repo path.
2. Tighten the provider-specific setup instructions.
3. Add any missing derived files needed for Codex, Claude Code, and Antigravity.
4. Keep a clear distinction between canonical and derived content.
```

## Recommended First Tasks for the Second Agent

Ask it to complete these in order:

1. Update all placeholder references so the execution repo points to the real library repo path.
2. Improve the Codex execution docs for your local workflow.
3. Flesh out the Claude Code `.claude/agents` derived files.
4. Expand the Antigravity runbook and session templates.
5. Add a short "how to run a first end-to-end swarm task" walkthrough.

## Guardrails

Tell the second agent:

- do not copy canonical prompts into multiple provider files unless the file is explicitly derived,
- do not fork role behavior across providers without documenting why,
- do not let workers self-approve,
- do not move validator policy into an advisory-only model,
- do not treat the execution repo as the source of truth for skill logic.

## Suggested Human Workflow

1. Create the second repo.
2. Copy `templates/aegis-execution/` into it.
3. Start a second agent in that repo with the bootstrap prompt above.
4. Let it improve execution docs and provider adapters.
5. Bring any canonical prompt changes back to this library repo separately.

## When to Send Work Back to This Repo

Route work back to the library repo if the second agent discovers that you need to change:

- role definitions,
- canonical handoff rules,
- shared contract fields,
- validator policy,
- or the provider-agnostic prompt text of a skill.

# Aegis Core Agent Prompt

You are working in the `aegis-core` repository.

This repository is the canonical source of truth for the Aegis swarm.

## Mission

Your job is to maintain and improve the provider-agnostic skill library, shared
contracts, and swarm role definitions.

## This Repo Owns

- canonical skill prompts in `skills/`
- shared contracts in `contracts/`
- library documentation in `docs/`
- shared prompt templates in `prompt_templates/`
- the execution repo scaffold in `templates/aegis-execution/`

## Non-Negotiable Rules

- Treat this repo as canonical for role behavior.
- Keep the swarm model as `master`, `worker`, and `validator`.
- Keep the orchestration loop as `master -> worker -> validator -> master`.
- Validators are blocking by default.
- Only the `master` requests approval from the human.
- Do not add provider-specific drift into the canonical prompts unless a limitation truly requires it.
- If a provider needs special behavior, prefer adapter notes and execution docs over mutating core role logic.

## What Belongs Somewhere Else

The separate `aegis-execution` repo should own:

- provider-specific runbooks
- derived agent files
- local operator workflows
- wrapper scripts or runtime glue

Do not move those concerns into this repo unless the user explicitly asks for it.

## How to Work Here

1. Inspect the relevant skill, contract, or library docs first.
2. Change canonical behavior only when the change should apply across providers.
3. Preserve clear frontmatter and output-envelope consistency across all skills.
4. Keep documentation aligned with the actual skill contract.
5. If a requested change is execution-specific, point it back to `aegis-execution`.

## When You Should Edit This Repo

Edit `aegis-core` when the task changes:

- a canonical role definition
- shared contract fields
- validator policy
- provider-agnostic prompt wording
- library structure or documentation

## Standard Check Before Finishing

- confirm all affected skills still expose the required frontmatter
- confirm the role/handoff model still makes sense
- run the library validator when relevant:

```powershell
py -3.10 .\tools\validate_skill_library.py
```

## Reporting Style

When you finish, report:

- what canonical behavior changed
- what files changed
- whether `aegis-execution` should also be updated

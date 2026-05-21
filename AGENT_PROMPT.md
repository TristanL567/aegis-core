# Aegis Core Agent Prompt

You are working in the `aegis-core` repository.

This repository is the canonical source of truth for the Aegis swarm.

For external consumers, `AEGIS.md` is the canonical entry point. The instruction
`reference AEGIS-CORE` means loading `AEGIS.md` first and following its
bootstrap, ticketing, orchestration, and Conformance Gate requirements. This
does not change the internal repo-editing behavior below.

## Mission

Your job is to maintain and improve the provider-agnostic skill library, shared
contracts, swarm role definitions, framework documentation, execution guidance,
and validation tooling.

## This Repo Owns

- canonical skill prompts in `skills/`
- canonical role prompts in `skills/roles/`
- canonical operating discipline in `skills/discipline/`
- future procedural skills in `skills/procedures/`
- shared contracts in `contracts/`
- framework documentation in `docs/`
- canonical execution guidance in `execution/`
- shared prompt templates in `prompt_templates/`
- validation and maintenance tools in `tools/`

## Non-Negotiable Rules

- Treat this repo as canonical for role behavior.
- Follow `skills/discipline/operating-discipline.md` as the canonical always-on operating discipline.
- Keep the swarm model as `master`, `worker`, and `validator`.
- Keep the orchestration loop as `master -> worker -> validator -> master`.
- Validators are blocking by default.
- Only the `master` requests approval from the human.
- Do not add provider-specific drift into the canonical prompts unless a limitation truly requires it.
- If a provider needs special behavior, prefer adapter notes and execution docs over mutating core role logic.

## Internal Boundary

Keep the repository boundary clear:

- `skills/` owns the stable top-level skill library path.
- `skills/roles/` owns canonical role prompts.
- `skills/discipline/` owns canonical always-on operating discipline.
- `skills/procedures/` is reserved for future procedural skills.
- `contracts/` owns shared handoff and output contracts.
- `docs/` owns framework-level guidance.
- `execution/` owns provider-agnostic operator and execution guidance.
- `tools/` owns validation and maintenance utilities.

Provider-specific runtime implementation, generated local agent files, and local
deployment glue can remain outside the canonical framework when needed.

## How to Work Here

1. Inspect the relevant skill, contract, or library docs first.
2. Apply `skills/discipline/operating-discipline.md` to keep work scoped, surgical, verified, and human-readable.
3. Change canonical behavior only when the change should apply across providers.
4. Preserve clear frontmatter and output-envelope consistency across all skills.
5. Keep documentation aligned with the actual skill contract.
6. If a requested change is execution-specific, keep provider-agnostic guidance in this repo and avoid adding provider-specific drift to canonical prompts.

## When You Should Edit This Repo

Edit `aegis-core` when the task changes:

- a canonical role definition
- shared contract fields
- validator policy
- provider-agnostic prompt wording
- framework structure or documentation
- provider-agnostic execution guidance

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
- whether follow-up execution-area work is needed

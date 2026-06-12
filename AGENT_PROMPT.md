# AEGIS-CORE Agent Prompt

You are using the `aegis-core` repository as a canonical framework reference
for work in another project.

This prompt is about how to use AEGIS-CORE content. It is not an instruction to
edit AEGIS-CORE itself.

## Entry Rule

Load `AEGIS.md` first. The instruction `reference AEGIS-CORE` means following
the bootstrap order, conformance contract, and Conformance Gate defined there.

Use `prompts/README.md` when the human asks how to operate this repo, choose a
workflow mode, or find a copy/paste-ready prompt. Use
`prompts/01-init/use-aegis-core.md` when you need the canonical binding prompt
for applying AEGIS-CORE to another project.

## How To Use This Repo

1. Start from `AEGIS.md`.
2. Load the files in its Bootstrap Load Order.
3. Use `contracts/` for the ticket, handoff, validator, override, and completion
   report contract.
4. Use `skills/roles/master/SKILL.md` as the entry role for AEGIS-scoped work.
5. Select worker and validator role prompts from `skills/roles/` by ticket type.
6. Consult `skills/procedures/` and `skills/references/` when a selected role or
   ticket calls for procedural or reference knowledge.
7. Use `execution/runbooks/` for provider-agnostic operating guidance and
   `prompts/` for human-facing prompt routing.
8. Apply the selected AEGIS-CORE content to the target project, not to this repo.

## Optional Context And Evidence

AEGIS-CORE can use optional external context tools when a ticket genuinely needs
system-wide understanding. These tools are advisory only.

- Use `docs/cross-references/` to understand which external tools, repos, or
  ideas have influenced AEGIS.
- Use `execution/runbooks/understand-anything.md` and
  `skills/procedures/codebase-map-generation/SKILL.md` when Understand Anything
  or comparable graph evidence is available and useful.
- Treat graph evidence, generated summaries, and dashboards as context evidence,
  not authority. Confirm claims against source files before relying on them.
- Do not create, run, or commit generated graph artifacts unless the current
  ticket explicitly allows that work.

## Required Operating Contract

- Use ticketing before implementation.
- Execute exactly one ticket at a time.
- Preserve the `master -> worker -> validator -> master` loop.
- Treat validators as blocking by default.
- Only the master requests human approval, and only the human authorizes a
  validator override.
- Keep changed files inside the target ticket's `allowed_areas`.
- Do not modify target ticket `must_not_touch` paths.
- Return the standard role envelope for role outputs.
- Return the full ticket completion report for completed tickets.
- Pass the `AEGIS.md` Conformance Gate before reporting completion.

## Project Boundary

When applying AEGIS-CORE to another project:

- Do not edit AEGIS-CORE files unless the user explicitly asks to change the
  framework itself.
- Do not copy full role, contract, or procedure bodies into the target project
  unless the user explicitly asks for a local fork.
- Treat AEGIS-CORE as the source of canonical behavior and cite paths to the
  loaded files when useful.
- Keep provider-specific runtime glue in the target project or runtime layer,
  not in AEGIS-CORE.

## First Response Shape

When a user asks you to apply AEGIS-CORE to a project, return:

- whether the project context is sufficient to define the first ticket;
- the first ticket envelope, or the missing context that blocks it;
- the selected worker and validator role paths for that ticket;
- the validation commands or evidence required before completion.

## Important Caveats

- AEGIS is not a "spec to code" compiler. It is an operating framework for
  scoped, validated work.
- AEGIS-CORE remains the source of behavior. Target projects may hold local
  conventions, but they should not silently fork role, contract, or validator
  semantics.
- Broad discovery, codebase maps, and graph tools must not expand a ticket
  beyond `allowed_areas`.
- When business intent, user outcome, design concept, or architecture boundary
  is unclear, block for clarification before implementation.

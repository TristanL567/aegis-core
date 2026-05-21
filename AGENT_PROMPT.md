# AEGIS-CORE Agent Prompt

You are using the `aegis-core` repository as a canonical framework reference
for work in another project.

This prompt is about how to use AEGIS-CORE content. It is not an instruction to
edit AEGIS-CORE itself.

## Entry Rule

Load `AEGIS.md` first. The instruction `reference AEGIS-CORE` means following
the bootstrap order, conformance contract, and Conformance Gate defined there.

Use `execution/prompts/use-aegis-core.md` when you need a copy/paste-ready
operator prompt for applying AEGIS-CORE to another project.

## How To Use This Repo

1. Start from `AEGIS.md`.
2. Load the files in its Bootstrap Load Order.
3. Use `contracts/` for the ticket, handoff, validator, override, and completion
   report contract.
4. Use `skills/roles/master/SKILL.md` as the entry role for AEGIS-scoped work.
5. Select worker and validator role prompts from `skills/roles/` by ticket type.
6. Consult `skills/procedures/` and `skills/references/` when a selected role or
   ticket calls for procedural or reference knowledge.
7. Use `execution/runbooks/` and `execution/prompts/` for provider-agnostic
   operating guidance.
8. Apply the selected AEGIS-CORE content to the target project, not to this repo.

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

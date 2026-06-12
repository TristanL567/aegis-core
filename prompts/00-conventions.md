# Prompt Conventions

Every human-facing prompt under `prompts/` uses the same anatomy. Prompts route
work and cite canonical behavior; they do not define role behavior, contract
behavior, validation semantics, or completion-report semantics.

## Frontmatter

Each prompt, except `README.md` and this file, starts with YAML frontmatter:

```yaml
---
id: short-stable-id
stage: init | plan | execute | validate | finish | control | providers
mode: relay | checkpointed | autonomous | any
audience: human
target_role: skills/roles/<role>/ | none
pairs_with:
  - prompts/<stage>/<file>.md
requires:
  - AEGIS.md
  - contracts/kernel.md
returns:
  - standard role envelope
---
```

`target_role` must resolve to an existing role under `skills/roles/` or be
`none`. `pairs_with` entries must resolve to prompt files or be explicitly
marked pending in `prompts/README.md` while migration tickets are open.

## Mandatory Sections

Every prompt file must contain these sections in this order:

1. `## When to use`
2. `## Preconditions`
3. `## Prompt`
4. `## Expected response`
5. `## Next step`

The `## Prompt` section contains one fenced `text` code block. Put the
copy/paste prompt inside that code block. Do not put multiple unrelated prompt
bodies in one file.

## Placeholder Syntax

Use bracketed placeholders for operator-provided values:

```text
[EPIC_ID]
[TICKET_ID]
[ROLE_PATH]
[VALIDATOR_FINDING_ID]
```

Use uppercase words with underscores. Do not invent provider-specific
placeholder syntax inside core prompts.

## Inline Kernel Block

Dispatch and execution prompts that carry ticket context must include this block
inside the prompt text:

```text
TICKET: [TICKET_ID]
GOAL: [GOAL]
DEPENDS_ON: [DEPENDS_ON]
ALLOWED_AREAS: [ALLOWED_AREAS]
MUST_NOT_TOUCH: [MUST_NOT_TOUCH]
ACCEPTANCE: [ACCEPTANCE]
VERIFY: [VERIFY]
```

The block is populated from the ticket envelope. It does not replace the
envelope or canonical contracts.

## Next Step Tables

Every prompt ends with a table that routes by returned `status` and
`next_recommended_role`. Each destination must be another file under
`prompts/`, `human`, or `stop`.

## Behavior Rules

- Prompts invoke roles and cite `contracts/`; they never define role behavior.
- The canonical invocation lives in exactly one prompt file:
  `prompts/01-init/use-aegis-core.md`.
- `prompts/README.md` may quote the canonical invocation once and must mark
  `prompts/01-init/use-aegis-core.md` as the canonical source.
- Planner-generated relay prompts must themselves conform to this template.
- Provider prompts may describe runtime mapping, but core behavior remains in
  `AEGIS.md`, `contracts/`, and `skills/roles/`.

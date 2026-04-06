# Provider Adapter Notes

The core prompts in this repository are provider-agnostic. Provider-specific behavior
should be derived from the `provider_notes` block in each skill frontmatter.

## Codex

- Prefer spawning specialized agents from the master when true parallel work helps.
- Treat the skill file as the canonical prompt and wrap it with runtime-specific context.
- Enforce validator gates in the operator or runner layer, not inside worker prompts alone.

## Claude Code

- Map each canonical skill into a `.claude/agents/<name>.md` file.
- Preserve the role and handoff contract in the frontmatter or surrounding adapter docs.
- Keep the library repo canonical and generate or copy derived agent files into the execution repo.

## Antigravity

- Use the skill prompt as the core instruction set and pair it with provider-specific session templates.
- Keep orchestration guidance explicit because adapter conventions may be more workflow-oriented than file-oriented.
- Favor adapter docs and templates over assuming a rigid agent-file schema.

## Adapter Discipline

- Do not fork the canonical prompt text per provider unless a provider-specific limitation requires it.
- Document any provider-specific deviation near the adapter, not by mutating the canonical skill.
- Validate at least one sample skill mapping across all providers before introducing new contract fields.

---
id: claude-code-setup
stage: providers
mode: any
audience: human
target_role: none
pairs_with:
  - prompts/01-init/apply-to-project.md
  - prompts/07-providers/custom-instructions.md
requires:
  - contracts/kernel.md
  - skills/roles/master/SKILL.md
returns:
  - provider setup instructions
  - standard role envelope
---

# Claude Code Setup

## When to use

Use this prompt to map AEGIS roles onto Claude Code local agents in a target
project.

## Preconditions

- The target project path is known.
- The AEGIS-CORE path is known.
- The operator wants provider-local stubs, not changes to AEGIS-CORE.

## Prompt

```text
Prepare Claude Code provider-local setup for AEGIS.

Canonical AEGIS-CORE root:
[AEGIS_CORE_ROOT]

Target project root:
[TARGET_PROJECT_ROOT]

Use canonical behavior from:
- AEGIS.md
- contracts/kernel.md
- contracts/swarm-contract.md
- contracts/ticket-contract.md
- contracts/epic-contract.md
- skills/roles/master/SKILL.md
- selected worker role under skills/roles/
- selected validator role under skills/roles/
- skills/roles/master-validator/SKILL.md when epic validation is used

Provider mapping:
- Claude Code local agent stubs may live under [TARGET_PROJECT_ROOT]/.claude/agents/.
- Stubs must cite AEGIS-CORE files instead of copying full role or contract
  bodies.
- Visible master-agent chats are preferred for epic assignments.
- Internal helper agents must not replace visible master-agent execution lanes.

Return the local files to create or update, the role path each stub cites, and
the first prompt from prompts/README.md to use after setup. Do not modify files
unless the active ticket explicitly allows this setup work.
```

## Expected response

- Claude Code mapping plan or created-file report.
- Cited role and contract paths.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | master | `prompts/01-init/apply-to-project.md` |
| needs_clarification | human | `prompts/07-providers/custom-instructions.md` |
| blocked | human | `prompts/06-control/halt.md` |

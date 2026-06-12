---
id: custom-instructions
stage: providers
mode: any
audience: human
target_role: none
pairs_with:
  - prompts/01-init/use-aegis-core.md
  - prompts/07-providers/codex-setup.md
requires:
  - AEGIS.md
  - contracts/kernel.md
returns:
  - provider custom instructions
  - standard role envelope
---

# Custom Instructions

## When to use

Use this prompt to generate provider custom instructions that point a runtime at
AEGIS-CORE without copying full role or contract bodies.

## Preconditions

- The provider has a custom-instructions or system-prompt surface.
- The operator wants AEGIS ticket discipline active by default.

## Prompt

```text
Draft provider custom instructions for AEGIS-CORE.

Required citations:
- AEGIS.md
- contracts/kernel.md
- contracts/swarm-contract.md
- contracts/ticket-contract.md
- contracts/epic-contract.md
- skills/roles/master/SKILL.md
- skills/roles/master-planner/SKILL.md when epic planning is requested

Instruction requirements:
- Load AEGIS.md first when the operator requests AEGIS-CORE.
- Require a binding acknowledgment before planning or implementation.
- Require a ticket envelope before implementation.
- Execute exactly one ticket at a time.
- Preserve master -> worker -> validator -> master routing.
- Enforce role locks: planners plan, master-agents supervise, workers edit,
  validators review.
- Treat validators as blocking unless the human records an override.
- Pass the AEGIS.md Conformance Gate before completion.
- Commit only ticket-owned changes with the format from contracts/kernel.md.

Provider:
[PROVIDER]

Runtime constraints:
[RUNTIME_CONSTRAINTS]

Return concise custom instructions and note which AEGIS prompt from
prompts/README.md the operator should use first.
```

## Expected response

- Provider custom instructions.
- Cited AEGIS files.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | human | `prompts/01-init/use-aegis-core.md` |
| needs_clarification | human | `prompts/07-providers/codex-setup.md` |
| blocked | human | `prompts/06-control/halt.md` |

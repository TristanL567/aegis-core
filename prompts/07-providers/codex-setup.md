---
id: codex-setup
stage: providers
mode: any
audience: human
target_role: none
pairs_with:
  - prompts/01-init/use-aegis-core.md
  - prompts/06-control/recover-context.md
requires:
  - contracts/kernel.md
  - execution/runbooks/codex.md
returns:
  - provider setup instructions
  - standard role envelope
---

# Codex Setup

## When to use

Use this prompt to operate AEGIS through Codex's run-and-return workflow.

## Preconditions

- The operator will carry envelopes and outputs between calls.
- The target ticket or planning task is available.

## Prompt

```text
Set up Codex for AEGIS run-and-return operation.

Use:
- AEGIS.md
- contracts/kernel.md
- contracts/swarm-contract.md
- contracts/ticket-contract.md
- execution/runbooks/codex.md
- prompts/README.md

Codex mapping:
- each call carries the active prompt, ticket envelope, role path, and prior
  artifacts explicitly;
- the operator routes master -> worker -> validator -> master between calls;
- validator findings block the next call unless the human records an override;
- recovery uses prompts/06-control/recover-context.md with carried artifacts.

Current task or ticket:
[TASK_OR_TICKET]

Return the next Codex call prompt to use, the role path it should load, and the
artifacts the operator must carry forward.
```

## Expected response

- Codex-specific routing setup.
- Next prompt and carried artifacts.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | master | `prompts/01-init/use-aegis-core.md` |
| completed | human | `prompts/06-control/recover-context.md` |
| blocked | human | `prompts/06-control/halt.md` |

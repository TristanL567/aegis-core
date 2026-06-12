---
id: antigravity-setup
stage: providers
mode: any
audience: human
target_role: none
pairs_with:
  - prompts/01-init/apply-to-project.md
  - prompts/03-execute/relay/dispatch-master-agent.md
requires:
  - contracts/kernel.md
  - execution/runbooks/antigravity.md
returns:
  - provider setup instructions
  - standard role envelope
---

# Antigravity Setup

## When to use

Use this prompt to start or configure an Antigravity session for one AEGIS
ticket or a master-agent assignment.

## Preconditions

- Repository root, branch, and ticket envelope are known.
- The operator wants Antigravity-specific session mapping only.

## Prompt

```text
Prepare Antigravity for AEGIS execution.

Repository root:
[REPOSITORY_ROOT]

Current branch and HEAD:
[BRANCH_AND_HEAD]

Use canonical behavior from:
- AEGIS.md
- contracts/kernel.md
- contracts/swarm-contract.md
- contracts/ticket-contract.md
- contracts/epic-contract.md
- skills/roles/master/SKILL.md
- selected worker role under skills/roles/
- selected validator role under skills/roles/

Ticket envelope:
[TICKET_ENVELOPE]

Provider mapping:
- one Antigravity master session coordinates one active ticket;
- selected workers receive the full ticket envelope;
- selected validators receive the full ticket envelope, worker output, changed
  files, and verification evidence;
- validators are blocking unless a human override is recorded.

Return the Antigravity session prompt and next AEGIS prompt route. Do not add
provider-specific behavior to core contracts or roles.
```

## Expected response

- Antigravity session setup.
- Selected role paths.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | master | `prompts/03-execute/relay/dispatch-master-agent.md` |
| needs_clarification | human | `prompts/01-init/apply-to-project.md` |
| blocked | human | `prompts/06-control/halt.md` |

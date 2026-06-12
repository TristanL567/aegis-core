---
id: apply-to-project
stage: init
mode: any
audience: human
target_role: skills/roles/master/
pairs_with:
  - prompts/01-init/use-aegis-core.md
  - prompts/02-plan/ticket-from-idea.md
requires:
  - AEGIS.md
  - contracts/kernel.md
  - execution/runbooks/apply-to-project.md
returns:
  - project application readiness
  - first ticket envelope or blockers
  - standard role envelope
---

# Apply To Project

## When to use

Use this prompt to start using AEGIS-CORE against a target project or repository
after the agent has acknowledged binding.

## Preconditions

- Binding has been acknowledged or will be verified first.
- The operator can provide target project context without secrets.
- The first ticket can be defined or blocked explicitly.

## Prompt

```text
Apply AEGIS-CORE to the target project using the canonical files below:
- AEGIS.md
- contracts/kernel.md
- contracts/swarm-contract.md
- contracts/ticket-contract.md
- skills/roles/master/SKILL.md
- execution/runbooks/apply-to-project.md
- execution/runbooks/shared-orchestration-loop.md

Do not copy contract or role bodies into the target project. Cite canonical
AEGIS-CORE paths when needed.

Target project context:
[TARGET_PROJECT_CONTEXT]

Repository state:
- branch: [BRANCH]
- head: [HEAD]
- unrelated dirty worktree entries: [DIRTY_WORKTREE]

Project constraints:
- allowed_areas: [ALLOWED_AREAS]
- must_not_touch: [MUST_NOT_TOUCH]
- validation_commands: [VALIDATION_COMMANDS]
- manual_verification: [MANUAL_VERIFICATION]
- secrets policy: do not copy secrets, credentials, private local paths,
  private repository URLs, or confidential configuration into prompts, docs,
  commits, or reports.

Requested application goal:
[APPLICATION_GOAL]

Return whether context is sufficient. If ready, return exactly one first ticket
envelope and selected worker and validator role paths. If not ready, return the
missing context that blocks ticket creation.

Hook install step: record whether the target project should install
execution/templates/hooks/ when available (pending: OVH-013). Do not install
hooks silently.
```

## Expected response

- Project readiness decision.
- First ticket envelope or missing context.
- Selected worker and validator role paths when ready.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | master | `prompts/03-execute/relay/dispatch-master-agent.md` |
| completed | worker | `prompts/03-execute/relay/relay-to-worker.md` |
| needs_clarification | human | `prompts/02-plan/ticket-from-idea.md` |
| blocked | human | `prompts/06-control/halt.md` |

# Claude Code Agent Setup

Use this prompt when asking Claude Code to create or refresh provider-local `.claude/agents/` stubs in a target project. Do not use it to create generated agents inside this repository unless a ticket explicitly allows that path.

```text
You are setting up Claude Code provider-local agents for an AEGIS workflow.

Target project root:
<absolute path to target project>

Canonical AEGIS library root:
<absolute path to aegis-core>

Create or update provider-local Claude Code agent stubs only in the target project, normally under:
<target project>/.claude/agents/

Do not modify the canonical AEGIS library except where an explicit ticket allows it.

Canonical role and rule sources:
- <aegis-core>/skills/master/SKILL.md
- <aegis-core>/skills/<selected-worker>/SKILL.md
- <aegis-core>/skills/<selected-validator>/SKILL.md
- <aegis-core>/contracts/ticket-contract.md
- <aegis-core>/contracts/swarm-contract.md
- <aegis-core>/execution/runbooks/shared-orchestration-loop.md
- <aegis-core>/execution/runbooks/claude-code.md

Generate concise agent stubs that:
- Reference the canonical skill and contract files instead of copying full bodies.
- Preserve the routing loop: master -> worker -> validator -> master.
- Keep human approval centralized through the master.
- Require one ticket at a time.
- Require workers to stay inside the ticket envelope.
- Require validators to review only and never implement fixes.
- Require the standard output envelope with status, summary, artifacts, findings, next_recommended_role, changed_files, and verification.

Suggested local agent responsibilities:
- master: load the canonical master skill, validate ticket completeness, select worker and validator, enforce scope, enforce validator gates, and prepare completion reports.
- worker: load the selected canonical worker skill, implement only the assigned ticket, report changed files and verification, and hand off to validator.
- validator: load the selected canonical validator skill, check worker output against the ticket envelope and verification evidence, and return findings to master.

Return:
- status
- summary of created or updated local files
- artifacts with local agent file paths
- findings
- next_recommended_role
```

## Ticket Session Prompt

Use this prompt to start a Claude Code ticket session after local agents are available.

```text
You are the Claude Code master agent for one AEGIS ticket.

Load and follow:
- <aegis-core>/skills/master/SKILL.md
- <aegis-core>/contracts/ticket-contract.md
- <aegis-core>/contracts/swarm-contract.md

Use these execution references:
- <aegis-core>/execution/runbooks/shared-orchestration-loop.md
- <aegis-core>/execution/runbooks/claude-code.md
- <aegis-core>/execution/templates/ticket-envelope.example.yaml
- <aegis-core>/execution/templates/completion-report.example.yaml

Ticket envelope:
<paste ticket envelope here>

Rules:
- Run exactly one ticket.
- Preserve the loop: master -> worker -> validator -> master.
- Dispatch to one selected worker skill from skills/.
- Route completed worker output to one selected validator skill from skills/.
- Treat validator findings as blocking unless explicit human approval is included.
- Do not duplicate full skill or contract prose in downstream prompts.

Return the standard envelope with:
- status
- summary
- artifacts
- findings
- next_recommended_role
- changed_files
- verification

Also return the next copy/paste worker prompt if the ticket is ready to dispatch.
```

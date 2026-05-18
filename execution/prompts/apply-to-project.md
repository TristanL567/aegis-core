# Apply to Project

Use this prompt to start an AEGIS application session against another project. It prepares context and backlog material, then preserves one-ticket-at-a-time execution.

```text
You are the master agent for applying AEGIS to another project.

Load and follow:
- skills/master/SKILL.md
- contracts/ticket-contract.md
- contracts/swarm-contract.md

Use operator guidance from:
- execution/runbooks/apply-to-project.md
- execution/runbooks/shared-orchestration-loop.md
- execution/runbooks/codex.md
- execution/runbooks/clean-commit.md

Use these prompts and examples for shape only:
- execution/prompts/start-ticket-run.md
- execution/prompts/validate-ticket.md
- execution/prompts/clean-commit.md
- execution/templates/ticket-envelope.example.yaml
- execution/templates/completion-report.example.yaml

Target project context:
- Project label: <for example, "MT project">
- Repository or workspace description: <describe without private local paths, secrets, credentials, or private URLs>
- Current branch: <paste branch>
- Current HEAD: <paste commit or "unknown">
- Known unrelated dirty worktree entries: <paste entries or "none">
- Build or dependency context: <paste relevant context>
- Project conventions: <tests, linting, formatting, generated files, review expectations>

Project constraints:
- allowed_areas: <paths or areas that AEGIS may change for the first ticket, or "to be defined per ticket">
- must_not_touch: <protected paths, generated artifacts, credentials, data, config, or other restricted areas>
- validation_commands: <exact commands required, or "to be defined per ticket">
- manual_verification: <manual checks required, or "to be defined per ticket">
- secrets_policy: Do not copy secrets, credentials, private local paths, private repository URLs, or project-specific confidential configuration into prompts, docs, commits, or reports.

Requested application goal:
<describe what AEGIS should help accomplish in this project>

Rules:
- Preserve the loop: master -> worker -> validator -> master.
- Create or refine a backlog if needed, but execute exactly one ticket at a time.
- Do not start implementation until one ticket envelope has a clear objective, allowed areas, must-not-touch areas, acceptance criteria, validation commands, manual verification expectations, and branch context.
- Select worker and validator skills from skills/ based on the ticket type.
- Keep canonical role behavior in skills/ and canonical field definitions in contracts/.
- Do not duplicate full skill or contract prose into downstream prompts.
- Do not hardcode private paths, secrets, credentials, repository URLs, or project-specific configuration.
- Do not change files outside the active ticket's allowed_areas.
- Preserve unrelated dirty worktree entries exactly as they are.
- If a required change exceeds the ticket boundary, return a blocker instead of expanding scope.
- Require validator approval before clean commit preparation or the next ticket.
- Use execution/prompts/start-ticket-run.md for the selected ticket.
- Use execution/prompts/validate-ticket.md for the validator gate.
- Use execution/prompts/clean-commit.md only after validator approval.

Return:
- Whether the project context is sufficient.
- Any missing context that blocks backlog creation or ticket dispatch.
- A proposed ticket backlog, if requested or needed.
- The single next ticket envelope to run first, if ready.
- The selected worker skill path for that ticket.
- The selected validator skill path for that ticket, if known.
- A copy/paste worker prompt for that ticket only.
- The standard envelope fields:
  - status
  - summary
  - artifacts
  - findings
  - next_recommended_role
  - changed_files
  - verification
```

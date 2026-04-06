# Testing the Skill Library

This repository includes a lightweight validator to confirm the basic library contract.

## Command

```powershell
py -3.10 .\tools\validate_skill_library.py
```

## What It Checks

- skill discovery under `skills/*/SKILL.md`
- required frontmatter fields
- valid role values
- valid handoff targets
- expected output envelope fields
- presence of at least one `master`, `worker`, and `validator`

## Workflow-Level Scenarios

Use these scenarios when validating an execution runtime built on top of this library:

1. Backend flow: `master -> backend-worker -> code-validator -> master`
2. DS flow: `master -> backend-worker -> ds-validator -> master`
3. Blocking gate: validator returns `fixes_required`, master routes remediation
4. Human checkpoint: only the master requests approval to continue
5. Adapter parity: one canonical skill maps cleanly into Codex, Claude Code, and Antigravity

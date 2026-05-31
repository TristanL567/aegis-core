# User Instructions

AEGIS Core is the canonical governance repo for agentic coding. It defines how
agents should plan, execute, validate, and report work without losing human
overview.

## How To Address Agents

Use this phrase when you want an external agent to follow this repo:

```text
reference AEGIS-CORE
```

That instruction means the agent must load `AEGIS.md` first and follow its
bootstrap order before implementation.

## Core Rules

- Work happens through tickets.
- Execute one ticket at a time unless an explicit epic-planner workflow governs
  multiple masters.
- The standard loop is `master -> worker -> validator -> master`.
- Validators are blocking unless the human explicitly overrides a finding.
- Completed work must include a full completion report with changed files,
  verification, findings, and human-readable diff context.

## What AEGIS Optimizes For

AEGIS favors small scope, human overview, readable diffs, clear architecture
boundaries, and explicit validation. It is not just a prompt library and not a
license for agents to roam through a repo. It is a governance layer for keeping
agentic coding reviewable.

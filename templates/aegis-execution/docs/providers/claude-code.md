# Claude Code Execution Guide

Claude Code is a strong fit for file-based subagent execution because the derived agent
files can live directly in `.claude/agents/`.

## Recommended Pattern

- Generate or copy derived agent files from the canonical library.
- Keep the execution repo responsible for the derived `.claude/agents` files.
- Preserve the `master -> worker -> validator -> master` flow.

## Starter Steps

1. Copy the sample `.claude/agents` files from `templates/claude-code/`.
2. Replace placeholder references to the canonical skill library path.
3. Use the `master` agent for coordination.
4. Route implementation work to the right worker agent.
5. Route the result to a validator agent before the master asks for human approval.

# Execution Prompts

This directory contains operator prompts and launch prompts for execution workflows.

Current prompts:

- `start-master.md`: start a master session for ticket routing.
- `start-ticket-run.md`: dispatch a single ticket run.
- `validate-ticket.md`: route completed work through a validator gate.
- `completion-report.md`: request a structured completion report.
- `clean-commit.md`: prepare a clean, scoped commit after validation.
- `apply-to-project.md`: apply AEGIS guidance to another repository or project.
- `use-aegis-core.md`: bind an external agent to the AEGIS contract when it is told to reference this repo.
- `aegis-conformance-check.md`: helper prompt for self-auditing a run against
  the AEGIS conformance gate before reporting done. `AEGIS.md` remains the
  canonical Conformance Gate source.
- `claude-code-agent-setup.md`: set up Claude Code local agent stubs.
- `antigravity-master-session.md`: run an Antigravity master session.

Canonical role behavior remains in `skills/`, and canonical ticket and swarm rules remain in `contracts/`.

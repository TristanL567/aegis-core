# AEGIS Options And Prompts

## Canonical Invocation

Use this prompt shape when applying AEGIS:

```text
reference AEGIS-CORE. Load AEGIS.md first. Create or validate one ticket
envelope before implementation. Execute one ticket only. Route work through
master -> worker -> validator -> master. Run validator before completion and
return the full completion report.
```

A bare repo reference is weaker than the canonical invocation. Agents must not
skip `AEGIS.md`.

## When To Use AEGIS

- Normal one-ticket workflow: use when a scoped change needs implementation and
  validation.
- Apply AEGIS to another project: use when a target repo should follow AEGIS
  tickets, roles, validators, and completion reporting.
- Clean commit workflow: use after validation when the user wants a scoped,
  reviewable commit.
- Validation-only workflow: use when completed work needs independent review.
- Epic planner / multi-master workflow: use when an epic envelope dispatches
  multiple masters under a `master-planner`.

## Important Prompt Locations

- `execution/prompts/use-aegis-core.md`: copy/paste prompt for binding another
  agent to AEGIS.
- `execution/prompts/validate-ticket.md`: validator prompt for ticket review.
- `execution/prompts/completion-report.md`: structured completion-report prompt.
- `execution/prompts/clean-commit.md`: scoped commit preparation prompt.
- `execution/prompts/apply-to-project.md`: prompt for applying AEGIS to a target
  project.

## Important Runbooks

- `execution/runbooks/shared-orchestration-loop.md`: standard
  `master -> worker -> validator -> master` loop.
- `execution/runbooks/apply-to-project.md`: applying AEGIS outside this repo.
- `execution/runbooks/clean-commit.md`: scoped staging and commit guidance.
- `execution/runbooks/multi-master-dispatch.md`: epic planner / multi-master
  dispatch.
- `execution/runbooks/understand-anything.md`: optional Understand Anything
  evidence workflow.

## Options

- Provider choice: Codex, Claude Code, Antigravity, or another runtime can use
  AEGIS if it preserves the contracts.
- Workflow scale: use the standard ticket workflow for most work; use the epic
  planner workflow only when an epic envelope governs multiple masters.
- Master-planner autonomy policy: `manual`, `checkpointed`, or
  `autonomous_until_error`.
- Optional codebase map evidence: Understand Anything may provide context, but
  it is advisory evidence only.
- Optional procedural skills: invoke them only when their situation-specific
  trigger applies.
- Optional references: use them as knowledge drawers, not as triggerable skills.
- Human override: validator findings can be overridden only when the human
  explicitly says so.

## Caveats

- AEGIS is not a code generator by itself; it is the governance framework for
  agentic work.
- Optional tools do not override AEGIS contracts.
- Validators remain blocking by default.
- Ticket scope wins over agent enthusiasm.
- The full completion report is required for completed ticket work.
- If the ticket is unclear, clarify before implementation.

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

## Useful Prompts

### Initialize the Master-Planner

Use this when starting a project, epic, or multi-ticket effort:

```text
reference AEGIS-CORE. Load AEGIS.md first, then the relevant contracts,
especially contracts/epic-contract.md, contracts/ticket-contract.md, and
contracts/swarm-contract.md. Load the relevant runbooks, especially
execution/runbooks/multi-master-dispatch.md when epic planning is involved.
Act as the AEGIS Master-Planner.

Own the project, roadmap, epic sequencing, and final integration. Do not
implement directly. First inspect the target repo/project context, then produce
or validate an epic envelope and a sequenced ticket backlog. Each ticket must
declare goal, dependencies, allowed areas, must-not-touch paths, requirements,
non-goals, acceptance criteria, verification commands, and completion-report
requirements.

Before dispatching any work, summarize:
- loaded AEGIS contracts, skills, and runbooks;
- proposed architecture boundary;
- proposed epics and ticket sequence;
- validation and commit policy;
- where human checkpoints are required.
```

### Architecture Outline Before Tickets

Use this when the system design is unclear or software entropy risk is high:

```text
reference AEGIS-CORE. Before creating implementation tickets, outline the
target architecture and business design. Consider docs/skill-architecture.md,
contracts/ticket-contract.md, contracts/epic-contract.md, and the relevant
procedures for design clarification, ubiquitous language, test-first change,
and module-boundary review.

Return a concise architecture brief covering:
- business/user outcome;
- core domain language;
- module boundaries and ownership;
- deep vs. shallow module risks;
- test and validation strategy;
- likely tickets;
- explicit non-goals.

Do not implement code until the architecture brief is accepted or converted
into scoped tickets.
```

### Force AEGIS Consideration

Use this when an agent might otherwise treat AEGIS as a vague reference:

```text
You must explicitly consider AEGIS-CORE before acting. Load AEGIS.md first.
Then load the relevant contract files, including contracts/swarm-contract.md,
contracts/ticket-contract.md, and contracts/epic-contract.md when epic planning
or planner dispatch is involved. Load the relevant runbooks for this task.
State which AEGIS materials you loaded and how they constrain the work.

If no ticket envelope exists, create or request one before implementation. If a
ticket exists, execute exactly that ticket and no future-ticket work. Route
through master -> worker -> validator -> master, treat validator findings as
blocking unless I explicitly override them, and return the full completion
report.
```

### Manual Route: Master-Planner And Master-Agent

```text
Act as the AEGIS Master-Planner. Provide me with the instructions for the
Master-Agent and the next ticket only.

I will route the instructions to the Master-Agent manually. The Master-Agent
must return a concise ticket execution summary with changed files, validation,
commit evidence if required, blockers, and next handoff state.

I will paste the Master-Agent summary back here. Validate the executed ticket
against the ticket envelope and AEGIS contracts. If a commit is required and the
summary is valid, tell me the exact scoped commit to make on the assigned branch.
The commit message must include the epic ID, ticket ID, type, and concise
description:

<EPIC-ID> <TICKET-ID> <type>: <concise description>

After I confirm the commit or required evidence, provide the next ticket
instruction. Continue until the epic pipeline is complete.
```

### Master-Agent Assignment Prompt

Use this when assigning one visible Master-Agent chat to one epic:

```text
reference AEGIS-CORE. You are a reusable AEGIS Master-Agent assigned by the
Master-Planner to this epic only:

Epic: <EPIC-ID>
Ticket: <TICKET-ID>
Branch: <BRANCH>
Visible chat name: AEGIS Master-Agent | <EPIC-ID>

Load AEGIS.md, the assigned ticket envelope, the relevant contracts, and any
relevant skills/runbooks. Execute only the assigned ticket. Use workers,
validators, procedures, and references internally as needed. Commit finished
validated work to the assigned branch if the assignment requires a commit.

Report:
- loaded AEGIS materials;
- assigned epic and ticket;
- implementation summary;
- validation summary;
- commit hash and message, if committed;
- blockers, if any;
- next handoff state.
```

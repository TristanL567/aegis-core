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

### Automated Route: Master-Planner And Master-Agent

```text
reference AEGIS-CORE. Load AEGIS.md first, then contracts/epic-contract.md,
contracts/ticket-contract.md, contracts/swarm-contract.md, and
execution/runbooks/multi-master-dispatch.md.

Act as the AEGIS Master-Planner. Own the project, roadmap, epic sequencing,
Master-Agent assignment, checkpoints, ledger decisions, and final integration.
Do not implement work directly.

Dispatch reusable Master-Agents in visible chats. Reuse existing Master-Agent
chats when possible. Rename each visible Master-Agent chat to:

AEGIS Master-Agent | <EPIC-ID>

Each Master-Agent may work on one epic assignment at a time. Dispatch exactly
one assigned ticket at a time unless the epic contract explicitly allows a
bounded ticket set. Each assignment must include epic ID, ticket ID, branch,
allowed areas, must-not-touch paths, verification commands, and whether
commit_required is true.

The Master-Agent must load AEGIS.md, the assigned ticket envelope, relevant
contracts, and relevant runbooks. It may use AEGIS roles, procedures,
references, workers, and validators internally.

The validator validates only. It does not commit. If commit_required is true,
the Master-Agent commits validated work to the assignment branch using:

<EPIC-ID> <TICKET-ID> <type>: <concise description>

After each ticket, the Master-Agent reports loaded AEGIS materials, assigned
epic/ticket, implementation summary, validation summary, commit hash/message if
committed, blockers, and next handoff state.

The Master-Planner validates the report against the ticket envelope and AEGIS
contracts, records the result, and dispatches the next ticket only if the
assignment completion gate passes.

If blockers, validator blocking findings, scope conflicts, checkpoint tickets,
merge conflicts, unauthorized destructive actions, or secrets risks occur, stop
and escalate according to contracts/epic-contract.md.

Notify the human at required checkpoints, critical errors, merge gate, or epic
completion according to the epic autonomy policy.
```

### Idea To Epic Intake

Use this when you have a broad idea but not yet a clean architecture or backlog:

```text
reference AEGIS-CORE. Act as the AEGIS Master-Planner. I have an idea, not a
ticket. Do not implement yet.

First produce a concise project intake:
- business/user outcome;
- target repo or product area;
- relevant constraints and risks;
- architecture assumptions that need confirmation;
- likely epics;
- questions that must be answered before ticket creation.

Then propose the smallest useful first epic and explain why it should come
first. Do not create implementation tickets until the intake is accepted.
```

### Review An Epic Plan

Use this before letting a generated epic/ticket backlog execute:

```text
reference AEGIS-CORE. Review this epic and ticket backlog against AEGIS
contracts before implementation.

Check:
- every ticket has explicit allowed areas and must-not-touch paths;
- dependencies and sequence are coherent;
- tickets are small enough for one-ticket execution;
- acceptance criteria and verification commands are testable;
- architecture and business context are sufficient;
- no future-ticket work is hidden in early tickets;
- validator and commit expectations are clear.

Return blocking findings first, then recommended edits. Do not implement.
```

### Resume A Paused Epic

Use this when returning to a partially executed epic:

```text
reference AEGIS-CORE. Act as the AEGIS Master-Planner and resume this epic.

Load AEGIS.md, contracts/epic-contract.md, the epic envelope, the ticket files,
and any ledger or completion reports. Reconstruct the current state from the
latest committed ticket, ledger entry, or pasted Master-Agent report.

Report:
- completed tickets and commits;
- current assignment state;
- unresolved blockers or validator findings;
- next safe ticket;
- whether a human checkpoint or merge gate is active.

Do not dispatch new work until the reconstructed state is clear.
```

### Final Integration And Merge Readiness

Use this before merging an epic branch:

```text
reference AEGIS-CORE. Act as the AEGIS Master-Planner and perform final
integration review for this epic.

Check the epic envelope, all ticket completion reports, validator decisions,
commit messages, branch state, and declared verification commands. Confirm every
commit matches:

<EPIC-ID> <TICKET-ID> <type>: <concise description>

Report:
- tickets completed;
- commits included;
- validation evidence;
- unresolved risks;
- files or systems changed;
- whether merge_policy is satisfied;
- whether human approval is required before merge.

Do not merge until the merge gate is satisfied.
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

# Human Usage Guide

This guide is for human operators who want to use AEGIS Core from GitHub or from
a local checkout. It explains what to load, what to paste into another agent,
which optional settings exist, and what caveats protect the work from AI-driven
software entropy.

## What AEGIS Core Is

AEGIS Core is a reusable operating framework for agentic coding. It does not
replace software engineering judgment. It gives agents a disciplined workflow:

1. clarify the work;
2. create one bounded ticket;
3. route implementation through a worker;
4. route the result through a validator;
5. report changed files, verification, risks, and manual checks;
6. commit only scoped, ticket-owned work.

The central promise is human overview. AEGIS optimizes for small, reviewable,
validated changes rather than autonomous volume.

## Fast Start

When you want an agent to use this repo on another project, paste:

```text
Reference AEGIS-CORE. Load AEGIS.md first, follow its Bootstrap Load Order,
use ticketing, route work through master -> worker -> validator -> master, and
pass the AEGIS.md Conformance Gate before reporting completion.
```

For a fuller prompt with placeholders, use:

- `execution/prompts/use-aegis-core.md`

## Required Files To Load

The canonical load order is defined in `AEGIS.md`:

1. `AEGIS.md`
2. `contracts/swarm-contract.md`
3. `contracts/ticket-contract.md`
4. `skills/roles/master/SKILL.md`
5. `execution/runbooks/shared-orchestration-loop.md`
6. `execution/runbooks/apply-to-project.md`

Worker and validator roles are loaded per ticket based on the work type.

## How A Human Should Operate AEGIS

1. Describe the target project and the desired outcome.
2. Ask the master to create or validate exactly one ticket.
3. Confirm the ticket has `allowed_areas`, `must_not_touch`, acceptance
   criteria, and verification commands.
4. Let the worker implement only that ticket.
5. Send the worker output to a validator.
6. Treat validator findings as blocking unless you explicitly approve an
   override.
7. Commit only the validated ticket-owned changes.

If the agent cannot define a clear ticket, it should ask for clarification
rather than implement.

## Ticket Context That Matters

For mechanical work, a small ticket can be enough. For product, business,
workflow, or architecture-sensitive work, require these fields when relevant:

- `business_context`: why the work matters.
- `user_or_operator_outcome`: who benefits and what outcome they need.
- `design_concept`: the behavior, workflow, or UX concept to preserve.
- `architecture_boundary`: the module, layer, service, component, data, or
  integration boundary to respect.
- `success_signal`: observable evidence that the result worked.
- `tradeoffs_or_constraints`: compatibility, rollout, performance, compliance,
  review, or business constraints.

These fields prevent technically plausible but strategically wrong
implementation.

## Optional Settings And Extensions

### Understand Anything / Codebase Maps

AEGIS can optionally use Understand Anything or comparable graph tools for
system context.

Use it when:

- the target project is unfamiliar;
- a ticket may affect architecture or module boundaries;
- business flows or domain terms are unclear;
- a diff impact review would reduce risk.

Do not use it when:

- the ticket is small and local context is sufficient;
- graph exploration would expand scope;
- generated artifacts are not allowed by the ticket.

Relevant files:

- `docs/cross-references/understand-anything.md`
- `execution/runbooks/understand-anything.md`
- `skills/procedures/codebase-map-generation/SKILL.md`

Generated graph claims are advisory. They must be checked against source files
before they become AEGIS evidence.

### Design Clarification

Use `skills/procedures/design-clarification-interview/SKILL.md` when a request
has unclear product, business, workflow, or architecture intent. The right output
is focused questions or a concise design brief, not code.

### Ubiquitous Language

Use `skills/procedures/ubiquitous-language-map/SKILL.md` when business terms,
code identifiers, docs, schemas, routes, tests, or UI labels do not clearly mean
the same thing.

### Test-First Changes

Use `skills/procedures/test-first-change/SKILL.md` when executable behavior
changes and a failing test, reproduction, baseline command, fixture, or manual
pre-change evidence is feasible.

### Module Boundary Review

Use `skills/procedures/module-boundary-review/SKILL.md` when a change may cross
module ownership, expand a public interface, add shared helpers, or create
shallow modules with complex coupling.

## Artifact And Commit Policy

- Generated graph scratch from Understand Anything is not committed by default.
- `.understand-anything/intermediate/` and
  `.understand-anything/diff-overlay.json` are ignored.
- Shareable graph artifacts may be committed only when a ticket explicitly lists
  them in `allowed_areas`.
- Completion reports must state what was changed, what was verified, and what
  risk remains.

## Important Caveats

- AEGIS is not a blind "spec to code" pipeline.
- Do not let agents implement future-ticket work.
- Do not let optional graph or search tools override ticket scope.
- Do not treat generated summaries as authority without source confirmation.
- Do not copy AEGIS role or contract bodies into target projects unless you
  intentionally want a fork.
- Keep provider-specific runtime glue outside AEGIS Core unless a ticket is
  explicitly about AEGIS itself.

## Recommended Human Review Questions

Before approving a ticket, ask:

- Did the agent execute exactly one ticket?
- Did changed files stay inside `allowed_areas`?
- Were `must_not_touch` paths preserved?
- Did the validator approve the work or did I explicitly override it?
- Are tests, commands, or manual checks named?
- Is the diff small enough to review?
- Did the result preserve the intended business and architecture design?


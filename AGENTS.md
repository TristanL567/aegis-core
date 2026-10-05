# AEGIS

Rules for agentic coding work a human can trust and review: every change is
scoped by a ticket, checked by an independent validator, and traceable to a
commit.

These rules apply to any task that edits project files. Reading, exploring, and
answering questions need no ticket. The human may waive the ticket for one
specific trivial change by saying so explicitly.

## The loop

1. **Ticket.** No edits before the human approves a ticket. Draft it with the
   `write-ticket` skill, save it as `.aegis/tickets/<ID>.yaml`, and write `<ID>`
   to `.aegis/active-ticket`. Note any files already modified before you start.
2. **Implement** inside the ticket's scope, following the rules below.
3. **Validate.** Hand the ticket ID, and the list of already-modified files, to
   the validator: a fresh-context reviewer that did not write the code. In
   Claude Code that is the `validator` subagent; elsewhere, a new session given
   `.claude/agents/validator.md` as its prompt. Don't pass your own test
   results; the validator runs the checks itself. On `FIXES_REQUIRED`, fix the
   findings and validate again; after three failed rounds, stop and ask the
   human. On `BLOCKED`, stop and bring the finding to the human.
4. **Report** to the human in the format below.
5. **Commit** only when the human asks or the ticket requires it.

Work on one ticket at a time. Finish or explicitly abandon the active ticket
before starting another. Work too large for one ticket becomes an ordered list
of tickets, each run through this loop on its own.

## Ticket format

```yaml
id: PROJ-012                  # uppercase letters, digits, hyphens; = file name
goal: The outcome, in one sentence.
context: >                    # why it matters, who it serves, and the design
  ...                         # intent or architecture boundary to keep
depends_on: []                # ticket IDs or conditions; [] means none
allowed_areas:                # the only paths you may change
  - .aegis/tickets/PROJ-012.yaml
  - src/billing/              # trailing / = directory prefix; no globs
  - tests/billing/test_invoice.py
must_not_touch:               # wins over allowed_areas
  - src/billing/migrations/
non_goals:                    # adjacent work that is explicitly out of scope
  - ...
acceptance_criteria:          # each one objectively checkable
  - ...
verify:                       # commands the validator runs
  - pytest tests/billing
manual_checks: []             # ordered checks only a human can do
```

## Rules

**Scope**
- Change only paths in `allowed_areas`. Never change `must_not_touch`.
- Treat `non_goals` as boundaries, not suggestions. Don't do another ticket's
  work.
- If the ticket can't be finished inside its scope, stop and tell the human
  which scope change or follow-up ticket would unblock it. Never widen scope
  yourself.
- When intent, a domain term, or a boundary is unclear, ask. Don't fill the gap
  with a plausible default.

**Changes**
- A behavior change starts with a check that fails before the change: a test, a
  reproduction, or recorded baseline output. If none is feasible, say why
  before changing code.
- Make the smallest diff that meets the acceptance criteria. No speculative
  code, unrelated refactors, formatting sweeps, or dependency changes unless
  the ticket owns them.
- Add an abstraction only when it removes real complexity now, and say why in
  the report.

**Validation**
- The validator is blocking. Never report a ticket done without `APPROVED` or
  an explicit human override.
- Only the human can override a validator finding. Report an override as an
  override, never as approval.
- Never say a check passed unless you ran it and saw it pass. Name every check
  you skipped and why.

**Git**
- Commit subject: `[ID] what changed`, with the description at 72 characters
  or fewer.
- One commit per ticket, containing the ticket's file and its work, nothing
  else. Leave unrelated changes alone: don't stage, revert, or stash them.
- No push, force-push, branch deletion, history rewrite, or handling of secrets
  without explicit human approval.

## Completion report

```text
Ticket:       <ID>: <goal>
Validator:    APPROVED | OVERRIDDEN (<finding>, approved by the human because <reason>)
Changed:      <path>: <one-line purpose>, one per line
Verified:     <command> -> <result>, one per line
Not verified: <check>: <why skipped>, <remaining risk>; or "none"
Manual:       <manual_checks left for the human>; or "none"
Notes:        <abstractions added and why, follow-up tickets, risks>
```

Keep it short enough that the human can judge the change without reading the
whole diff.

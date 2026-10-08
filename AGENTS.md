<!-- aegis:begin -->
# AEGIS

Rules for agentic coding work a human can trust and review: every change is
scoped by a ticket, checked by an independent validator, and traceable to a
commit.

These rules apply to any task that edits project files. Reading, exploring, and
answering questions need no ticket. The human may waive the ticket for one
specific trivial change by saying so explicitly.

Skills live in `.claude/skills/<name>/SKILL.md`. If your tool doesn't load
skills on its own, read the file and follow it.

## The loop

1. **Ticket.** Draft it with the `write-ticket` skill, save it as
   `.aegis/tickets/<ID>.yaml`, and write `<ID>` to `.aegis/active-ticket`.
   Note any files already modified before you start. If `human_gates`
   includes `ticket`, show the ticket and wait for the human's approval before
   saving it and going on.
2. **Worktree.** Work in the ticket's own worktree and branch (see
   Isolation).
3. **Implement** inside the ticket's scope, following the rules below.
4. **Validate**, without asking. Start a fresh-context subagent that did not
   write the code and tell it to follow `.claude/skills/validate/SKILL.md`.
   Pass it the ticket ID, the worktree path, the base ref, the originating
   request (issue text or the human's words), and the already-modified files.
   Don't pass your own test results; the validator runs the checks itself. On
   `FIXES_REQUIRED`, fix the findings and validate again with a new subagent;
   after three failed rounds, stop and ask the human. On `BLOCKED`, stop and
   bring the finding to the human.
5. **Report** to the human in the format below.
6. **Commit** the ticket on its branch once the validator approves. Push the
   branch and open a pull request when the human or the ticket asks for it.
   Merge only as Human gates allow.

Each agent works on one ticket at a time. Finish or explicitly abandon the
active ticket before starting another. Work too large for one ticket becomes
an epic: an ordered list of tickets that share an epic branch, each run
through this loop on its own.

## Ticket format

```yaml
id: PROJ-012                  # uppercase letters, digits, hyphens; = file name
goal: The outcome, in one sentence.
context: >                    # why it matters, who it serves, and the design
  ...                         # intent or architecture boundary to keep
epic: null                    # epic ID if the ticket belongs to one
depends_on: []                # ticket IDs or conditions; [] means none
human_gates: []               # ticket, merge; [] means fully automatic
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
smoke:                        # how to start the dev environment, then what
  - Start the app with npm run dev on a free port   # to check in it;
  - Open /invoices/42; every line shows its VAT     # [] if nothing runs
manual_checks: []             # ordered checks only a human can do
```

## Human gates

Validation is automatic. The human adds gates per ticket in `human_gates`:

- `ticket`: the human approves the ticket before implementation starts.
- `merge`: the human approves before the ticket's branch merges anywhere,
  including into an epic branch.

With `[]`, the default, the agent tickets, implements, validates, and commits
without stopping. Set gates from the human's words or the issue (for example,
a label that names the gate). Never remove a gate the human set.

These always stop for the human, whatever `human_gates` says:

- merging or pushing to the default branch;
- deploys and releases;
- migrations on shared data;
- handling secrets: creating, reading out, or changing them;
- deleting data or branches, or rewriting pushed history, including
  force-push.

## Isolation

Parallel agents must not see each other's unfinished work.

- One worktree and branch per ticket: `aegis/<ID>`. A ticket in an epic
  branches from the epic branch `aegis/<EPIC>`; any other ticket branches from
  the default branch. Where each run is already its own container, such as CI
  or a cloud session, that container is the worktree.
- A worktree separates files only. Ports, databases, local services, caches,
  `.env` files, and the git stash stay shared, so smoke tests run in an
  environment private to the ticket:
  - pick a free port, never a fixed one another agent may hold;
  - use a per-ticket database, schema, or throwaway instance, never shared
    data;
  - install dependencies inside the worktree;
  - never use `git stash`; set work aside with a WIP commit on the ticket
    branch, and squash it into the ticket's commit before pushing;
  - stop everything you started when you're done, including on failure.
- After an epic's tickets merge into the epic branch, validate the epic once
  more on that branch: a validator subagent runs every ticket's `verify` and
  `smoke` together.

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

## Completion report

```text
Ticket:       <ID>: <goal>
Validator:    APPROVED | OVERRIDDEN (<finding>, approved by the human because <reason>)
Gates:        <gates that stopped for the human>; or "none"
Changed:      <path>: <one-line purpose>, one per line
Verified:     <command> -> <result>, one per line
Not verified: <check>: <why skipped>, <remaining risk>; or "none"
Manual:       <manual_checks left for the human>; or "none"
Notes:        <abstractions added and why, follow-up tickets, risks>
```

Keep it short enough that the human can judge the change without reading the
whole diff.
<!-- aegis:end -->

<!-- aegis:begin -->
# AEGIS

Every edit to project files is scoped by a ticket, checked by an independent
validator, and traceable to a commit; reading and answering need no ticket.
The human may waive the ticket for one trivial change by saying so. Skills
are in `.claude/skills/<name>/SKILL.md`; if your tool doesn't load them, read
and follow them.

## The loop

1. **Ticket.** Draft it with `write-ticket`; the format is in
   `.claude/skills/write-ticket/ticket-format.md`. Save it as
   `.aegis/tickets/<ID>.yaml`, write `<ID>` to `.aegis/active-ticket`, and
   note files already modified. A change you can state in one sentence gets a
   short ticket. If `human_gates` has `ticket`, show it and wait for approval
   before saving it.
2. **Worktree.** Work on branch `aegis/<ID>` in its own worktree, branched
   from `aegis/<EPIC>` in an epic, else from the default branch. Where each
   run is already its own container (CI, a cloud session), that is the
   worktree.
3. **Implement** inside the ticket's scope, by the rules below.
4. **Validate** without asking: a fresh subagent that didn't write the code
   follows `.claude/skills/validate/SKILL.md`. Give it the ticket ID,
   worktree, base ref, the originating request and the already-modified
   files, not your test results. On `FIXES_REQUIRED`, fix and validate with a
   new subagent; after three failed rounds, ask the human. On `BLOCKED`,
   bring it to the human.
5. **Report** in the format below.
6. **Commit** after `APPROVED`: one commit, `[ID] what changed` (description
   at most 72 characters), with the ticket file and its work only. Push or
   open a pull request when the human or the ticket asks; merge only as the
   gates allow.

One ticket per agent at a time; finish or explicitly abandon it before the
next. Work too large for one ticket becomes an epic: ordered tickets, each
through this loop, then a fresh validator subagent runs every ticket's
`verify` and `smoke` together on the epic branch.

## Sessions

- One ticket per session; an epic's tickets may run in sequence in one
  session, each validated by a fresh subagent. Clear the context between
  unrelated tasks.
- Implement a ticket drafted in an earlier conversation in a fresh session.
- After two corrections on the same issue, stop and restate the problem.
- Delegate broad exploration to subagents.

## Human gates

`human_gates` takes `ticket` (approve before work starts) and `merge` (approve
before any merge, into an epic branch too). Default `[]`: no stops. Take
gates from the human's words or issue labels; never remove one.

Always stop for the human: merging or pushing to the default branch; deploys
and releases; migrations on shared data; creating, reading out or changing
secrets; deleting data or branches, or rewriting pushed history.

## Isolation

Parallel agents must not see each other's unfinished work. A worktree
separates files only, so: use a free port, never a fixed one; use a per-ticket
database or throwaway instance, never shared data; install dependencies in
the worktree; set work aside with a `[ID] WIP` commit, squashed before
pushing, never `git stash`; stop everything you started, also on failure.

## Rules

- **Scope.** Change only `allowed_areas`, never `must_not_touch`; `non_goals`
  are boundaries; don't do another ticket's work. If the work doesn't fit,
  stop and say which scope change or follow-up ticket would unblock it.
  Never widen scope yourself.
- **Ask, don't guess** when intent, a domain term or a boundary is unclear.
- **A behavior change starts with a check that fails before it:** a test, a
  reproduction or recorded output. If none is feasible, say why first.
- **Smallest diff** that meets the criteria: no speculative code, unrelated
  refactors, formatting sweeps or dependency changes the ticket doesn't own.
  Add an abstraction only when it removes real complexity now, and say why.
- **The validator is blocking.** Never report done without `APPROVED` or the
  human's explicit override, reported as an override. Never say a check
  passed unless you saw it pass; name every check you skipped.
- Leave unrelated changes alone: don't stage, revert or stash them.

## Hooks

In Claude Code, `.claude/hooks/` blocks edits outside the active ticket's
scope and `git stash`, and records the validator's verdict in
`.aegis/verdicts/<ID>`. Git's hook in `.githooks/` refuses a commit without
the `[ID]` subject or an APPROVED verdict. Never write a verdict yourself;
only the human records an override. Where no hook runs, the rules still
hold.

## Design work

A new screen, flow, or feature whose design is still open gets a design
ticket (`kind: design`, always `human_gates: [ticket, merge]`) before any
implementation, run with the `design-track` skill. Every change users see
follows the product's `DESIGN.md` and works the same at phone and desktop
width: the same tasks, information, actions, and names.

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

Keep it short enough to judge without reading the whole diff.
<!-- aegis:end -->

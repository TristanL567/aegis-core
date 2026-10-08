---
name: write-ticket
description: Draft an AEGIS ticket, or an ordered set of tickets, from an idea, bug report, or feature request, with explicit file scope, checkable acceptance criteria, and real verification commands. Use before any implementation when no ticket exists, or when the user asks to plan, scope, break down, or ticket work. Asks clarifying questions instead of guessing intent.
---

# Write Ticket

Turn a request into a ticket a validator can check and, when asked, a human
can approve. The ticket format is in AGENTS.md. This skill only plans: don't
edit project code, and if `human_gates` includes `ticket`, don't save the
ticket until the human approves it.

## 1. Ground it in the code

Before drafting, read enough of the project to name real things:

- the files and directories the change will touch, and their tests;
- how the project checks itself: test, lint, and type-check commands from
  `package.json`, `pyproject.toml`, `Makefile`, CI config, or the README;
- risky neighbors: migrations, public interfaces, generated files, CI config,
  lockfiles, shared configuration.

## 2. Ask before guessing

Stop and ask when any of these hold:

- two or more plausible designs would satisfy the request but behave
  differently for the user or the architecture;
- the user, workflow, or outcome the change serves isn't stated;
- a domain term is ambiguous or used inconsistently;
- the module or layer boundary the change must respect is unclear;
- the request is vague: "improve", "clean up", "add support for", "handle edge
  cases".

Ask the fewest questions that remove the ambiguity, at most five, and give
each one a recommended answer so the human can simply confirm. Never write an
implementation-ready ticket on guessed intent. If part of the request is
clear, draft that part and list the open questions for the rest.

## 3. Size it

One ticket is one diff a human can review in a few minutes, and one validator
pass. Split when there are more than about five acceptance criteria, when
`allowed_areas` spans unrelated modules, or when one part could ship without
the other. Split tickets get sequential IDs and `depends_on` in execution
order.

## 4. Write the fields

- `id`: `<PREFIX>-<NNN>`. Reuse the prefix already used in `.aegis/tickets/`
  and take the next free number. Uppercase letters, digits, and hyphens
  only.
- `goal`: the outcome, not the activity. "Invoices show VAT per line", not
  "update invoice code".
- `context`: why it matters, who it serves, and the design intent or
  architecture boundary the implementation must keep, in one to three
  sentences. Leave it empty only for purely mechanical work.
- `epic`: the epic ID when the ticket is one of an epic's ordered tickets;
  otherwise `null`.
- `human_gates`: `ticket`, `merge`, both, or `[]`. Take them from the human's
  words or the issue (for example, a label that names the gate). Default to
  `[]`; never invent a gate the human didn't ask for, and never drop one they
  did.
- `allowed_areas`: as narrow as you can name. Use real paths: directories end
  with `/`, and there are no globs, because scope matches exact paths and `/`
  prefixes only. Always include the ticket's own file
  (`.aegis/tickets/<ID>.yaml`) and the tests the change needs.
- `must_not_touch`: the risky neighbors from step 1 that sit inside or next to
  `allowed_areas`. Skip paths nobody would touch anyway.
- `non_goals`: the adjacent work a helpful agent would be tempted to do.
- `acceptance_criteria`: each one checkable by reading the diff or running a
  command. Name observable behavior, not effort: "returns 422 with field
  errors for invalid input", not "handles errors".
- `verify`: commands that exist in this project today and cover the criteria.
  For a behavior change, include the test that fails before the change.
- `smoke`: ordered steps that start the dev environment and check the change
  in it, written so they can run on a free port with a per-ticket database or
  schema. Take the start command from the project. `[]` when the change has
  nothing to run, such as docs or a library without an app.
- `manual_checks`: only what a human has to look at, such as UI, real data, or
  external systems. `[]` if none.

## 5. Check, then present

Before showing the ticket, confirm:

- every path in `allowed_areas` exists, or is a new file under a directory
  that exists;
- no `must_not_touch` entry blocks a file the work needs;
- every `verify` command runs in the project today (run each once; failures
  caused by the missing change are expected), and needs no file outside
  `allowed_areas`;
- every `smoke` step can run privately to the ticket: no fixed port, no shared
  data;
- every acceptance criterion is covered by a `verify` command, a `smoke`
  step, or a manual check;
- nothing in `goal` or `acceptance_criteria` depends on an unanswered question.

Present the ticket as YAML. For a split, show the ordered list with one-line
goals first, then each ticket. Save each ticket to `.aegis/tickets/<ID>.yaml`
and write the first ticket's ID to `.aegis/active-ticket`. If `human_gates`
includes `ticket`, save only after the human approves, and don't start
implementing in the same turn unless the human says to; otherwise go on with
the loop.

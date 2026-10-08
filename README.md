# AEGIS

**Scoped, independently validated, traceable changes from AI coding agents.**

AI coding agents drift. They widen scope, refactor code nobody asked them to
touch, approve their own work, and report checks that never ran. AEGIS is a
short rule set that agents carry inside each repo. Every agent change stays
inside a ticket, is validated by an agent that didn't write it, and lands as
one traceable commit.

It's for developers who use Claude Code, Codex, or similar agents on real
codebases and want to control what changes without reading every line of
every diff. Validation runs automatically; you add a human gate only where
you want one.

## How it works

```text
write-ticket drafts a ticket
│ gate "ticket"? human approves
v
implement in own worktree <──┐
│                            │
v                            │
validate (fresh subagent)    │
├─ FIXES_REQUIRED ───────────┘
├─ BLOCKED ──> human decides
└─ APPROVED ─> report, commit
   gate "merge"? human merges
```

1. **Ticket.** Every edit starts from a ticket: the goal, the paths the agent
   may change, protected paths, checkable acceptance criteria, the commands
   that verify them, and smoke steps for the running app.
2. **Implement.** The agent works in the ticket's own worktree and branch, so
   parallel agents never see each other's unfinished work.
3. **Validate.** Without being asked, the agent starts a fresh subagent that
   follows the `validate` skill. It runs the checks and smoke tests itself in
   an isolated environment, reads the whole diff, and blocks until the ticket
   is met.
4. **Report and commit.** The agent reports what changed, what was verified,
   and what wasn't. Each ticket is one commit.

## The three parts

| Part | What it does |
| --- | --- |
| [`AGENTS.md`](AGENTS.md) | All the rules: the loop, the ticket format, human gates, isolation, and the completion report. Always loaded. |
| [`.claude/skills/`](.claude/skills/) | [`write-ticket`](.claude/skills/write-ticket/SKILL.md) turns a request into a ticket and asks instead of guessing. [`validate`](.claude/skills/validate/SKILL.md) is the independent review, run only by a subagent that didn't write the code. |
| [`PROMPTS.md`](PROMPTS.md) | Copyable prompts: install AEGIS into a repo, start work, implement, validate, ask for gates, update. Says when to use each skill. |

Once installed, a repo carries `AGENTS.md` and the skills itself;
`PROMPTS.md` stays here for you to copy prompts from. Agents in the cloud, in
CI, or on another machine never need this repository.

## Human gates

By default an agent tickets, implements, validates, and commits without
stopping. Ask for a gate per ticket, in your prompt or as an issue label:

- `human_gates: [ticket]`: you approve the ticket before work starts.
- `human_gates: [merge]`: you approve before the branch merges.

Some actions always stop for a human: merging or pushing to the default
branch, deploys, migrations on shared data, secrets, and deleting data,
branches, or pushed history.

## Core rules

- No edits without a ticket, and one ticket at a time per agent.
- Change only `allowed_areas` and never `must_not_touch`. If the work doesn't
  fit, stop and ask; never widen scope.
- When intent is unclear, ask instead of filling the gap with a plausible
  default.
- Make the smallest diff that meets the acceptance criteria: no speculative
  code, no unrelated refactors.
- The validator is blocking. Only the human can override it, and an override
  is reported as one.
- Never claim a check passed without running it, and name every skipped check.
- One commit per ticket, `[ID] description`, containing the ticket file and
  its work.

The full rules are in [`AGENTS.md`](AGENTS.md).

## A ticket

```yaml
id: SHOP-012
goal: Invoices show VAT per line.
context: Accountants reconcile VAT per invoice line.
epic: null
depends_on: []
human_gates: []
allowed_areas: [.aegis/tickets/SHOP-012.yaml, src/billing/, tests/billing/]
must_not_touch: [src/billing/migrations/]
non_goals: [Changing the PDF layout.]
acceptance_criteria: [Each invoice line returns its VAT amount.]
verify: [pytest tests/billing]
smoke: [Start the app on a free port, Open /invoices/42; every line shows VAT]
manual_checks: []
```

A path ending in `/` covers a directory; any other path must match exactly.
There are no globs, and `must_not_touch` wins over `allowed_areas`. Tickets
live in `.aegis/tickets/<ID>.yaml`, and the active ticket's ID is in
`.aegis/active-ticket`.

## Setup

Paste the bootstrap prompt from [`PROMPTS.md`](PROMPTS.md#bootstrap) into an
agent working in your repo. It copies `AGENTS.md` and the skills in, records
the aegis-core version in `.aegis/VERSION`, and shows you the diff before
anything is committed. If the repo already has an `AGENTS.md`, only the AEGIS
block between its markers is added or replaced.

## Daily use

1. Describe the change or point the agent at an issue, using a prompt from
   [`PROMPTS.md`](PROMPTS.md).
2. Add `human_gates` if you want to approve the ticket or the merge.
3. The agent tickets, implements, and validates until the validator approves.
4. Read the completion report and do any manual checks it lists.
5. Merge, or let the agent open a pull request for you to merge.

To pick up a newer aegis-core, use the update prompt in
[`PROMPTS.md`](PROMPTS.md#update-aegis-from-upstream).

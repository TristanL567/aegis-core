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

## How to use

1. **Install, once per repo.** Paste the
   [bootstrap prompt](PROMPTS.md#bootstrap) into an agent working in your
   repo. It copies in `AGENTS.md`, the skills, and the `ux-persona` agent,
   records the aegis-core version in `.aegis/VERSION`, and shows you the
   diff before anything is committed. An existing `AGENTS.md` keeps
   everything outside its AEGIS block.
2. **Start work.** Describe the change or point the agent at an issue with
   a [start-work prompt](PROMPTS.md#start-work). The agent tickets,
   implements in its own worktree, validates, commits, and sends you a
   completion report. Do the manual checks it lists, then merge.
3. **Start a design.** For a screen, flow, or feature whose design is still
   open, use the [design prompt](PROMPTS.md#start-a-design). It ends in a
   frozen spec that becomes a build epic.

What you approve, and when:

- Nothing by default; validation is automatic.
- The ticket before work starts, if you add `human_gates: [ticket]`.
- The merge, if you add `human_gates: [merge]`.
- Gates go in your prompt or on the issue as the label `aegis:gate-ticket`
  or `aegis:gate-merge`.
- A design ticket always stops twice: for the brief and for the freeze.
- Some actions always stop for you: merging or pushing to the default
  branch, deploys, migrations on shared data, secrets, and deleting data,
  branches, or pushed history.

[`PROMPTS.md`](PROMPTS.md) also has prompts to implement or validate one
ticket, and to [update AEGIS](PROMPTS.md#update-aegis-from-upstream).

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

1. **Ticket.** The goal, the paths the agent may change, checkable
   acceptance criteria, and the commands and smoke steps that verify them.
2. **Implement** in the ticket's own worktree and branch, so parallel agents
   never see each other's unfinished work.
3. **Validate.** Unasked, a fresh subagent runs every check itself, reads the
   whole diff, and blocks until the ticket is met.
4. **Report and commit:** what was and wasn't verified; one commit per
   ticket.

## The three parts

| Part | What it does |
| --- | --- |
| [`AGENTS.md`](AGENTS.md) | All the rules: the loop, the ticket format, human gates, isolation, when design work starts, and the completion report. Always loaded. |
| [`.claude/skills/`](.claude/skills/) | [`write-ticket`](.claude/skills/write-ticket/SKILL.md) turns a request into a ticket and asks instead of guessing. [`validate`](.claude/skills/validate/SKILL.md) is the independent review, run only by a subagent that didn't write the code. [`design-track`](.claude/skills/design-track/SKILL.md) runs a design ticket from brief to frozen spec. [`ux-test`](.claude/skills/ux-test/SKILL.md) usability-tests a prototype or build at phone and desktop width; [`ux-persona`](.claude/agents/ux-persona.md) is its screen-only persona subagent. |
| [`PROMPTS.md`](PROMPTS.md) | Copyable prompts: install AEGIS into a repo, start work or a design, implement, validate, ask for gates, update. Says when to use each skill. |

Once installed, a repo carries `AGENTS.md` and the skills itself; agents
never need this repository.

## Core rules

- No edits without a ticket, and one ticket at a time per agent.
- Change only `allowed_areas` and never `must_not_touch`. If the work doesn't
  fit, stop and ask; never widen scope.
- When intent is unclear, ask instead of filling the gap with a plausible
  default.
- Make the smallest diff that meets the acceptance criteria: no speculative
  code, no unrelated refactors.
- Only the human can override the validator.
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

## Design and mobile

Most people read on a phone, so the phone layout is never a cut-down
desktop. Design lives in three layers:

| Layer | Holds |
| --- | --- |
| [`AGENTS.md`](AGENTS.md) | Always loaded: when a design ticket is needed, and the parity rule. |
| [`design-track`](.claude/skills/design-track/SKILL.md) skill | The design process: prototype rounds, `ux-test`, the pass rule, the freeze. |
| `DESIGN.md` in your repo | That product's design contract: breakpoints, navigation, touch and input, formats, glossary. The first design ticket drafts it from the [template](.claude/skills/design-track/DESIGN-template.md); you approve it. |

**Parity rule:** one product, two layouts. Phone and desktop offer the same
tasks, information, actions, and names; only the layout differs. Every UI
ticket gets parity acceptance criteria, and the validator checks each
touched task at 390x844 and 1440x900. Anything available at only one width
blocks the ticket.

## Design track

When the design of a screen, flow, or feature is still open, start with a
design ticket instead of code:

```text
design ticket, gate "ticket"
│
v
prototype (one HTML file) <──┐
│                            │
v                            │
ux-test (fresh subagent)     │
│                            │
v                            │
decide each finding          │
├─ fix (max 3 rounds) ───────┘
└─ passes ─> gate "merge"
   freezes spec, decisions,
   findings, and DESIGN.md
   │
   v
   write-ticket: build epic
```

- The prototype is a throwaway file with fake data. It never ships.
- `ux-test` drives every key task like a user, at phone and desktop width,
  and rates each finding. Persona subagents run only if you ask for a
  persona pass.
- AI test results are evidence, not user validation. The design ticket
  keeps a short real-user check for you.
- The build epic reruns `ux-test` on the real build.

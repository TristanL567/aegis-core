# AEGIS prompts

Copy a prompt, fill in the `<placeholders>`, and paste it into an agent
working in the target repo. After the bootstrap, the repo carries AEGIS
itself: every agent that opens it reads `AGENTS.md`, and none of them needs
this repository again.

## When to use what

| Situation | Use | Who starts it |
| --- | --- | --- |
| Repo has no AEGIS yet | Bootstrap prompt | You, once per repo |
| New issue, bug, feature, or epic | `write-ticket` skill | The working agent, before any edit |
| Ticket implemented | `validate` skill | The working agent, in a fresh subagent; never itself |
| You want to approve something | `human_gates` | You, in the prompt or as an issue label |
| aegis-core changed | Update prompt | You |

## Bootstrap

```text
Install AEGIS from https://github.com/TristanL567/aegis-core (branch main) into this repo. This setup step needs no ticket.
1. Clone it to a new, uniquely named temporary directory outside this repo and note its commit SHA.
2. Copy its AGENTS.md here. If AGENTS.md exists, replace its <!-- aegis:begin --> ... <!-- aegis:end --> block, or add the block at the top if there is none; keep everything else.
3. Copy each folder in its .claude/skills/ into .claude/skills/ here, replacing only skills with the same name.
4. If CLAUDE.md exists and doesn't contain @AGENTS.md, add that line at its top; if there is no CLAUDE.md, create CLAUDE.md containing only @AGENTS.md.
5. Write the SHA to .aegis/VERSION, and add .aegis/active-ticket and .claude/worktrees/ to .gitignore if missing.
6. Remove the temporary clone (it is not project data), show me the diff, and commit only when I ask.
```

## Start work

Ticket an issue, bug, or feature with `write-ticket`, then run the loop:

```text
Follow AGENTS.md for <issue URL or description>. Ticket it with the write-ticket skill, implement it on its own worktree and branch, validate it automatically, and report. human_gates: []
```

All the way to a pull request:

```text
Follow AGENTS.md for <issue URL or description>: ticket, implement, validate, commit, push the ticket branch, and open a pull request. human_gates: []
```

An epic:

```text
Follow AGENTS.md. Use the write-ticket skill to split <description> into epic <EPIC-ID>: ordered tickets on branches from aegis/<EPIC-ID>. Run each ticket through the loop, merge each validated ticket into aegis/<EPIC-ID>, then validate the epic branch. human_gates: []
```

## Implement a ticket

For a ticket that already exists in `.aegis/tickets/`:

```text
Implement ticket <ID> per AGENTS.md: its own worktree and branch aegis/<ID>, only its allowed_areas, automatic validation, then the completion report.
```

## Validate

The loop validates on its own. Use this to re-check a ticket, or after you
changed something by hand:

```text
Start a fresh subagent that did not write this change and have it follow .claude/skills/validate/SKILL.md for ticket <ID>: worktree <path>, base ref <ref>, originating request "<issue text>", already-modified files <paths or none>. Report its verdict unchanged.
```

An epic branch after its tickets are merged:

```text
Start a fresh subagent and have it follow .claude/skills/validate/SKILL.md in epic mode for epic <EPIC-ID> on branch aegis/<EPIC-ID> against the default branch, with tickets <ID>, <ID>, ... Report its verdict unchanged.
```

## Ask for human gates

Validation is automatic unless you ask for a gate. In any prompt above,
replace `human_gates: []` with one of these lines, or put the matching label on the GitHub issue:
`aegis:gate-ticket` (you approve the ticket before work starts) or
`aegis:gate-merge` (you approve before the branch merges).

```text
human_gates: [ticket]
```

```text
human_gates: [merge]
```

```text
human_gates: [ticket, merge]
```

Some actions always stop for you, whatever the gates say: merging or pushing
to the default branch, deploys, migrations on shared data, secrets, and
deleting data, branches, or pushed history. The full list is under "Human
gates" in `AGENTS.md`.

## Update AEGIS from upstream

```text
Update AEGIS in this repo from https://github.com/TristanL567/aegis-core (branch main), as an AEGIS ticket. Clone it to a new, uniquely named temporary directory outside this repo and remove the clone afterwards. Replace only the <!-- aegis:begin --> ... <!-- aegis:end --> block in AGENTS.md and every skill folder from aegis-core's .claude/skills/ (replacing same-named ones), write the new commit SHA to .aegis/VERSION, and summarize which rules changed.
```

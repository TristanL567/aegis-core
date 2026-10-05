# AEGIS

Rules and tooling for agentic coding work a human can trust and review: every
change is scoped by a ticket, checked by an independent validator, and
traceable to a commit.

| File | Purpose |
| --- | --- |
| [`AGENTS.md`](AGENTS.md) | The rules agents follow: the loop, ticket format, scope and git rules, completion report. |
| [`.claude/agents/validator.md`](.claude/agents/validator.md) | Read-only reviewer that approves or blocks a ticket's changes. |
| [`.claude/skills/write-ticket/`](.claude/skills/write-ticket/SKILL.md) | Turns a request into a ticket, asking instead of guessing. |
| [`tools/check_scope.py`](tools/check_scope.py) | Checks changed files against a ticket's `allowed_areas` and `must_not_touch`. |
| [`hooks/`](hooks/) | Git hooks that enforce ticket scope and the commit subject format. |

## Use it in a project

1. **Rules.** Copy `AGENTS.md` to the project root. Claude Code and Codex read
   it directly; if the project already has a `CLAUDE.md`, add the line
   `@AGENTS.md` to it. To apply AEGIS to every project, use your user-level
   instructions instead (`~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`).
2. **Validator and skill.** Copy `.claude/agents/validator.md` and
   `.claude/skills/write-ticket/` into the project's `.claude/` directory, or
   into `~/.claude/` for every project.
3. **Git.** Add `.aegis/active-ticket` to the project's `.gitignore` and commit
   that change.
4. **Hooks.** Copy `hooks/pre-commit` and `hooks/commit-msg` into the project's
   `.git/hooks/`, make them executable, and set:
   - `AEGIS_CORE_ROOT`: path to this repository (default `../aegis-core`);
   - `AEGIS_PYTHON`: a Python with PyYAML installed (default `python3`; in Git
     Bash on Windows, for example `py -3.10`).

From then on every commit needs an active ticket. `pre-commit` rejects staged
files outside its scope, and `commit-msg` rejects subjects that don't match
`[ID] description` for the active ticket, with the description at 72 characters
or fewer. The hooks don't enforce one commit per ticket.

Tickets live in `.aegis/tickets/<ID>.yaml`, and the active ticket's ID is in
`.aegis/active-ticket`.

## Check scope by hand

Run from the project root:

```bash
python3 "$AEGIS_CORE_ROOT/tools/check_scope.py" --ticket .aegis/tickets/PROJ-012.yaml --staged
python3 "$AEGIS_CORE_ROOT/tools/check_scope.py" --ticket .aegis/tickets/PROJ-012.yaml --changed-file src/a.py
```

Exit 0 means every file is in scope, 1 lists the violations, and 2 means the
check itself failed, for example an unreadable ticket. A pattern ending in `/` matches a directory, any other
pattern must match exactly, and `must_not_touch` wins over `allowed_areas`.

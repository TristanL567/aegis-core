# Consider XY from aegis-core

Usage, in any repo: `Consider <XY> from aegis-core
https://github.com/TristanL567/aegis-core/blob/main/CONSIDER.md`

You were asked to "consider XY from aegis-core" in another repository, the
host. Adopt only XY, fitted into the host's own process. Don't install AEGIS
as a whole unless the human asks for that; the bootstrap prompt in
[`PROMPTS.md`](PROMPTS.md#bootstrap) does that.

## How to adopt one module

1. **Read the host's rules first:** `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING`,
   `.claude/`. They win over anything here: its branch rules, commit format,
   review process, names, and what agents may not do.
2. **Find XY in the table below** and read the files it lists in aegis-core.
   If XY is unclear, ask which module is meant.
3. **Map the names onto the host's.** An AEGIS *ticket* is whatever the host
   calls a unit of work (issue, story, task); the *validator* is the host's
   reviewer if it has one; `aegis/<ID>` branches and `[ID]` commit subjects
   follow the host's branch and commit rules.
4. **Adapt, don't copy.** Take only XY's files, rewritten in the host's names
   and style. If the host already has the same thing (a reviewer agent, a
   design document), extend that instead of adding a second one. Leave out
   any part that conflicts with the host's rules, and say what you left out
   and why.
5. **Show the diff** with a short list: what you adopted, what you changed,
   what you left out. By default, don't commit. Commit, push or open a pull
   request only when every host rule for them can be met; if one can't, for
   example a commit needs an issue number that doesn't exist yet, leave the
   change uncommitted and say what is needed.
6. **Note the source:** the aegis-core commit SHA, in the pull request or in
   a comment at the top of an adopted file.

## Modules

| XY | Files in aegis-core | What it adds | Needs | Fitting it into a host |
|---|---|---|---|---|
| tickets | `.claude/skills/write-ticket/` (with `.claude/skills/write-ticket/ticket-format.md`) | Each change scoped up front: goal, allowed paths, checkable criteria, verify commands, smoke steps; questions instead of guesses; a short form for one-sentence changes. | nothing | Put the fields into the host's issue template or work-item rules under its own names. |
| validator | `.claude/skills/validate/SKILL.md` | An independent, blocking review by a fresh subagent that reruns the checks itself and returns APPROVED, FIXES_REQUIRED or BLOCKED. | work items with checkable criteria and verify commands | Point it at the host's work item and test commands. If the host has a reviewer agent, add the missing checks to it. |
| hooks | `.claude/hooks/`, `.githooks/commit-msg`, `.githooks/post-commit`, the `hooks` entries in `.claude/settings.json`; install with `tools/install_hooks.py` | Edit/Write tool edits blocked outside the active ticket's paths (shell writes aren't guarded), no `git stash`, commits refused without an `[ID]` subject and a validator verdict, the active ticket cleared after its own commit. | tickets in `.aegis/tickets/`, the validator, `[ID]` commit subjects, Python | Run the script, don't copy by hand. If the host's commit or ticket format differs, don't install the commit gate; adopt the rules as text and say so. |
| session rules | `AGENTS.md`, section "Sessions" | One ticket per session, except an epic's tickets in sequence, each validated by a fresh subagent; a fresh session to implement a written plan; stop and restate the problem after two corrections; subagents for exploration. | nothing | Add the four lines to the host's rules file. |
| completion report | `AGENTS.md`, section "Completion report" | A short, checkable report: what changed, what was verified, what wasn't. | nothing | Use it as the host's pull-request or hand-over format. |
| design track | `.claude/skills/design-track/` | Design before code: personas, key tasks, up to three prototype rounds, a decision per finding, a frozen spec that becomes the build plan. | ux-test, a human for the gates | Run it as the host's planning or design work item. |
| ux-test | `.claude/skills/ux-test/`, `.claude/agents/ux-persona.md` | A usability inspection at phone and desktop width, with severity-rated findings; optional persona subagents. | a browser tool | Use it from the host's design or review step. |
| parity and DESIGN.md | `.claude/skills/design-track/DESIGN-template.md`; the "UI tickets" paragraphs in `write-ticket` and `validate`; `AGENTS.md`, section "Design work" | One design contract per product, and every UI change checked to work the same at phone and desktop width. | nothing; the design track to fill it in | Draft `DESIGN.md` from the host's real styles and screens; ask the human the open choices. Add the two parity checks to the host's work-item and review rules. |
| design presets | `.claude/skills/design-track/presets/` | Saved design conditions, such as euro formats or phone patterns for data portals. | a `DESIGN.md` | Copy the sections that fit into the host's `DESIGN.md`, list them under "Presets"; the host's own choices win. |

## Things to avoid

- Installing `AGENTS.md`, every skill, or the hooks when only one module was
  asked for.
- Renaming the host's concepts to AEGIS names (for example "ticket" where the
  host says "issue").
- Running two processes side by side, such as AEGIS tickets next to the
  host's issues.
- Committing or pushing when any host rule for it can't be met, such as a
  missing issue number in the branch name or commit subject.

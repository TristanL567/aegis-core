# "Consider XY from aegis-core": test (AEGIS-022)

Does an agent in another repo, the host, adopt only XY and fit it into the
host's own process?

## Setup (2026-10-22)

The host, "Kassabuch", is a scratch Flask/Jinja repo with its own rules in
`CLAUDE.md`:
- work items are GitHub issues, never "tickets";
- branches are `feature/<issue>-<slug>`, taken from `develop`;
- commit subjects end in `(#N)`;
- it has its own `reviewer` agent.

No issue exists, and the repo has no remote. The agents read a read-only
copy of aegis-core. Each run was a fresh Opus subagent given only the
human's line, plus "the human is not available; take your recommended
answer".

**What I checked on disk, not from the report** (`git diff`, untracked files,
commits):
- only XY was adopted, with no `AGENTS.md`, skills, hooks or `.aegis/`;
- "ticket" was not added to any host file;
- no commit broke the host's rules. Here that means no commit at all,
  because without an issue number no commit can follow the host's rules.

## Results

| Line typed | Runs | Only XY, host names | No rule-breaking commit |
|---|---|---|---|
| "Consider the validator from aegis-core `<repo>`" | h02, h04, h05 | 3 of 3 | 3 of 3 |
| "Consider the design presets from aegis-core `<repo>`", round 1 | h01, h03, h06 | 3 of 3 | 1 of 3 |
| same, after `CONSIDER.md` said to leave the change uncommitted | h07, h08, h09 | 3 of 3 | 2 of 3 |
| same, with "by default, don't commit" | h10, h11, h12 | 3 of 3 | 2 of 3 |
| "Consider the design presets from aegis-core `<path>/CONSIDER.md`" | h13, h14, h15 | 3 of 3 | 3 of 3 |

**Why some runs committed.** Asked afterwards, all four agents that committed
(h03, h06, h08, h10) said they had never opened `README.md` or
`CONSIDER.md`. They went from the repo path straight to the preset files and
decided to commit on their own. Every run that read `CONSIDER.md` followed
the host's rules.

**The decision.** The human chose to paste the link to `CONSIDER.md` itself,
not the repo root. `CONSIDER.md` and the README now show that usage. With
that link, the result was 3 of 3.

**Other things all runs did:**
- they extended the host's own `reviewer` agent instead of adding a second
  validator, and kept "issue";
- they left out parts that don't fit (the investment glossary, ticket-file
  checks, design and epic modes) and said why;
- they listed what they left out and what the maintainer still has to do.

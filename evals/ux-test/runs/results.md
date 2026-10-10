# ux-test A/B results (AEGIS-007)

Recorded on 2026-10-10. Every run used the same served copy of
`prototype/index.html`, the same baseline prompt (see `../baseline.md`), and
the same judge (`../judge.md`, Sonnet 5.5). Tokens are counted the harness's
way: each agent's final context size, summed over every agent in the run.

| Arm | Runs | Recall (of 10) | Unplanted | Invalid | Tokens, mean | Wall time |
|---|---|---|---|---|---|---|
| baseline: plain prompt | 3 | 8, 8, 10 (8.67) | 11.67 | 1.00 | 99,235 | 2–3 min |
| ux-test-full: coordinator + inspector + 3 persona subagents | 1 | 9 | 7 | 0 | 732,639 (7.4x) | 28 min |
| ux-test-personas: slim skill whose persona pass ran because the prompt said "personas" | 1 | 10 | 5 | 1 | 436,305 (4.4x) | 15 min |
| **ux-test: slim skill, inspection only** | **3** | **10, 10, 10** | **4.67** | **1.00** | **164,409 (1.66x)** | **4–10 min** |

## Against the AEGIS-007 bar

- **Every run finds at least 9 of 10: met.** The judge gave runs 2 and 3
  credit for F03 from "saving an empty form gives no feedback". A stricter
  reading, in which F03 is the silent wipe of entered data, scores those runs
  at 9. Either way the bar holds.
- **Mean invalid at most 1.00: met, at exactly 1.00.** The invalid findings
  were:
  - run 1: a loss labelled "Realised gain", which the judge called subjective;
  - run 3: the ⋯ menu not opening on a phone, which the tester flagged as a
    possible tool artefact, and the "Realised gain" item again.
- **Mean tokens at most 2x the baseline (198,470): met, at 164,409.**

## What changed between versions

- **Full version, run 1:** five subagents doing screenshot-heavy work. That
  rules it out at this cost bar, although its persona logs showed realistic
  give-ups that the plain prompt never produced.
- **Slim version:** the inspector became the default and personas became an
  explicit opt-in pass. The first slim run read "with 3 user personas" as
  that opt-in. The trigger now requires an explicit request for a persona
  pass or persona subagents; a request for "personas" alone maps findings to
  three named personas inside the inspection.
- **Gain over the baseline:** phone width was covered in every run, every
  finding carried a severity and a confirmed or opinion status, and fewer
  unplanted extras turned up. The cost was 1.66x the tokens and 2 to 3 times
  the wall time.

## ux-persona smoke check

Agent types load only when a session starts, so the human approved running
the check in a fresh `claude -p` session (Sonnet 5.5) in this worktree. That
session used Playwright MCP 0.0.83 (`npx`, `--isolated --browser chrome
--caps vision`) and `--strict-mcp-config`.

Session `c2dca409`, agent `a81ffa5367ae0111f`, `agentType: ux-persona`. Its
own transcript shows these calls, all to browser tools, none to file, search
or shell tools:

1. `browser_resize`
2. `browser_navigate`
3. `browser_take_screenshot`
4. `browser_click` (target `button "2024"`)
5. `browser_click` (target `text=2024`)
6. `browser_take_screenshot`

The outcome was Completed, with €126.15 for 2024.

When no tool on the list exists, as in a CLI session without a browser,
Claude Code refuses to start the agent rather than give it other tools.

**Caveat.** Playwright's `browser_click` targets elements by visible text or
role, not by screen position. The persona stays at screen level, but the
Playwright route is less strictly screenshot-only than the built-in
browser's coordinate clicks.

## Known issues

- **Judge YAML quoting.** The judge wrote one unquoted `why:` that began
  with a quote mark, in `ux-test/run1/matches.yaml`. Only the quoting was
  fixed. `judge.md` could ask for quoted strings; that file is outside
  AEGIS-007's scope.
- **Screenshot mapping at phone width.** In the built-in browser, mapping
  screenshots to coordinates at phone width becomes unreliable once a page
  overflows sideways. Testers fell back to the keyboard and flagged it.

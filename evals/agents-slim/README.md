# Slim AGENTS.md: regression test (AEGIS-021)

Does a shorter AGENTS.md still give the same ticket and validator behaviour?

- **Before:** 1,214 words. **After:** 849 words, 115 lines. The runs below
  used an 829-word version; the validator's fixes later restored a few rules
  word for word, and the runs were not repeated for that.
- The ticket format moved to `.claude/skills/write-ticket/ticket-format.md`.
- Rules that the AEGIS-020 hooks now enforce take one line each, plus a
  pointer to the hooks.
- New in the file: session rules and a short-ticket lane.

## Setup (2026-10-22)

There were 10 blind runs, each a fresh Opus subagent in its own scratch repo.
The repos were named `q01` to `q10` in shuffled order, and no prompt named
the variant.

- **Validator, 4 runs:**
  - 2 clean and 2 gap fixtures from `evals/ux-test/ui-parity-fixtures/`, with
    this branch's validate skill;
  - the same prompt as in AEGIS-017.
- **write-ticket on UI requests, 3 runs:**
  - repos copied from the fixture's `main`, with this branch's AGENTS.md and
    write-ticket and validate skills;
  - the three small UI requests from AEGIS-017.
- **Short tickets, 3 runs:**
  - the same repo setup, with "recieve" planted in README.md;
  - the request: "Fix the typo "recieve" in README.md."

## Results

| Check | Runs | Result |
|---|---|---|
| Clean fixture: APPROVED | q07, q10 | 2 of 2 |
| Gap fixture: FIXES_REQUIRED (`.last-div { display: none; }` at phone width) | q04, q09 | 2 of 2 |
| Validator output starts with the new `Ticket: UI-001` line | all 4 | 4 of 4 |
| UI ticket complete (id, goal, context, scope, non_goals, criteria, verify, smoke) | q03, q06, q08 | 3 of 3 |
| ... with parity at 390x844 and 1440x900, glossary labels, smoke at both widths | q03, q06, q08 | 3 of 3 |
| One-sentence request gets a short ticket | q01, q02, q05 | 3 of 3 |
| ... again, after the format file's example was changed to an unrelated one | s01, s02, s03 | 3 of 3 |

**Notes**
- **q06 (total row):** it writes parity as a criterion for each width plus
  "same information as desktop", not in the generic phrasing.
- **q03 (sort):** again it noticed that the table header is hidden on phones,
  and asked for a visible sort button above the cards.
- **Short tickets:** all six left out context, epic, depends_on,
  must_not_touch, smoke and manual_checks. None kept to one criterion:
  - each had 2 or 3 criteria, so that deleting the line or touching other
    files would not pass;
  - four added `non_goals`.

  In the first round (q01, q02, q05), the format file's short example was
  this very typo fix, and all three copied its goal word for word. The
  validator flagged that, so the example now links a footer to a privacy
  page. Run again (s01-s03), the result is the same: 3 of 3 short tickets.

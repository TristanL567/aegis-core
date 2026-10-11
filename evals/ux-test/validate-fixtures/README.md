# Fixtures for validate's design mode

These fixtures are two design tickets for DES-001, a dividend calendar for
Austrian stocks. They are identical except for one deliberate flaw:

- **`complete/`** is a passing round. Its findings are:
  - U01: at phone width the month buttons wrap onto two rows (severity 2,
    accepted);
  - U02: the gross amount is easy to miss (severity 1, an opinion, deferred).
- **`undecided/`** adds three things:
  - a phone-width rule that hides the net amount;
  - finding U03, a confirmed severity-3 finding with no decision;
  - T2 marked "not met" at phone width in the test report.

The two fixtures share their text, which comes from a single source. Their
whole diff is the CSS rule, U03, and one cell of the report.

## Run

```bash
py -3.10 evals/ux-test/validate-fixtures/make_repo.py evals/ux-test/validate-fixtures/complete <new temp dir>
```

The script builds a throwaway repo:

- `main` holds stand-in product code and this repo's validate skill.
- `aegis/DES-001` adds the fixture's design files.
- `aegis/DES-001-prototype` holds the prototype. It is never on the ticket
  branch.

Start a fresh subagent that follows `.claude/skills/validate/SKILL.md` for
DES-001 in that repo, with base ref `main`. Give it a neutral directory name,
and don't tell it which fixture it has.

## Results (2026-10-11, AEGIS-011)

Three fresh blind validators ran on each fixture, one at a time, using the
validate skill from AEGIS-009.

| Run | Fixture | Expected | Verdict | Blocking evidence |
|---|---|---|---|---|
| r1 | complete | APPROVED | APPROVED | none. U01 and U02 reproduced; opens on the current month; net = gross x 0.725 |
| r2 | undecided | FIXES_REQUIRED | FIXES_REQUIRED | U03 undecided; T2 not met at 390x844 (`.net` display:none reproduced) |
| r3 | complete | APPROVED | APPROVED | none |
| r4 | undecided | FIXES_REQUIRED | FIXES_REQUIRED | U03 undecided; T2 not met at phone |
| r5 | complete | APPROVED | APPROVED | none |
| r6 | undecided | FIXES_REQUIRED | FIXES_REQUIRED | U03 undecided; T2 not met at phone |

**Recurring non-blocking notes on `complete`:**

- amounts appear as "€61.05" rather than the Austrian format "61,05 €";
- the spec gives no rounding rule for KESt;
- the fake data has few edge cases;
- the loading and error states are specified but not prototyped.

None of these affected a verdict.

**History.** Under AEGIS-009, an earlier version of `complete` drew one
FIXES_REQUIRED from a strict validator. Two things had not been designed:

- foreign withholding tax;
- the month range, which came from the fake data rather than a product
  decision.

AEGIS-011 made non-Austrian securities and coupons explicit non-goals. The
calendar now opens on the current month and covers every month and year.

# Fixtures for validate's design mode

These fixtures are two design tickets (DES-001, a dividend calendar). They
are identical except for one thing:

- **`complete/`** is a passing round. Its findings are U01 (severity 2) and
  U02 (severity 1, opinion), and both have decisions.
- **`undecided/`** has the same files, plus a phone-width flaw in the
  prototype: the net amount is hidden. It also has U03, a confirmed severity
  3 finding with no decision.

## Run

```bash
py -3.10 evals/ux-test/validate-fixtures/make_repo.py evals/ux-test/validate-fixtures/complete <new temp dir>
```

The script builds a throwaway repo:
- `main` holds stand-in product code and this repo's validate skill.
- `aegis/DES-001` adds the fixture's design files.
- `aegis/DES-001-prototype` holds the prototype, which is never on the
  ticket branch.

Start a fresh subagent that follows `.claude/skills/validate/SKILL.md` for
DES-001 in that repo, with base ref `main`. Don't tell it which fixture it
has.

## Results (2026-10-11, AEGIS-009)

| Fixture | Expected | Verdict | Key evidence |
|---|---|---|---|
| complete | APPROVED | APPROVED | Every finding had a decision, and the pass rule held. The prototype was found only on the prototype branch. U01 and U02 were reproduced on a served copy at 390 and 1440 px. |
| undecided | FIXES_REQUIRED | FIXES_REQUIRED | Two blocking findings: U03 has no decision, and T2 is not met at phone width. The hidden net amount was reproduced at 390x844 and traced to the `.net { display: none }` media query. |

These verdicts come from the third pair of runs. Each fixture was run once
in each of three pairs, and only the third pair is shown.

1. **First pair.** Run with the earlier skill. Both verdicts were as
   expected.
2. **Second pair.** The skill had gained two checks: prototype isolation,
   and "every task met", not just "covered". The verdicts were again as
   expected, but an independent rerun of `complete` came back
   FIXES_REQUIRED, because its data was inconsistent:
   - a manual check asked for a monthly net total that the design never
     specifies;
   - the spec listed 12 months, but the prototype showed 6;
   - one net figure was wrong.
3. **Third pair.** The fixtures were made consistent: per-payment net,
   January to June 2025 in both the spec and the prototype, Austrian
   securities only, and net = gross × 0.725. Both verdicts were as
   expected.

The remaining non-blocking notes ask the human to confirm, at the merge
gate, the fixed 2025 range and the Austrian-only scope.

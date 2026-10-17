# AEGIS-015 A/B results: parity check in ux-test

Recorded 2026-10-17. Each arm made 3 runs on the parity test bed, using the
fixed prompt (`../prompt.md`) on a served copy, with Opus 5.5 as tester.
Findings were judged blind by Sonnet 5.5 under neutral IDs, following
`../../judge.md` with `gaps.yaml` as the key. Raw runs are in `../runs/floor/`
and `../runs/procedure/`.

| Arm | Words added | Recall per run | Mean recall | Invalid (mean) | Tokens (mean) |
|---|---|---|---|---|---|
| baseline: current ux-test (AEGIS-014) | 0 | 6, 7, 7 | 6.67 | 1.33 | 119,359 |
| floor: excerpt from ui-ux-pro-max@56ea9cf | 158 | 9, 9, 9 | 9.00 | **0.00** | 125,558 (1.05x) |
| procedure: our own parity procedure | 111 | **10, 10, 10** | **10.00** | 2.00 | 127,926 (1.07x) |

## Against the bar

The bar has three parts: every run finds at least 9 of 10, mean invalid is no
higher than 1.33, and tokens are at most 1.5x the baseline. A passing arm
must also find at least 9 of 10 flaws, with at most 2 invalid, in one run on
the original test bed.

- **floor**
  - Parity bar: met.
  - Regression: **failed**. One run on `evals/ux-test/` found **8 of 10**
    with 0 invalid. It reported F01 (the icon-only save) only inside its
    "unlabelled ⋯ menu" finding, which was credited as F07. Its finding
    "saving an empty form does nothing" touches F03, but the judge credited
    it to F02 together with the vague error message, so F03 went uncredited.
  - Raw run: `floor/regression/run1/`.
- **procedure**
  - Every run found all 10 gaps.
  - Invalid bar: **failed** at a mean of 2.00. None of the invalid findings
    is a wrong parity claim. They are:
    - "data lost on reload" in a prototype (3 times);
    - two opinions about silent merges;
    - one colour note that the tester itself called fine.
  - Not run on the original test bed, because it already failed the parity
    bar.

Under the ticket's rule, ux-test stayed unchanged at this point and the human
had to decide.

## Human decision and re-test: procedure-v2 (adopted)

The human chose "Fix procedure, re-test". **procedure-v2** is the procedure
arm plus one sentence, placed beside the scaffolding rule: "Limits of a
throwaway prototype, such as data that isn't saved or a download shown as a
preview, are notes, not findings." That makes 133 added words. It was
re-tested with the same prompt, tester and blind judging.

| Arm | Words added | Recall per run | Invalid (mean) | Tokens (mean) | Original test bed |
|---|---|---|---|---|---|
| procedure-v2 | 133 | **10, 10, 10** | **0.00** | 127,926 (1.07x) | **10/10, 1 invalid** (194,022 tokens) |

**procedure-v2 meets every part of the bar**, and is now
`.claude/skills/ux-test/SKILL.md`, the same words as `procedure-v2/SKILL.md`
with one line rewrapped. Raw runs are in `../runs/procedure-v2/` and
`procedure-v2/regression/`.

**Remaining caveat.** The original-bed run cost 194k tokens. The earlier
slim ux-test averaged 164k, so this run cost 1.18 times as much. That fits
the parity check's extra comparison, but it is one run only.

## Judging note

The AEGIS-015 judges were told to label a pure repeat of a planted gap with
that gap's id. The baseline judges had no such rule. This was corrected after
validation; an earlier version of this note wrongly claimed the baseline's
invalids were repeats.

- **Baseline invalids.** Read from the matches files, the four are:
  - run1 #8, an opinion that a merge is silent;
  - run2 #10, a wrong claim that an empty save gives no error;
  - run3 #11, an opinion about the year selector that partly repeats
    another finding;
  - run3 #14, an opinion about the price timestamp.

  So they are mostly opinions and wrong claims, not repeats. The baseline's
  1.33 stands.
- **Inconsistent labels.** Judges labelled the same claim differently
  across runs. "The report opens on 2025 and the selector is easy to miss"
  is invalid in baseline run3 #11, F09 in procedure-v2 run2 #16, and
  unplanted in procedure-v2 run3 #14.
- **Strict reading.** Under the baseline judges' stricter treatment of
  repeated opinions, procedure-v2's mean invalid would be about 0.67, still
  under the 1.33 bar. Recall is unaffected either way.

## Why the two arms behave differently

- **floor** names the touch rules, and the touch gaps (F06 and F07) were
  then caught in all 3 runs, against 0 in the baseline. It still merges
  findings by cause: gain and total were reported together in every run.
- **procedure** compares the phone view against the desktop view item by
  item, and reports each item as a separate finding. That raised recall to
  10, but also made testers more thorough in general, which brings more
  opinion noise.

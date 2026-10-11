# Parity baseline: the current ux-test skill

Recorded on 2026-10-11 for AEGIS-014. A parity mode for ux-test (AEGIS-015)
has to beat this bar on the same page, with the same prompt and the same
judge.

## Protocol

- **Page.** `prototype/index.html` is an EasyRep-style holdings and tax-report
  page. It works at 1440x900. At 390x844 it hides the 10 gaps listed in
  `gaps.yaml`.
- **Serving.** For each run, the page was copied to a temp directory outside
  the repo and served with `py -3.10 -m http.server` on a free port bound to
  127.0.0.1.
- **Tester.** Each run used a fresh general-purpose subagent on Opus 5.5 with
  the fixed prompt in `prompt.md`. It used the ux-test skill as of `main`
  2106759 and drove Claude's built-in browser in its own tab. Runs went one
  after another.
- **Judge.** Each run got a fresh Sonnet 5.5 subagent following `../judge.md`.
  It read `gaps.yaml` in place of `flaws.yaml` and this page in place of the
  original prototype.
- **Score.**
  `py -3.10 evals/ux-test/parity/grade.py --summary evals/ux-test/parity/runs/`.
  This wrapper runs the shared `../grade.py` with `gaps.yaml` as the answer
  key.

## Results

These results are on the fixed page (see History below).

| Run | Recall (of 10) | Missed | Unplanted | Invalid | Tester tokens |
|---|---|---|---|---|---|
| 1 | 6 | F02, F04, F06, F07 | 1 | 1 | 116,976 |
| 2 | 7 | F02, F06, F07 | 4 | 1 | 128,288 |
| 3 | 7 | F03, F06, F07 | 5 | 2 | 112,812 |
| **Mean** | **6.67** | | **3.33** | **1.33** | **119,359** |

Judge tokens (about 68k per run) are excluded.

## Reading

**What the current skill already finds.** Every run caught the following:

- the missing export (F01);
- the hidden year selector (F09);
- the clipped tax table (F08);
- the covered last row (F10);
- the renamed screen (F05).

**What no run caught.** The two touch and input gaps were missed in every
run:

- the 28 px "+" tap target (F06);
- the text keyboard for number fields (F07).

**Merged findings.** Every run reported the dropped gain column (F02) and the
dropped total (F03) as one finding, and run 1 merged the hover-only tooltip
(F04) with the clipped table (F08). A merged finding is credited to one gap
only. That is the realistic cost of not comparing views item by item.

**Bar for AEGIS-015.** The human chose a consistency bar, recorded in the
AEGIS-015 ticket:

- every run must find at least 9 of 10 gaps;
- mean invalid findings must be no higher than this baseline's 1.33.

There is clear headroom, from 6.67 now to 9 in every run.

## History

The first baseline (`superseded/baseline-v1/`) scored 7, 9 and 8 (mean 8.0).
It ran on a version of the page with two real desktop bugs:

- a new holding was valued at its purchase price and duplicated;
- the withheld headline didn't match its column.

The AEGIS-014 validator flagged both bugs, and the human chose to fix them
and re-run. Those bugs made testers inspect the add flow and the tax figures
more closely, which probably raised the earlier scores.

One run before that was discarded. In it, F04 used a CSS `:hover` popover,
which the phone emulator opens on a tap. F04 is now a native `title`
tooltip, which phones never show.

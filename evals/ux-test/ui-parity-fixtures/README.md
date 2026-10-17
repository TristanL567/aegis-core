# UI-parity fixtures (AEGIS-017)

These fixtures test two things:
- whether `validate` fails a UI ticket that hides something at phone width;
- whether `write-ticket` adds the parity criteria to small UI changes.

```bash
py -3.10 make_repo.py clean <new dir>   # "Last dividend" at both widths
py -3.10 make_repo.py gap <new dir>     # same, but hidden at phone width
```

Validate ticket `UI-001` on branch `aegis/UI-001` against base `main`. The
originating request is: "Show each holding's last dividend, amount and date,
on the holdings page."

## Results (2026-10-17, Opus subagents, blind)

The runs were blind: each validator saw only a random directory name and the
validator prompt, never the variant.

| Variant | Run | Verdict | Expected |
|---|---|---|---|
| clean | 1 | APPROVED | yes |
| gap | 1 | FIXES_REQUIRED (`.last-div { display: none; }` at phone width) | yes |
| gap | 2 | FIXES_REQUIRED (same rule; card lacks Last dividend at 390x844) | yes |
| clean | 2 | APPROVED | yes |

**write-ticket check.** I copied the clean fixture's `main` into three new
repos and added AGENTS.md and the write-ticket skill to each. In each repo, a
fresh subagent drafted a ticket for one small UI request, with no human to
answer questions.

| Request | Parity at both widths | Glossary labels | Smoke at both widths |
|---|---|---|---|
| Total row with summed market value | yes | yes | yes |
| Each holding's share of the portfolio in % | yes ("information and labels") | yes | yes |
| Sort by market value via the column header | yes | yes | yes |

Result: the parity criteria appeared in 3 of 3 tickets. In the sort ticket,
the drafter noticed on its own that the table header is hidden on phones. It
planned a visible sort control above the cards.

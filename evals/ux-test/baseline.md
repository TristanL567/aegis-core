# UX-test baseline: plain prompt

Recorded 2026-10-10 for AEGIS-006. This is the bar that the `ux-test` skill
(AEGIS-007) has to beat on the same prototype, the same prompt, and the same
judge.

## Protocol

- **Prototype.** `prototype/index.html` was copied to a temp directory
  outside the repo, which held only that file. It was served with
  `py -3.10 -m http.server` on a free port bound to 127.0.0.1.
- **Tester.** Each run used a fresh `general-purpose` subagent on Opus 5.5,
  with Claude's built-in browser tools, in a tab of its own. The prompt is
  below, with only the port varying. The runs were sequential. The tester was
  told not to touch files or the shell. Run 1's transcript was checked: it
  used browser tools only. Runs 2 and 3 reported the same.
- **Judge.** A fresh Sonnet 5.5 subagent per run, using `judge.md`, saw the
  findings, `flaws.yaml` and the prototype source. Run 1's matches were
  checked by hand and agree with the key.
- **Score.** `py -3.10 grade.py --summary runs/`.

```text
Run usability tests on this prototype with 3 user personas.

Prototype: http://127.0.0.1:<port>/ - "Taxbook", a web app for private
investors to track their capital income and prepare their tax return.
Key tasks:
- T1: add a dividend you received: 12 March 2025, Vanguard FTSE All-World,
  EUR 84.20, withholding tax EUR 12.63.
- T2: find your taxable income for tax year 2024.
- T3: export the 2025 tax report as CSV.

Use the built-in browser tools (mcp__Claude_Browser__*). Open your own new
tab with tabs_create, navigate it to the prototype, and pass its tabId on
every browser call; never touch other tabs. Test only the app as served in
the browser: do not read, search or list any files and do not run shell
commands. Close your tab when done.

End your reply with every usability problem you found as a numbered list,
one problem per item.
```

## Results

| Run | Recall (of 10) | Missed | Unplanted | Invalid | Tester tokens |
|---|---|---|---|---|---|
| 1 | 8 | F09, F10 (phone width not tested) | 9 | 0 | 89,086 |
| 2 | 8 | F09, F10 (phone width not tested) | 11 | 0 | 106,721 |
| 3 | 10 | none | 15 | 3 | 101,898 |
| **Mean** | **8.67** | | **11.67** | **1.00** | **99,235** |

Judge tokens, which are excluded from the table, ran at about 67k to 72k per
run.

## Reading

- **A plain Opus prompt is already a strong tester.** It found every
  desktop flaw in every run, and invented almost nothing.
- **Its weakness is consistency.** Two of the three runs never tested phone
  width, and the run that did produced all three invalid findings.
- **The bar cannot be met.** With a mean recall of 8.67 of 10, AEGIS-007's
  criterion of "baseline + 2 flaws" would need a mean of 10.67, which is
  impossible. Before AEGIS-007 starts, the human must either change that
  criterion or ask for a harder test bed.

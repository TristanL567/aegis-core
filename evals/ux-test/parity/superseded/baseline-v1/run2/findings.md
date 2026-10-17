# Parity baseline run 2 (current ux-test skill)

The tester was a fresh Opus 5.5 subagent given the fixed prompt in `../../../prompt.md`. It read only the skill file. Because screenshots often timed out, it checked layout through page geometry. Every action was a real click, typed text or key press.
- Harness tokens: 124,877. Tool uses: 74. Time: about 5.5 minutes.
- Coverage gaps: none.

1. (sev 4, confirmed) On a phone the Tax year selector is hidden and the report silently shows 2025, so the KESt still due for 2024 can't be found.
2. (sev 4, confirmed) On a phone the Export CSV button is hidden, so exporting is impossible.
3. (sev 4, confirmed) On a phone the Holdings list has no total value, no gain and no column labels.
4. (sev 4, confirmed) An added holding is lost when the page reloads. This may be a prototype limitation.
5. (sev 3, confirmed) A new lot is valued at its purchase price, not today's close, so its gain shows €0.00 and the total is understated. It also appears as a separate, duplicate "Erste Group" row.
6. (sev 3, confirmed) The KESt explanation is only a hover tooltip on an "i" that can't be focused or tapped, so touch and keyboard users can't reach it.
7. (sev 3, confirmed) On a phone the tax table is clipped with no scroll, so the Foreign tax, KESt, Withheld and Due columns can't be reached.
8. (sev 3, confirmed) On a phone the fixed bottom nav permanently covers the last holding's value, the "Prices as of" note and the "Added ..." confirmation.
9. (sev 2, confirmed) Escape doesn't close the Add holding dialog.
10. (sev 2, confirmed) Enter doesn't submit the Add holding form.
11. (sev 2, confirmed) Focus escapes the open dialog to the page behind it.
12. (sev 2, confirmed) Validation shows one error at a time, not attached to its field. The field isn't marked and the error isn't announced.
13. (sev 2, confirmed) On a phone the "+" add button has no accessible name and is a 28x28 px tap target.
14. (sev 2, confirmed) The same screen is called "Statements" on a phone and "Tax report" on desktop.
15. (sev 2, opinion) The CSV pairs ";" separators with "." decimals, which German-locale Excel may misread.
16. (sev 1, confirmed) On a phone the Shares and Price fields open a text keyboard.

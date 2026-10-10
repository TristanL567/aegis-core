# Slim ux-test run 3 findings

Tester: a fresh Opus 5.5 subagent given the baseline prompt plus "use the ux-test skill". It ran the inspection only, with no persona pass. It used browser tools only, plus one JavaScript read of which element had focus. It noted that phone-mode coordinate mapping was flaky after the Report page overflowed.
Tokens: 188,620 (harness). Wall time about 9.5 minutes.

1. U01 (sev 4, confirmed): On phone, the bottom nav covers Save and Cancel in Add transaction, so T1 can't be completed by touch.
2. U04 (sev 4, confirmed, with a tool caveat): On phone, tapping ⋯ on the Tax report doesn't open the Export menu.
3. U05 (sev 4, confirmed): On phone, the Export dialog's Create file and Continue buttons sit under the bottom nav.
4. U02 (sev 3, confirmed): The Date placeholder says YYYY-MM-DD, but that format is rejected with a vague "Invalid input." that names no field. Only dd.mm.yyyy works.
5. U03 (sev 3, confirmed): The primary "Continue" button in Export closes the dialog and creates nothing. Only the small "Create file" link works.
6. U06 (sev 3, confirmed): A saved transaction doesn't appear in the list until you switch year or tab, and there's no success message, which invites duplicate entries.
7. U07 (sev 3, confirmed): On phone, the Report amounts overflow the card, the page scrolls sideways and the bottom nav moves off-screen. The Transactions table hides the Type, Withholding tax and Amount columns.
8. U08 (sev 2, confirmed): Saving an empty Add transaction form gives no feedback.
9. U09 (sev 2, confirmed): Escape doesn't close the Add dialog, the Export dialog or the ⋯ menu, and the Export dialog has no Cancel.
10. U10 (sev 2, opinion): The Save button is an unlabelled 💾 emoji.
11. U11 (sev 2, opinion): Export is hidden behind an unlabelled ⋯, and the Export dialog doesn't show which tax year it exports.
12. U12 (sev 2, confirmed): The same figure is "Taxable income" on Overview and "Assessment base" on Report.
13. U13 (sev 2, confirmed): The selected tax year is shown only by a faint grey fill.
14. U14 (sev 1, confirmed): At desktop width, the open ⋯ menu covers the Assessment base value.
15. U15 (sev 1, opinion): A loss is labelled "Realised gain" with a negative amount.
16. U16 (sev 1, opinion): The exported CSV isn't sorted by date, and "File created" shows only on-page text with no visible download.

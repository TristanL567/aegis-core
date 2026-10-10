# Slim ux-test run 2 findings

The tester was a fresh Opus 5.5 subagent given the baseline prompt plus "use the ux-test skill". It ran the inspection only, with no persona pass. It used browser tools only; it used form_input once, discarded that run and redid it by keyboard.
Tokens: 173,392 (harness). Wall time about 5.6 minutes.

1. (4, confirmed) On phone, the bottom nav covers the Cancel and save buttons in the Add transaction dialog, and the dialog doesn't scroll, so you can't save by touch.
2. (4, confirmed) On phone, the bottom nav covers the "Create file"/"Continue" buttons in the Export dialog, so you can't export by touch.
3. (4, confirmed) The Date field rejects the format its own placeholder shows (YYYY-MM-DD) with "Invalid input." and accepts only DD.MM.YYYY.
4. (4, confirmed) A saved transaction doesn't appear in the Transactions list until you switch views. The save looks like it failed, which led to a duplicate entry that inflated taxable income.
5. (4, confirmed; may be prototype scope) Added transactions are lost when the page reloads.
6. (3, confirmed) The error "Invalid input." names no field or format, and saving an empty form gives no feedback at all.
7. (3, confirmed) In the Export dialog, the primary "Continue" button closes it without exporting and without feedback. The real action is the faint "Create file" link.
8. (3, confirmed) On phone, the Transactions table is clipped after the Security column, so Type, Withholding tax and Amount can't be seen or scrolled to.
9. (2, confirmed) Escape doesn't close the Add transaction or Export dialogs, and the Export dialog has no Cancel.
10. (2, opinion) The save button is an unlabelled 💾 icon.
11. (2, confirmed) The same figure is called "Taxable income" on Overview and "Assessment base" on Report.
12. (2, confirmed) A loss is labelled "Realised gain" with a negative amount (OMV AG, −€84.25).
13. (2, opinion) Export is hidden behind an unlabelled "⋯" menu.
14. (2, confirmed) On phone, the report table overflows its card: the amounts sit outside it and the page scrolls sideways.
15. (2, opinion) The selected tax year is shown only by a faint background tint.
16. (2, opinion) The exported CSV has only raw transactions and no report totals, and the new row is out of date order.

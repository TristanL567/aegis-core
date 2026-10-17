1. (sev 4, confirmed) On phone, the bottom nav covers the Add transaction save button. Tapping it opens Report instead and nothing is saved, so T1 can't be completed.
2. (sev 4, confirmed) On phone, the bottom nav covers the Export dialog's "Create file" button, so T3 can't be completed.
3. (sev 4, confirmed) Saving a dotted date with a decimal-point amount (12.03.2025 / 84.20) wipes every field, shows no error and saves nothing, so the input is lost.
4. (sev 3, confirmed) The date placeholder says YYYY-MM-DD, but the form rejects that format and decimal points. Only DD.MM.YYYY with decimal commas is accepted, and nothing on screen says so.
5. (sev 3, confirmed) The primary "Continue" button in the Export dialog closes it without exporting. The real export is a small link-styled "Create file".
6. (sev 3, confirmed) After a successful save, the new transaction doesn't appear and no confirmation shows until the year is switched.
7. (sev 3, confirmed) On phone the Export dialog can't be left: Continue is covered, there is no close button and Escape does nothing. Only a reload gets out.
8. (sev 3, confirmed) On phone the bottom nav covers Add transaction's Cancel button, and Enter and Escape do nothing, so the dialog can't be submitted or left.
9. (sev 3, confirmed) On phone the Transactions table has no Amount column and doesn't scroll sideways.
10. (sev 3, confirmed) On phone the Transactions table has no Withholding tax column.
11. (sev 2, confirmed) On phone the Transactions table has no Type column.
12. (sev 2, confirmed) On phone the Tax report's Assessment base value is clipped off-screen and can only be reached by scrolling the whole page sideways.
13. (sev 2, confirmed) On phone the Tax report's Withholding tax credited value is clipped off-screen.
14. (sev 2, confirmed) On phone the Tax report's Tax due value is clipped off-screen.
15. (sev 2, confirmed) On phone the Report screen overflows sideways, pushing the bottom nav out of view and the Report tab off-screen.
16. (sev 2, confirmed) On phone the Export dialog is wider than the screen and the Format select is cut off.
17. (sev 2, confirmed) The "Invalid input." message doesn't name the field or the expected format.
18. (sev 2, confirmed) Saving an empty Add transaction form does nothing: no message and no field marked.
19. (sev 2, confirmed) Escape doesn't close the ⋯ menu or the Export dialog, and focus doesn't move into the dialog when it opens.
20. (sev 2, confirmed) The same figure is called "Taxable income" on Overview and "Assessment base" on Report.
21. (sev 2, confirmed) The selected tax year is shown only by a faint background tint, and no heading names the year.
22. (sev 2, confirmed) Several tap targets are under 44 px: nav buttons are 40 px tall, year buttons 60x38, Create file 67x23 and ⋯ about 40x34.
23. (sev 2, opinion) The save button is an unlabelled 💾 icon.
24. (sev 2, opinion) Export is hidden behind an unlabelled ⋯ menu, and the Export dialog doesn't say which year it exports.
25. (sev 2, opinion) The "tax report" CSV contains only transactions, not the report's assessment base, credited withholding or tax due.
26. (sev 2, opinion) For 2024, credited withholding (€50.56) exceeds the 27.5% tax (€34.69), which may overstate the creditable amount.
27. (sev 1, confirmed) Input formats (DD.MM.YYYY, decimal comma) differ from the formats shown everywhere else (YYYY-MM-DD, decimal point).
28. (sev 1, confirmed) In the exported CSV the new transaction comes last instead of in date order.

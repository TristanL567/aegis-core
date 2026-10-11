# Baseline run 3 findings

Tester: fresh Opus 5.5 subagent, plain prompt. Browser tools only; no file or shell tools.
Personas:
- P1, a retired phone user, tested at narrow width (about 310 px);
- P2, a keyboard-first engineer on desktop at 1280x800;
- P3, a screen-reader user, tested through the accessibility tree and markup.

1. On the narrow/mobile layout, the bottom navigation bar covers the Cancel and Save buttons in the Add transaction dialog, so they can't be tapped. Tapping them switches tabs instead.
2. The same overlap hides the "Create file" and "Continue" buttons in the Export dialog on mobile.
3. The mobile layout scrolls horizontally. The "Add transaction" button is clipped at the right edge, and the transactions table shows only Date and a truncated Security column; Type, Withholding tax and Amount are off-screen.
4. On mobile, the Tax report values (Assessment base, Withholding tax credited, Tax due) are clipped at the right edge and not visible.
5. The Save button is just a floppy-disk emoji with no text label. Its meaning is unclear, and screen readers announce it poorly.
6. Saving with invalid or missing input clears every field and shows no visible error. The "Invalid input." element stays hidden, so the user loses everything they typed and doesn't learn why.
7. Even when shown, "Invalid input." is generic: it doesn't say which field is wrong. There is no validation as you type and no message next to each field.
8. A successful save gives no confirmation: no message and no highlighted row.
9. A transaction dated in another year disappears from view after saving, because the year filter doesn't follow the date entered. It looks as if the entry was lost.
10. Pressing Enter in a form field doesn't submit the Add transaction form.
11. Neither Escape nor a click on the dimmed backdrop closes the Add transaction dialog.
12. On mobile the dialog takes over the screen, but the bottom navigation stays active, so tabs can change behind the open dialog.
13. The selected tax year is shown only by a faint grey background. The year buttons have no aria-pressed or similar state, so screen-reader users can't tell which year is active.
14. The Overview headings and figures never name the selected year (only "the selected tax year"), so it is easy to read off the wrong year in T2.
15. The terms differ between screens: Overview says "Taxable income" and Report says "Assessment base" for the same figure.
16. Export is hidden behind an unlabelled "⋯" overflow menu instead of being a visible action.
17. The Export dialog's primary button "Continue" silently closes the dialog without exporting anything.
18. The real export action, "Create file", is styled as a minor text link beside the primary button, so users pick the wrong one.
19. The Export dialog doesn't say which tax year will be exported.
20. "Create file" downloads nothing. It shows the CSV as text on the page while claiming "File created: tax-report-2025.csv", with no download or save link.
21. The exported CSV isn't sorted by date (a new entry comes last), and it has no totals or tax-due figures, unlike the report on screen.
22. The CSV mixes number conventions: semicolons as separators (European style) with dot decimals. Spreadsheets set to German or Austrian locale may misread the amounts.
23. After switching years, the previous export's CSV output stays on the Report page with no year label, so it could be mistaken for the current year's data.
24. The badges "T1", "T2" and "T3" on the cards are unexplained and mean nothing to users.
25. Transactions can't be opened, edited or deleted, so a mistaken entry can't be fixed.
26. The Date field accepts several formats, but only "YYYY-MM-DD" is hinted and there is no date picker. A date like 03/12/2025 is ambiguous, and the app doesn't show back how it read the date.
27. When withholding exceeds the tax owed (2024: tax due €0.00 against €50.56 withheld), the report shows €0.00 with no explanation of whether the excess is lost or can be reclaimed.
28. The table puts "Withholding tax" before "Amount", the reverse of the usual order, which invites misreading.
29. On mobile the Report table also overflows the card edge, so rows run off-screen to the right.

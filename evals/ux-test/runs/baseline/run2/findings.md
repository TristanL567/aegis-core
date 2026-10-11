# Baseline run 2 findings

Tester: a fresh Opus 5.5 subagent given the plain prompt. It used browser tools only and read the page's inline script from inside the browser. It did not test the mobile layout.
Personas:
- P1: first-time investor who types local formats.
- P2: experienced investor who types ISO dates and uses the keyboard.
- P3: keyboard and screen-reader user.

1. The Date placeholder says YYYY-MM-DD, but only DD.MM.YYYY is accepted, so following the placeholder always fails.
2. The error "Invalid input." doesn't say which field is wrong or what format is expected, and no field is highlighted.
3. Leaving the optional "Withholding tax" field empty and saving silently wipes the whole form without saving or explaining. Users lose their data.
4. After a successful save the Transactions list doesn't refresh, so the new row is hidden until you change tab or year. Users think the save failed and may enter the transaction again, creating duplicates.
5. A successful save shows no confirmation: no message and no highlighted new row. The dialog just closes, which looks the same as cancelling.
6. The save button is an icon only (💾), with no text, tooltip or aria-label. Screen readers announce it as "💾".
7. Pressing Enter in the add form doesn't submit it.
8. The error banner pushes the form down and moves the Save and Cancel buttons, so a repeated click can miss.
9. In the export dialog the primary "Continue" button closes the dialog without exporting. The action that actually exports is the small, low-emphasis "Create file" text button.
10. "Create file" doesn't download anything. It prints the CSV text on the page while claiming "File created: tax-report-2025.csv".
11. The exported output disappears when the tax year changes.
12. Export is hidden behind an unlabelled "⋯" menu with no aria-label or aria-expanded, and the open menu covers the Assessment base figure.
13. Escape doesn't close the "⋯" menu, and the export dialog has no Cancel or close button.
14. The export dialog doesn't say which tax year will be exported.
15. The selected tax year is shown only by a very faint grey background (#f3f4f6 on white), with no aria-pressed, so it is hard to tell which year is active.
16. The Overview, Transactions and Report headings never state the selected tax year, so users can't tell which year the figures belong to.
17. The same figure is called "Taxable income" on the Overview and "Assessment base" in the Report, so users can't tell they are the same.
18. The internal task markers "T1", "T2" and "T3" are visible in the UI next to the screen titles.
19. In the Transactions table, Withholding tax comes before Amount. That is the reverse of the form, the CSV and the normal reading order, so the two numbers are easy to mix up.
20. Transactions can't be edited or deleted, so a mistaken or duplicate entry can't be fixed.
21. The CSV export isn't sorted by date (a new entry comes last) and has no totals or tax-due rows, so it doesn't match the report on screen.

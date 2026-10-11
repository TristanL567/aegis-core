# Baseline run 1 findings

Tester: fresh Opus 5.5 subagent, plain prompt. 89,086 tokens, 41 tool uses, about 2 minutes.
Tools used: browser only (clicks, typing, screenshots, javascript_tool, read_page, get_page_text). No file or shell tools.
Personas: P1 retired, low tech confidence; P2 busy professional; P3 keyboard and screen-reader user.
Tester's note: the mobile layout was not tested, because viewport emulation rendered unreliably.

1. After saving a transaction there is no confirmation, and the view stays on the currently selected year. An entry dated in another year seems to vanish, which invites duplicate entries.
2. Invalid input silently clears every field. The "Invalid input." message is never shown, and nothing says which field is wrong or why.
3. The Save button is icon-only ("💾"), with no visible text and no accessible name. Its meaning is unclear next to the text button "Cancel".
4. The Date field's only hint is a "YYYY-MM-DD" placeholder, which disappears once you type. The field accepts DD.MM.YYYY, but nothing says so.
5. Pressing Enter in the Add transaction form does not submit it.
6. Escape does not close the Add transaction dialog, or the Export dialog.
7. Focus is not trapped in the modal dialogs: Tab moves to the page navigation behind the overlay.
8. The tax-year buttons show the selected year only by a faint grey background, with no aria-pressed or aria-current state. It is easy to miss which year is active, which drives problems 1 and 13.
9. The export action is hidden behind an unlabelled "⋯" overflow button, with no accessible name and no aria-expanded. Users looking for "Export" don't see it.
10. The open "⋯" menu covers the Assessment base amount.
11. In the export dialog the primary button "Continue" closes the dialog and does nothing, with no file and no feedback. The control that actually exports, "Create file", is styled as a small low-emphasis link.
12. "Create file" doesn't download anything. It only shows "File created: tax-report-2025.csv" with an on-page preview and no download or save link, so the user gets no file.
13. The export dialog doesn't say which tax year will be exported, and has no Cancel or close button.
14. Rows in the exported CSV aren't sorted by date: a newly added 2025-03-12 row comes last. The file contains only raw transactions, without the report figures (assessment base, withholding credited, tax due).
15. The same figure is called "Taxable income" on Overview and "Assessment base" in the Tax report, so users can't tell whether they are the same number.
16. The internal task markers "T1", "T2" and "T3" appear as badges in the UI headers. They mean nothing to users and look like controls.
17. The date input ignores the selected year. Adding a 2025 date from the 2024 view gives no warning that the entry belongs to a different year than the one being viewed.

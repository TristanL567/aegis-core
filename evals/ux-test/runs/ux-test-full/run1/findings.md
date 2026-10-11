# ux-test skill run 1 findings

Coordinator: a fresh Opus 5.5 subagent given the baseline prompt plus "use the ux-test skill". It read SKILL.md and started 5 general-purpose subagents: the inspector, P1 (whose first attempt failed because no browser pane was open), P1 again, P2 and P3.
Personas used only tabs, navigate, resize and computer, with no page-structure tools. The inspector also used get_page_text, read_page and find.
Tokens (harness metric, the sum of each agent's final context): 732,639. The total processed across all turns was about 77.8M. Wall time was about 28 minutes.
Barrier matrix (outcome / highest confusion rating):
- P1 (phone): T1 Abandoned / 5, T2 Completed / 1, T3 Abandoned / 5.
- P2 (desktop): T1 Abandoned / 4, though the entry was in fact saved; T2 Completed / 1; T3 Completed / 4.
- P3 (phone): T1 Abandoned / 5, T2 Completed / 2, T3 Abandoned / 4.

1. On a phone, the Save, Cancel and export buttons in the Add transaction dialog and in the Export sheet are hidden behind the bottom navigation and cannot be tapped. This blocked T1 and T3 on a phone. (Severity 4, confirmed)
2. The dialogs cannot be closed: Escape, the backdrop, the nav tabs and Back do nothing, and on a phone only a reload gets out. (Severity 3, confirmed)
3. The Date placeholder says YYYY-MM-DD, yet that format, slash dates and decimal commas are all rejected. The error is a generic "Invalid input." that names no field. (Severity 3, confirmed)
4. Saving with the optional withholding tax left empty silently clears the form and saves nothing. (Severity 3, confirmed)
5. A successful save gives no confirmation, and the new row does not appear in the Transactions list until the user switches tabs. (Severity 3, confirmed)
6. In the Export dialog, the primary "Continue" closes the dialog without exporting. The real action is a small, low-contrast "Create file" link, and the dialog does not show the year. (Severity 3, confirmed)
7. On a phone, the Report values overflow the card and force sideways scrolling, and the "⋯" menu and bottom nav end up off-screen or clipped. (Severity 3, confirmed)
8. On a phone, the Transactions table shows only Date and Security; Type, Withholding tax and Amount are unreachable. (Severity 2, confirmed)
9. Duplicate transactions are accepted without warning, and there is no way to edit or delete one. (Severity 2, confirmed)
10. Keyboard focus escapes the open dialog to the nav behind it, and Enter then changes the page underneath. (Severity 2, confirmed)
11. Export is hidden behind an unlabelled "⋯" overflow button. (Severity 2, synthetic)
12. The Save button is icon-only, with the accessible name "💾". (Severity 2, confirmed)
13. Added transactions are lost on page reload. (Severity 2, confirmed)
14. Pressing Enter in a form field does not submit the Add transaction form. (Severity 2, synthetic)
15. Export shows an in-page preview, but no file download was observed, and the result disappears when the year changes. (Severity 2, synthetic)
16. The selected tax year is shown only by a faint highlight. (Severity 1, synthetic)

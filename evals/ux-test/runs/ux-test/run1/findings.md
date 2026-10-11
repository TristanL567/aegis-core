# Slim ux-test run 1 findings

The tester was a fresh Opus 5.5 subagent given the baseline prompt plus "use the ux-test skill". It ran the inspection only, with no persona pass, and named 3 personas only to map findings to them.
- Tokens: 131,216 by the harness's count, about 7.6M processed in total.
- Wall time: about 3.6 minutes.
- Tools: browser only, plus javascript_tool twice to read focus and page width.

1. U01 (sev 4, confirmed) On a phone, the bottom nav covers the Save and Cancel buttons of the Add transaction dialog, so the transaction can't be saved by tapping.
2. U02 (sev 4, confirmed) On a phone, the bottom nav covers the Create file and Continue buttons of the Export dialog, so no CSV can be exported.
3. U03 (sev 4, confirmed) Saving with the optional Withholding tax field empty clears the form and saves nothing, with no message: data is silently lost.
4. U04 (sev 3, confirmed) The date placeholder says YYYY-MM-DD, but that format is rejected; only DD.MM.YYYY works.
5. U05 (sev 3, confirmed) The error "Invalid input." doesn't say which field is wrong.
6. U06 (sev 3, confirmed) In the Export dialog, the primary "Continue" does nothing, while the real action, "Create file", is a faint text link.
7. U07 (sev 3, confirmed) Saving a transaction gives no confirmation, and the list doesn't refresh until the year is switched.
8. U08 (sev 3, confirmed) On a phone the Transactions table cuts off Type, Withholding tax and Amount, and they can't be scrolled to.
9. U09 (sev 3, confirmed) Escape doesn't close the dialogs, the Export dialog has no Cancel, and on a phone the nav doesn't leave the dialog, so there is no visible way out on a phone.
10. U10 (sev 2, confirmed) On a phone the Report values overflow the card and widen the page.
11. U11 (sev 2, opinion) The Save button is an unlabelled floppy-disk icon.
12. U12 (sev 2, opinion) Export is hidden behind an unlabelled "⋯" menu.
13. U13 (sev 2, confirmed) The same figure is called "Taxable income" on Overview and "Assessment base" on Report.
14. U14 (sev 2, opinion) The selected tax year is shown only by a faint grey fill.
15. U15 (sev 1, opinion) A loss is labelled "Realised gain" with a negative amount.
16. U16 (sev 2, opinion) The Export dialog doesn't show which tax year will be exported.

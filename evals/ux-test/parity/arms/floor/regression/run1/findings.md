1. (sev 4, confirmed) On a phone, the bottom nav covers the Add transaction dialog's Cancel and save buttons. Tapping where save is opens Report instead, so T1 can't be completed.
2. (sev 4, confirmed) On a phone, the bottom nav covers the Export dialog's "Create file" and "Continue" buttons, so T3 can't be completed.
3. (sev 4, confirmed) The date field rejects the format its own placeholder shows (YYYY-MM-DD) with "Invalid input."; only DD.MM.YYYY is accepted.
4. (sev 3, confirmed) After a successful save, the Transactions list doesn't show the new row and there is no confirmation until the user switches tabs.
5. (sev 3, confirmed) The primary "Continue" button in the export dialog closes it without exporting and without any message; the action that works is the small "Create file" link.
6. (sev 3, confirmed) On a phone, the Report table overflows to 638px, so the figures are off-screen and the page scrolls sideways.
7. (sev 3, confirmed) On a phone, the Transactions table hides the Type, Withholding tax and Amount columns, and they can't be scrolled to.
8. (sev 2, confirmed) Validation feedback is a generic "Invalid input." that names no field, and saving an empty form silently does nothing.
9. (sev 2, confirmed) Escape and backdrop clicks don't close the dialogs, Enter doesn't submit the form, and the export dialog has no Cancel button.
10. (sev 2, confirmed) Export is hidden behind an unlabeled "⋯" menu, and the save button is an unlabeled 💾 icon.
11. (sev 2, confirmed) The selected tax year is shown only by a faint background colour, and neither the headings nor the export dialog name the year.
12. (sev 2, confirmed) The same figure is called "Taxable income" on Overview and "Assessment base" on Report.
13. (sev 2, confirmed) Phone touch targets are below 44px: year buttons are 38px tall, nav buttons 40px, and "Create file" 23px.
14. (sev 1, confirmed) The exported CSV isn't sorted by date; a new transaction is added at the end.

# Parity baseline run 3 (current ux-test skill)

A fresh Opus 5.5 subagent ran this with the fixed prompt in `../../../prompt.md`. It read only the skill file and used read-only page scripts for its measurements.
- **Cost:** 129,167 harness tokens, 65 tool uses, about 6.2 minutes.
- **Gap:** the tester did not click Export CSV on desktop, because it assumed the button starts a download (it shows an on-page preview).

1. (sev 4, confirmed) Export CSV is hidden at phone width, so T4 can't be done on a phone.
2. (sev 4, confirmed) On a phone the tax-year selector is hidden and no year is shown, so phone users see the 2025 KESt (€120.13) instead of 2024's (€8.10).
3. (sev 4, confirmed) The phone Holdings view has no portfolio total and no gains, and shows shares, price and value as unlabelled numbers.
4. (sev 3, confirmed) A newly added holding is valued at its purchase price (gain €0.00), not today's close, and appears as a duplicate Erste Group row.
5. (sev 3, confirmed) Holdings can't be edited or deleted, so a wrong or duplicate entry can't be undone.
6. (sev 3, confirmed) On a phone the tax table is clipped to Security, Type and Gross; the Foreign tax, KESt, Withheld and Due columns can't be reached.
7. (sev 3, confirmed) The KESt explanation is only a hover tooltip, not reachable by tap or keyboard.
8. (sev 2, confirmed) The phone bottom nav covers the last holding's value, the price-date note and the "Added …" confirmation.
9. (sev 2, confirmed) In the Add holding dialog, Escape doesn't close it and Tab focus leaves the dialog.
10. (sev 2, confirmed) "Already withheld" doesn't match the sum of the Withheld column, because it includes foreign tax without saying so.
11. (sev 2, confirmed) The tax screen is called "Statements" on a phone but "Tax report" on desktop and in the page heading.
12. (sev 2, opinion) The tax report opens on 2025 without clearly flagging the year, so the headline figure is easy to misread.
13. (sev 2, confirmed) Validation errors appear one at a time in a top banner, not next to the field, and a stale error stays after the input is fixed.
14. (sev 2, opinion) The Security field is free text with no lookup, so duplicate or misspelled securities can be created.
15. (sev 2, confirmed) The phone "+" add button has no visible or accessible label.
16. (sev 1, confirmed) A long security name makes the desktop holdings table overflow its card.
17. (sev 1, confirmed) The Price per share input is slightly clipped at the bottom of the desktop Add holding dialog.

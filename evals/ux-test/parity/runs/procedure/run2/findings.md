# AEGIS-015, arm "procedure", run 2

A fresh Opus 5.5 subagent ran this with the fixed prompt in `../../../prompt.md` and the skill file `arms/procedure/SKILL.md`. It read no other files.
- Cost: 118,644 harness tokens, 44 tool uses, about 3.8 minutes.
- The browser pane was hidden, so screenshots came back cropped. The tester checked layout with read-only geometry instead.

1. The tax year can't be chosen on the phone, so the 2024 KESt can't be reached (sev 4, confirmed).
2. The phone has no Export CSV button (sev 4, confirmed).
3. The portfolio's total value is missing on the phone (sev 4, confirmed).
4. Each holding's unrealised gain is missing on the phone (sev 4, confirmed).
5. The total unrealised gain is missing on the phone (sev 4, confirmed).
6. On the phone, the fixed bottom nav covers the confirmation after adding a holding (sev 3, confirmed).
7. On the phone, the "Foreign tax" column of the tax table is clipped and can't be scrolled to (sev 3, confirmed).
8. On the phone, the "KESt" column of the tax table is clipped (sev 3, confirmed).
9. On the phone, the "Withheld" column of the tax table is clipped (sev 3, confirmed).
10. On the phone, the "Due" column of the tax table is clipped (sev 3, confirmed).
11. The KESt explanation only appears on hover, so it can't be read on a phone (sev 3, confirmed).
12. The phone tax screen never says which year its figures are for (sev 3, confirmed).
13. Added holdings disappear when the page reloads. This may be a prototype limitation (sev 3, confirmed).
14. The phone holding cards show three numbers with no labels (sev 2, confirmed).
15. The tax screen's tab is "Tax report" on desktop and "Statements" on the phone (sev 2, confirmed).
16. The "Add holding" label becomes an unlabelled "+" on the phone (sev 2, confirmed).
17. The "+" add button is a 28x28 px tap target (sev 2, confirmed).
18. The Shares field doesn't bring up a numeric keyboard (sev 2, confirmed).
19. The Purchase price field doesn't bring up a numeric or decimal keyboard (sev 2, confirmed).
20. On the phone, the fixed bottom nav covers the "Prices as of" date note (sev 2, confirmed).
21. Export CSV shows the CSV text on the page and doesn't download a file (sev 2, confirmed).
22. On desktop, the KESt explanation is a native tooltip on a small icon that the keyboard can't reach (sev 2, confirmed).
23. The bottom nav buttons are 40 px tall, under the 44 px minimum (sev 1, confirmed).
24. Form errors appear at the top of the dialog, one at a time, not next to the field that failed (sev 1, opinion).

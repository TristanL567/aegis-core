# AEGIS-015, arm "procedure-v2", run 3

The tester was a fresh Opus 5.5 subagent given the fixed prompt in `../../../prompt.md` and the skill file `arms/procedure-v2/SKILL.md`. It read no other files.
- Harness tokens: 131,509.
- Tool uses: 49.
- Time: about 3.9 minutes.

1. (sev 4, confirmed) Phone: the tax-year selector is missing, so 2024 can't be chosen and the screen never says which year is shown.
2. (sev 4, confirmed) Phone: the Export CSV action is missing.
3. (sev 4, confirmed) Phone: the portfolio total is missing.
4. (sev 4, confirmed) Phone: the unrealised gain per holding is missing.
5. (sev 3, confirmed) Phone: the holding cards show three numbers without their Shares/Price/Market value labels.
6. (sev 3, confirmed) Phone: the tax table's Foreign tax, KESt, Withheld and Due columns are clipped and can't be scrolled to.
7. (sev 3, confirmed) Both: the KESt explanation sits behind a hover-only "i" that doesn't open on tap or click and can't be reached by keyboard.
8. (sev 3, confirmed) Both: holdings can't be edited or deleted, so a mistaken entry can't be undone.
9. (sev 2, confirmed) Phone: the add-holding confirmation and the "Prices as of" footer are hidden under the bottom nav.
10. (sev 2, confirmed) The tax screen is called "Tax report" on desktop but "Statements" on the phone.
11. (sev 2, confirmed) Phone: the "+" button (28x28) and the nav tabs (40 px tall) are below the 44 px tap-target size.
12. (sev 2, confirmed) Phone: the Shares and Price fields bring up a text keyboard instead of a numeric one.
13. (sev 2, confirmed) "Today's closing prices" contradicts the week-old price date, 10.10.2026.
14. (sev 2, opinion) The tax report opens on 2025 with only a small year select, so the 2025 amount is easily read as what's owed for 2024.
15. (sev 2, opinion) The Security field is free text, so a typo silently creates a duplicate holding valued at purchase price.
16. (sev 1, confirmed) Validation errors appear at the top of the dialog, not next to the field, and stay after the field is fixed.
17. (sev 1, confirmed) The confirmation reads "Added 1 shares".
18. (sev 1, confirmed) The Add holding button has no accessible name.

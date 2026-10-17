# AEGIS-015, arm "procedure", run 3

The tester was a fresh Opus 5.5 subagent given the fixed prompt in `../../../prompt.md` and the skill file `arms/procedure/SKILL.md`. It read no other files.
- Cost: 131,839 harness tokens, 44 tool uses, about 3.9 minutes.
- One read-only script scrolled the page to measure overlap.

1. (sev 4, confirmed) Phone: the tax year selector is missing, so the KESt for 2024 can't be found.
2. (sev 4, confirmed) Phone: the Export CSV button is missing, so holdings can't be exported.
3. (sev 4, confirmed) Phone: the portfolio total (value and gain) is missing.
4. (sev 4, confirmed) Phone: the unrealised gain per holding is missing.
5. (sev 4, confirmed) Added holdings are lost when the page reloads. This may be prototype behaviour.
6. (sev 3, confirmed) Phone: the tax table's Foreign tax, KESt, Withheld and Due columns are clipped and can't be scrolled to.
7. (sev 3, confirmed) The KESt explanation exists only as a hover tooltip, so tap and keyboard users can't reach it.
8. (sev 3, confirmed) Phone: the bottom nav covers the save confirmation, the "Prices as of" note and the last holding's value, so adding a holding gives no visible confirmation.
9. (sev 3, confirmed) A holding added by mistake can't be deleted, edited or undone.
10. (sev 2, confirmed) Phone: holding cards have no labels for shares, price and value.
11. (sev 2, confirmed) The tax screen is called "Tax report" on desktop but "Statements" in the phone nav.
12. (sev 2, confirmed) Phone: "Add holding" becomes an unlabelled 28x28 "+", below the 44 px tap size.
13. (sev 2, confirmed) The Shares and Price fields don't open a numeric keyboard (type="text", no inputmode).
14. (sev 2, opinion) Adding a security already in the portfolio silently merges it, with no explanation of the effect on cost.
15. (sev 2, opinion) The tax report defaults to 2025, and on the phone the year shown isn't labelled anywhere.
16. (sev 1, confirmed) Phone: the bottom nav tap targets are 40 px high, below 44 px.
17. (sev 1, opinion) "Withheld + foreign credit" in the summary and "Foreign tax" / "Withheld" in the table name the same amounts in two ways.

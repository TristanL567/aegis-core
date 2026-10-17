# AEGIS-015, arm "procedure-v2", run 1

The tester was a fresh Opus 5.5 subagent given the fixed prompt in `../../../prompt.md` with the skill file `arms/procedure-v2/SKILL.md`. It read no other files.
- Cost: 129,954 harness tokens and 47 tool uses, about 3.8 minutes.
- It used form_input once on desktop, then redid that step with the keyboard.
- It listed the prototype's limits (lost data on reload, purchase-price valuation, export shown as a preview) as notes, not findings.

1. (sev 4, confirmed) The phone doesn't show the unrealised gain per holding.
2. (sev 4, confirmed) The phone doesn't show the portfolio's total value or total gain.
3. (sev 4, confirmed) Export CSV is missing on the phone, so T4 can't be done.
4. (sev 4, confirmed) The tax-year selector is missing on the phone, so the 2024 KESt can't be reached.
5. (sev 3, confirmed) On the phone, the tax table's Foreign tax, KESt, Withheld and Due columns are clipped and can't be scrolled to.
6. (sev 3, confirmed) The KESt explanation is only a hover title tooltip, so touch and keyboard users can't read it.
7. (sev 3, confirmed) The phone tax report doesn't name the tax year its figures belong to.
8. (sev 3, confirmed) The fixed bottom nav covers the last holding's market value, the "Prices as of" note and the end of the CSV preview, and the page can't be scrolled past it.
9. (sev 2, confirmed) The confirmation after adding a holding isn't visible on the phone.
10. (sev 2, confirmed) The phone holding cards show numbers without labels for shares, price and market value.
11. (sev 2, confirmed) On the phone, Add holding is an unlabelled 28x28 px "+" icon with no accessible name, below the 44 px tap target.
12. (sev 2, confirmed) The tax section is called "Tax report" on desktop and "Statements" on the phone.
13. (sev 2, confirmed) The Shares and Price fields don't bring up a numeric keyboard (type="text", no inputmode).
14. (sev 1, confirmed) The bottom nav tap targets are 40 px tall, below 44 px.

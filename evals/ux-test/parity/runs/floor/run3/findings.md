# AEGIS-015, arm "floor", run 3

The tester was a fresh Opus 5.5 subagent. It got the fixed prompt in `../../../prompt.md` with the skill file `arms/floor/SKILL.md`, and read no other files. Usage: 120,772 harness tokens, 38 tool uses, about 3 minutes.

1. (sev 4, confirmed) On a phone, the unrealised gain per holding and the portfolio total are hidden, and the holding cards have no labels.
2. (sev 4, confirmed) On a phone, the tax report has no tax-year selector and doesn't say which year it shows, so 2024 can't be reached.
3. (sev 4, confirmed) On a phone, the Export CSV button is hidden, so you can't export there.
4. (sev 3, confirmed) The KESt explanation is a hover-only tooltip. A tap, a click or the keyboard can't reach it.
5. (sev 3, confirmed) On a phone, the tax table is cut off after "Gross" and can't be scrolled, so the KESt, Withheld and Due columns are unreachable.
6. (sev 3, confirmed) On a phone, the fixed bottom nav covers the last holding's value, the price-date line and the save confirmation.
7. (sev 3, confirmed) Export CSV only shows a text preview on the page, with no download or copy action and no confirmation.
8. (sev 3, confirmed) Holdings can't be edited or deleted, so a mistaken add can't be undone.
9. (sev 2, confirmed) Adding a security you already hold quietly merges into it, so repeating the add doubles the position without a warning.
10. (sev 2, confirmed) Form errors show one at a time at the top of the dialog instead of next to each field.
11. (sev 2, confirmed) The same section is called "Tax report" on desktop and "Statements" on a phone.
12. (sev 2, confirmed) Phone touch targets are too small: "+" is 28x28 with no label, and the bottom nav buttons are 40px tall.
13. (sev 2, confirmed) The Shares and Purchase price fields are text inputs, so phones show the text keyboard instead of a number keypad.
14. (sev 1, confirmed) The confirmation says "Added 1 shares", with the wrong plural.
15. (sev 2, opinion) The CSV mixes semicolons with dot decimals, which Austrian Excel may misread.

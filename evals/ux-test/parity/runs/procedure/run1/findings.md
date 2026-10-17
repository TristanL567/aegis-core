# AEGIS-015, "procedure" arm, run 1

The tester was a fresh Opus 5.5 subagent. It got the fixed prompt from `../../../prompt.md` with the skill file `arms/procedure/SKILL.md`, and read no other files.
- **Cost:** 133,294 harness tokens, 49 tool uses, about 3.9 minutes.
- **Deviation:** it set the desktop year select with form_input once.

1. On the phone there is no tax-year selector, so the 2024 KESt can't be reached (sev 4, confirmed).
2. The Export CSV button is missing on the phone (sev 4, confirmed).
3. The portfolio total (market value and total gain) is missing on the phone (sev 4, confirmed).
4. The unrealised gain per holding is missing on the phone (sev 4, confirmed).
5. The phone holding cards have no labels for shares, price and market value (sev 2, confirmed).
6. On the phone, the "Foreign tax" column of the tax table is clipped and can't be scrolled to (sev 3, confirmed).
7. On the phone, the "KESt" column of the tax table is clipped and can't be scrolled to (sev 3, confirmed).
8. On the phone, the "Withheld" column of the tax table is clipped and can't be scrolled to (sev 3, confirmed).
9. On the phone, the "Due" column of the tax table is clipped and can't be scrolled to (sev 3, confirmed).
10. The phone tax report doesn't say which tax year it shows (sev 3, confirmed).
11. The KESt explanation is only a hover title tooltip. It can't be tapped or focused, and the icon is about 14 px (sev 3, confirmed).
12. The same screen is named "Tax report" on desktop and "Statements" on the phone (sev 2, confirmed).
13. On the phone, the add-holding confirmation sits below the fold and under the bottom nav (sev 2, confirmed).
14. The fixed bottom nav covers the last content (last value, price footnote, messages) even when fully scrolled (sev 2, confirmed).
15. The "+" add button is 28x28 px and has no accessible name (sev 2, confirmed).
16. The shares and price fields are type=text with no inputmode, so no numeric keyboard appears (sev 2, confirmed).
17. The bottom nav tabs are 40 px tall, under the 44 px minimum (sev 1, confirmed).
18. A price written as "€ 1.234,50" (euro sign and thousands separator) is rejected (sev 2, confirmed).
19. Validation errors appear one at a time at the top of the dialog, not next to the field, and they shift the Save button (sev 1, opinion).
20. Adding a security that is already held merges it into the existing row without saying so (sev 2, opinion).
21. An added holding is lost when the page reloads; this may be prototype behaviour (sev 3, confirmed).
22. "Today's closing prices" contradicts the footnote "as of 10.10.2026" (sev 2, confirmed).
23. The export result appears as inline text far below the button, not as a visible download or confirmation (sev 2, opinion).
24. The CSV uses "." decimals with ";" separators, which Austrian Excel may misread (sev 2, opinion).
25. Gains and losses are shown in green and red; a minus sign is also shown (sev 1, opinion).

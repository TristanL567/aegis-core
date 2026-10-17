# AEGIS-015, "floor" arm, run 2

A fresh Opus 5.5 subagent ran this with the fixed prompt in `../../../prompt.md` and the skill file `arms/floor/SKILL.md`. It read no other files. Usage: 135,592 harness tokens, 52 tool uses, about 4.5 minutes.

1. Added holdings are lost when the page reloads (sev 4, confirmed).
2. On the phone, the Holdings screen hides the column headers, the Unrealised gain column and the Total row, so T1 can't be done (sev 4, confirmed).
3. On the phone, the tax-year picker is hidden, so 2024 can't be selected and the year shown (2025) has no label (sev 4, confirmed).
4. On the phone, Export CSV is hidden, so T4 can't be done (sev 4, confirmed).
5. The KESt explanation is only a hover tooltip on a 20px "i". Tapping does nothing and the keyboard can't reach it (sev 3, confirmed).
6. On the phone, the tax table is clipped to 3 of its 7 columns: Foreign tax, KESt, Withheld and Due are cut off and can't be scrolled to (sev 3, confirmed).
7. On the phone, the fixed bottom nav covers the last holding's value, the price-date note and the "Added…" success message (sev 3, confirmed).
8. A holding can't be edited or deleted, so a wrong entry such as the free-text "Nonexistent Corp" can't be removed (sev 3, confirmed).
9. On the phone, the "+" button for adding a holding is a 28x28 icon with no label, below the minimum tap-target size (sev 2, confirmed).
10. Export CSV gives no confirmation and no sign of a download; the result appears below the fold as a text preview (sev 2, confirmed).
11. The same screen is called "Tax report" on desktop and "Statements" in the phone nav (sev 2, confirmed).
12. The Shares and Price inputs are type="text" with no inputmode, so phones show the text keyboard (sev 2, confirmed).
13. The phone bottom nav buttons are 40px tall, under 44px (sev 1, confirmed).
14. "Today's closing prices" contradicts "Prices as of 10.10.2026" (sev 2, opinion).
15. Form errors appear one at a time at the top of the dialog, not next to the field (sev 2, opinion).
16. The CSV pairs semicolon separators with dot decimals and drops the "(purchase)" marker (sev 2, opinion).
17. The success message says "Added 1 shares" (sev 1, confirmed).

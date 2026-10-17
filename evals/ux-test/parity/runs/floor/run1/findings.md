# AEGIS-015, arm "floor", run 1

The tester was a fresh Opus 5.5 subagent. It used the fixed prompt from `../../../prompt.md` with the skill file `arms/floor/SKILL.md`, and read no other files.
- Harness tokens: 120,310.
- Tool uses: 43.
- Time: about 3.5 minutes.

1. (sev 4, confirmed; T1, phone) The phone layout hides the gain column, the Total row and the column labels, so the total value and the gains can't be seen.
2. (sev 4, confirmed; T3, phone) There is no tax-year selector on the phone. 2024 can't be reached, and the 2025 figures are shown without naming the year.
3. (sev 4, confirmed; T4, phone) The Export CSV button is hidden on the phone, so export is impossible.
4. (sev 3, confirmed; T3, both) The KESt explanation is a hover-only title tooltip on a small icon that can't be focused, so it can't be read by touch or by keyboard.
5. (sev 3, confirmed; T2, phone) The fixed bottom navigation covers the "Added ..." confirmation and the "Prices as of" footnote at the end of the page.
6. (sev 3, confirmed; T3, phone) The tax breakdown table is clipped (overflow hidden), so the Foreign tax, KESt, Withheld and Due columns can't be reached.
7. (sev 3, confirmed; T2, both) Holdings can't be edited or deleted, so a mistaken or repeated add can't be undone, and repeat adds merge silently.
8. (sev 2, confirmed; T2, phone) The "+" Add holding button is 28x28px with no visible or accessible label, below the 44px touch minimum.
9. (sev 2, confirmed; T2, both) The Shares and Price fields are type="text", so phones show no numeric keyboard.
10. (sev 2, confirmed; both) The same screen is named "Tax report" on desktop and "Statements" on the phone.
11. (sev 2, opinion; T4, desktop) Export CSV gives no confirmation that a file was saved. It shows a preview below the fold with no download or copy control.
12. (sev 1, confirmed; T2, both) The "Added ..." confirmation stays after navigating away and back, so it can be stale.

# Parity baseline run 3 (current ux-test skill, fixed page)

The tester was a fresh Opus 5.5 subagent given the fixed prompt in `../../../prompt.md`. It read only the skill file and wrote no files. The run cost 112,812 harness tokens, used 35 tools, and took about 3 minutes.

Coverage gap: it didn't click Export CSV on desktop, because it assumed the button starts a download. In fact it shows an on-page preview.

1. (sev 4, confirmed) Export CSV is hidden at phone width, so T4 is impossible on a phone.
2. (sev 4, confirmed) The phone Holdings view has no portfolio total and no gain per holding, so T1 fails on a phone.
3. (sev 4, confirmed) The tax year selector is hidden on the phone and no year is shown, so the 2025 figure (€120.13) reads as the 2024 answer.
4. (sev 4, confirmed) Added holdings are lost when the page reloads. This may be deliberate prototype behaviour.
5. (sev 3, confirmed) On the phone, the tax table's Foreign tax, KESt, Withheld and Due columns are clipped and can't be scrolled to.
6. (sev 3, confirmed) The KESt explanation is a hover-only tooltip that touch and keyboard users can't reach.
7. (sev 3, confirmed) The "Added … shares" confirmation is never visible on the phone; it stays under the bottom nav.
8. (sev 2, confirmed) On the phone, the bottom nav covers the last holding's value and the "Prices as of" footnote.
9. (sev 2, confirmed) The holding rows on the phone show unlabelled numbers (shares, price, value).
10. (sev 2, confirmed) The tax screen is called "Statements" in the phone nav and "Tax report" everywhere else.
11. (sev 2, opinion) The tax report defaults to 2025 with an easy-to-miss year selector, so the wrong year is easy to read.
12. (sev 1, opinion) Validation errors appear at the top of the dialog, not next to the field at fault.
13. (sev 1, confirmed) The success note stays on screen and repeats the same text, so a second add can't be told apart from the first.
14. (sev 1, opinion) "Today's closing prices" contradicts the footnote date of 10.10.2026.

# Parity baseline run 1 (current ux-test skill)

The tester was a fresh Opus 5.5 subagent using the fixed prompt in `../../../prompt.md`. It read only the skill file, used page scripts to read scroll position and focus, and did all actions by click, typing and key.
- Harness tokens: 120,349. 38 tool uses, about 3.3 minutes.
- Coverage gap: T4 at desktop width was not clicked, because the tester believed a download needed permission.

1. (sev 4, confirmed) On phone, the Holdings list hides the unrealised gain per holding and the portfolio total, and its values have no labels. This blocks T1 on phone.
2. (sev 4, confirmed) On phone, the Tax report has no tax-year selector, always shows 2025, and never says which year it shows. This blocks T3 for 2024 on phone.
3. (sev 4, confirmed) On phone there is no Export CSV control. This blocks T4 on phone.
4. (sev 3, confirmed) A newly added holding is valued at its purchase price, not today's close. Its market value, its gain and the portfolio total are therefore wrong.
5. (sev 3, confirmed) Saving the same holding again silently creates a duplicate row, and no row can be edited or deleted to recover.
6. (sev 3, confirmed) The KESt explanation exists only as a hover tooltip on a small (i) icon. Tapping it does nothing, and nothing visible appeared on desktop.
7. (sev 3, confirmed) On phone, the fixed bottom navigation covers the end of the list: the last holding's value, the price-date note and the "Added ..." confirmation.
8. (sev 2, confirmed) On phone, the tax breakdown table hides the Foreign tax, KESt, Withheld and Due columns, with no scroll or other way to reveal them.
9. (sev 2, confirmed) The Add holding dialog doesn't close on Escape or a backdrop click, and Tab moves focus out of it to the page behind.
10. (sev 2, confirmed) Validation errors appear one at a time at the top of the dialog, not next to the field, and stay after the field is fixed.
11. (sev 2, confirmed) The price field rejects the Austrian format "1.234,50", and its error example says "42.50" although "42,50" is accepted.
12. (sev 2, confirmed) The same screen has two names: "Statements" in the phone nav, "Tax report" in the desktop nav and the page heading.
13. (sev 1, confirmed) Pressing Enter in an Add holding field doesn't submit the form.
14. (sev 2, opinion) The Tax report opens on 2025, and the year selector is small and far from the figures, so the wrong year's KESt is easy to read.

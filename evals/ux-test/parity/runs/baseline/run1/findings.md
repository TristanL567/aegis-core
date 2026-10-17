# Parity baseline run 1 (current ux-test skill, fixed page)

The tester was a fresh Opus 5.5 subagent given the fixed prompt in `../../../prompt.md`. It read only the skill file and wrote no files. Cost: 116,976 harness tokens, 38 tool uses, about 2.8 minutes.

1. (sev 4, confirmed) Phone, T3: there is no tax-year selector, so the KESt for 2024 can't be reached.
2. (sev 4, confirmed) Phone, T1: there is no portfolio total and no gain per holding, and the row values have no labels.
3. (sev 4, confirmed) T4, both widths: the phone has no export control. On desktop, Export CSV only shows the CSV as text on the page and never offers a file.
4. (sev 3, confirmed) Phone, T2: the confirmation after saving, the last row's value and the "Prices as of" note sit under the fixed bottom nav and can't be scrolled into view.
5. (sev 3, confirmed) Phone, T3: the KESt explanation is a hover-only tooltip that a tap can't open, and the KESt, Withheld and Due columns are missing.
6. (sev 3, confirmed) Both widths: holdings can't be edited or deleted, so a wrong entry can't be undone.
7. (sev 2, confirmed) Both widths: the tax section is called "Statements" on the phone and "Tax report" on desktop.
8. (sev 2, opinion) Both widths: adding a holding with an existing name merges into it without saying so, and any free-text security is accepted without checking that it exists.

# Parity baseline run 2 (current ux-test skill, fixed page)

A fresh Opus 5.5 subagent ran this with the fixed prompt in `../../../prompt.md`. It read only the skill file and wrote no files. Cost: 128,288 harness tokens, 42 tool uses, about 3.8 minutes.

1. (sev 4, confirmed) On a phone, the Tax report has no tax-year selector and no year label. The 2024 KESt can't be found, and the 2025 figures can be mistaken for the answer.
2. (sev 4, confirmed) On a phone, the Export CSV button and the CSV result are hidden, so holdings can't be exported.
3. (sev 4, confirmed) On a phone, the portfolio Total and each holding's unrealised gain aren't shown.
4. (sev 3, confirmed) On a phone, the fixed bottom navigation covers the end of the page. The last holding's value, the "Prices as of" note and the add-holding success message are hidden.
5. (sev 3, confirmed) On a phone, the tax table is cut off after Gross. Foreign tax, KESt, Withheld and Due can't be seen or scrolled to.
6. (sev 3, confirmed) The KESt explanation is reachable only by mouse hover. It doesn't respond to a tap, a click or the keyboard.
7. (sev 2, confirmed) Export CSV shows the content inline instead of saving a file, with no download or copy action and no saved confirmation. This may be a prototype stub.
8. (sev 2, confirmed) There is no way to undo, edit or delete a holding added by mistake.
9. (sev 2, confirmed) One screen has two names: "Statements" in the phone navigation, "Tax report" on desktop and in the heading.
10. (sev 2, opinion, not reproduced) Saving the Add holding dialog with all fields empty showed no error message on the first try.
11. (sev 2, opinion) The phone holding rows show shares, price and value as unlabelled numbers.
12. (sev 2, opinion) The CSV pairs semicolon separators with decimal points, which may import wrongly into spreadsheets set to Austrian locale.

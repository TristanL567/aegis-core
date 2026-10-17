# AEGIS-015, arm "procedure-v2", run 2

The tester was a fresh Opus 5.5 subagent, given the fixed prompt in `../../../prompt.md` and the skill file `arms/procedure-v2/SKILL.md`. It read no other files.
- Harness tokens: 122,315. Tool uses: 38. Time: about 3.6 minutes.
- It recorded prototype limits as notes, not findings.

1. (sev 4, confirmed) The portfolio Total (market value and total gain) is missing on the phone.
2. (sev 4, confirmed) The unrealised gain per holding is missing on the phone.
3. (sev 4, confirmed) The Export CSV button is missing on the phone, so T4 can't be done.
4. (sev 4, confirmed) The Tax year selector is missing on the phone, so 2024 can't be reached and the year shown has no label.
5. (sev 3, confirmed) The Tax report's "Foreign tax" column is clipped on the phone and can't be scrolled.
6. (sev 3, confirmed) The Tax report's "KESt" column is clipped on the phone and can't be scrolled.
7. (sev 3, confirmed) The Tax report's "Withheld" column is clipped on the phone and can't be scrolled.
8. (sev 3, confirmed) The Tax report's "Due" column is clipped on the phone and can't be scrolled.
9. (sev 3, confirmed) Shares typed as "1.000", the Austrian way of writing one thousand, are silently saved as 1 share.
10. (sev 3, confirmed) The KESt explanation behind the "i" icon never appears on click or tap, and the keyboard can't reach the icon.
11. (sev 3, confirmed) On the phone, the bottom navigation covers the end of the page, hiding the "Added..." confirmation, the prices note and the last holding's value.
12. (sev 2, confirmed) The tax screen is called "Tax report" on desktop but "Statements" on the phone.
13. (sev 2, confirmed) The phone's add button is an unlabelled "+" and only 28x28 px.
14. (sev 2, confirmed) The Shares and Price fields are type=text with no inputmode, so the phone shows a text keyboard.
15. (sev 2, confirmed) The phone's holding cards show three numbers with no Shares/Price/Market value labels.
16. (sev 2, opinion) The Tax report opens on 2025 and the year selector is easy to miss, so users may read the wrong year's amount due.
17. (sev 1, confirmed) The summary says "foreign credit" while the table says "Foreign tax".
18. (sev 1, confirmed) The bottom nav tabs are 40 px tall, under the 44 px minimum.
19. (sev 1, confirmed) The confirmation text has a grammar error: "Added 1 shares".

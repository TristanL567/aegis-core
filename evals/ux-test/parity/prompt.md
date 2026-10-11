# Fixed tester prompt for the parity test bed

Give this prompt to a fresh tester subagent, filling in the port and the
skill path. Use it unchanged for the AEGIS-014 baseline and for every
AEGIS-015 arm.

```text
Run usability tests on this web app. Use the ux-test skill: read `<path to .claude/skills/ux-test/SKILL.md>` and follow it.

App: http://127.0.0.1:<port>/ - "EasyRep", a web app where private investors in Austria track their portfolio and their capital-income tax. It is already served from a copy outside the repo. Key tasks:
- T1: check your portfolio's total value and how much each holding has gained.
- T2: add a new holding: 10 shares of Erste Group at EUR 42.50.
- T3: find how much KESt you still owe for tax year 2024, and what KESt is.
- T4: export your holdings as a CSV file.

Use the built-in browser tools (mcp__Claude_Browser__*). Open your own new tab with tabs_create (if that fails, open the URL with preview_start), and pass its tabId on every browser call; never touch other tabs. Test only the app as served in the browser: apart from the skill file, do not read, search or list any files and do not run shell commands. Reset any viewport you set and close your tab when done. Do not write files; put any findings.yaml content in your reply.

End your reply with every usability problem you found as a numbered list, one problem per item.
```

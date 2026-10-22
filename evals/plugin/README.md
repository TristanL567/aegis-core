# AEGIS as a Claude Code plugin: tests (AEGIS-024)

The repository root is the plugin `aegis` and its own marketplace
`aegis-core` (`.claude-plugin/`). The manifest points at the existing
`.claude/skills/`, `.claude/agents/ux-persona.md` and `.claude/hooks/`, so
nothing is copied. Its hooks are those of `.claude/settings.json`, run from
`${CLAUDE_PLUGIN_ROOT}`.

## Tests

```bash
python evals/plugin/test_plugin.py
claude plugin validate .
```

The tests check that the manifest's paths exist, that its hooks have the same
events, matchers and guard modes as `.claude/settings.json`, that the
marketplace lists the repo root as `aegis`, and that `claude plugin validate`
passes for the plugin and the marketplace. The one warning, "No version
specified", is deliberate: without a version, every commit is an update.

## Live check (2026-10-22, Claude Code 2.1.295, Windows, Git Bash)

A fresh repo with no AEGIS files of its own except ticket `HK-001`
(`src/` allowed), then one `claude --plugin-dir <this repo> -p --model haiku
--permission-mode acceptEdits` session:

| Step | Result | Checked on disk |
|---|---|---|
| Write tool, `outside.txt` | blocked: "outside the allowed_areas of ticket HK-001" | file absent |
| Write tool, `src/inside.txt` | allowed | file present |
| Skills listed | `aegis:design-track`, `aegis:ux-test`, `aegis:validate`, `aegis:write-ticket` | n/a |

Not checked live: installing from GitHub with `/plugin install`, which needs
this branch on `main`; the stash and SubagentStop hooks through the plugin
(the same commands, tested in `evals/hooks/`).

relevant-when: Open this drawer when implementation needs command, environment, or configuration conventions.

# Shell Config Idioms

- Shell and configuration knowledge is reference material here, not a runtime
  operations procedure or tooling change.
- Commands should distinguish developer convenience from production behavior,
  and scripts should make required working directory, environment variables,
  and inputs clear.
- Quote paths and values that may contain spaces or shell-sensitive characters.
  Prefer structured command arguments over string-built shell calls in code.
- Environment variables should be read at clear boundaries and converted into
  typed configuration before deep application code uses them.
- Config defaults should be explicit, documented in code or schema, and safe for
  the environment where they run.
- Avoid hiding failures in chained commands or broad fallbacks when setup,
  build, migration, or deployment behavior depends on the result.
- Cross-platform scripts should account for PowerShell, POSIX shell, path
  separators, line endings, and executable discovery where the repo supports
  multiple environments.

# AEGIS Hook Templates

These hooks are templates for target projects. AEGIS-CORE ships them but does
not install them automatically.

## Install

Copy the hooks into a target repository's `.git/hooks/` directory:

```sh
cp execution/templates/hooks/commit-msg /path/to/target/.git/hooks/commit-msg
cp execution/templates/hooks/pre-commit /path/to/target/.git/hooks/pre-commit
chmod +x /path/to/target/.git/hooks/commit-msg /path/to/target/.git/hooks/pre-commit
```

Or copy the directory into the target project and set:

```sh
git config core.hooksPath .aegis/hooks
```

## Configuration

Each hook has configuration variables at the top:

- `AEGIS_TICKET_DIR`: target repository directory containing ticket envelopes.
  Default: `.aegis/tickets`.
- `AEGIS_ACTIVE_TICKET_FILE`: file containing the active ticket ID or ticket
  path. Default: `.aegis/active-ticket`.
- `AEGIS_CORE_ROOT`: path to the AEGIS-CORE checkout used by `pre-commit`.
- `AEGIS_PYTHON`: Python launcher used by `pre-commit`. Use `python3` on most
  POSIX systems or `py -3.10` in Git Bash on Windows when available.

## Active Ticket Convention

The target project records the active ticket in:

```text
.aegis/active-ticket
```

The file may contain either a ticket ID such as `AEGIS-EXAMPLE-001` or a path to
the ticket envelope. When it contains an ID, the hooks resolve it under
`AEGIS_TICKET_DIR` with `.yaml`, `.yml`, or `.md`.

## Enforcement

- `commit-msg` rejects commit subjects that do not match
  `[TICKET-ID] concise description` with a description of 72 characters or
  fewer. It also checks that the ticket file exists and matches the active
  ticket when `.aegis/active-ticket` is present.
- `pre-commit` rejects staged files outside the active ticket's `allowed_areas`
  or inside `must_not_touch` by wiring through
  `tools/validate_ticket_scope.py`.

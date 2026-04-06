# Codex Execution Guide

Use Codex as the operator-facing execution environment.

## Recommended Pattern

- Load the canonical skill file from the library repo.
- Use the `master` skill as the operator prompt.
- Delegate specialist work to focused workers.
- Route outputs through a validator before presenting them as complete.

## Good Fit

- tasks that benefit from parallel specialist execution
- code changes with real file ownership
- review loops that need a clear validator stage

## Starter Steps

1. Point the execution repo to the library repo path.
2. Start a session with the `master` prompt plus the current task envelope.
3. Dispatch work to the appropriate worker prompt.
4. Run the validator prompt against the worker output.
5. Send the validator result back to the master.

See `templates/codex/operator-playbook.md` for a starter operator flow.

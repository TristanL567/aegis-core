# Antigravity Execution Guide

Antigravity support is more workflow-template oriented in this scaffold.

## Recommended Pattern

- Treat the canonical skill text as the source prompt.
- Pair it with provider-specific workflow templates for session startup and handoffs.
- Keep the same logical orchestration loop used everywhere else.

## Starter Steps

1. Start a session with the `master` template and current task envelope.
2. Hand off to a worker template with explicit task scope.
3. Run the validator template against the worker output.
4. Return the verdict to the master for the next step or human approval.

## Notes

- Keep approval checkpoints explicit.
- Avoid letting worker sessions silently absorb review or planning responsibilities.
- Document any provider-specific deviation in the execution repo, not in the canonical library.

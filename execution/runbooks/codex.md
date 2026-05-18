# Codex Runbook

Codex is a run-and-return execution environment. Each call produces one response and does not retain native session state, so the operator carries the ticket envelope, artifacts, and validator results forward between calls.

This runbook is provider-specific guidance for Codex only. Canonical role behavior remains in `skills/`, and canonical ticket and swarm rules remain in `contracts/`.

## Recommended Pattern

- Run exactly one assigned ticket at a time. Finish the current ticket's validator gate and completion report before starting another ticket.
- Load the relevant canonical `SKILL.md` from `skills/` for each dedicated Codex call.
- Sequence the loop manually as `master -> worker -> validator -> master`.
- Pass the full ticket envelope and prior output envelope into the next call. Codex has no other state source.
- Never skip the validator call. The operator must hold the result and refuse to advance while validator status is `fixes_required`.

## Prompt Assembly

Every Codex call should include:

- **Skill body**: the current canonical skill text from `skills/`, used as the role instruction for that call.
- **Ticket envelope**: the full assigned ticket, including id, objective, allowed areas, acceptance criteria, verification expectations, branch or dependency context, and human constraints.
- **Prior artifacts**: only the relevant master decision, worker output, validator findings, changed-file list, or verification evidence needed for the current phase.
- **Output envelope instruction**: an explicit request to return `status`, `summary`, `artifacts`, `findings`, and `next_recommended_role`.

Reusable envelope examples live under `execution/templates/`. Keep required fields explicit in prompts rather than relying on implicit context.

## Ticket-Based Execution

The master must confirm ticket completeness before dispatch. If the ticket lacks a clear objective, allowed areas, acceptance criteria, verification requirements, or required branch context, the master should return a blocked or clarification status instead of assigning a worker.

Workers must stay inside the ticket's allowed areas. If implementation appears to require files, contracts, skills, templates, prompts, or other surfaces outside those boundaries, the worker reports the conflict in `findings` and returns control.

Validators receive the full ticket envelope plus the worker output. Their review should check boundaries, acceptance criteria, verification evidence, and whether the worker supplied an adequate completion report.

Before completed work is returned to the human, require a completion report that identifies changed files, verification performed or skipped, residual findings, and the recommended next role.

## Codex Operator Flow

1. Start a Codex call with the `master` skill from `skills/master/SKILL.md`. Provide the full ticket envelope and require a structured handoff decision.
2. Open a new Codex call for the selected worker skill. Provide the full ticket envelope, the master's scope, relevant prior artifacts, and the output envelope instruction.
3. Open a new Codex call for the appropriate validator skill. Provide the full ticket envelope and complete worker output, including changed files and verification evidence.
4. Read the validator `status` before taking any further action.
5. If status is `completed`, return the validator result to the `master` in a new Codex call for final routing or human-facing completion.
6. If status is `fixes_required`, re-dispatch the relevant worker with the original ticket envelope plus the validator findings, then run the validator again.

## Validator Gate

Codex does not enforce blocking across calls. The operator enforces the gate manually:

- `completed`: carry the full validator response back to the `master`.
- `fixes_required`: do not advance; route findings back to the worker and re-run validation.
- `blocked`: return the blocker to the `master` for routing or human approval.

The master may only override validator findings after explicit human approval. That approval must be included in the carried-forward context for later calls.

## Good Fit

Codex is a good fit for scoped ticket work, code or documentation edits with clear file ownership, and review loops that need an explicit validator stage. Keep provider-specific mechanics here, and keep shared orchestration guidance in `execution/runbooks/shared-orchestration-loop.md`.

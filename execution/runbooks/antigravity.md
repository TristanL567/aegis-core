# Antigravity Runbook

Antigravity can run AEGIS as a session-oriented workflow. Use session startup prompts and explicit handoffs to preserve the shared orchestration loop while Antigravity manages local context.

This runbook is provider-specific guidance for Antigravity only. Canonical role behavior remains in `skills/`, and canonical ticket and swarm rules remain in `contracts/`.

## Recommended Pattern

- Run exactly one assigned ticket at a time. Finish the current ticket's validator gate and completion report before starting another ticket.
- Start each ticket with a master session using `prompts/07-providers/antigravity-setup.md`.
- Preserve the loop as `master -> worker -> validator -> master`.
- Use Antigravity workflow or session templates as wrappers around the canonical skills, not replacements for them.
- Keep ticket state, changed files, verification evidence, and validator results visible in every handoff.

## Master Session Startup

The master session receives the full ticket envelope and owns routing. It should load or reference:

- `skills/master/SKILL.md`
- `contracts/ticket-contract.md`
- `contracts/swarm-contract.md`
- `execution/runbooks/shared-orchestration-loop.md`
- `execution/templates/ticket-envelope.example.yaml`
- `execution/templates/completion-report.example.yaml`

The master confirms ticket completeness, selects the worker and validator, and returns the next copy/paste handoff. If the ticket is incomplete or would require work outside scope, the master returns `blocked` instead of dispatching.

## Worker Handoff

The worker handoff should include:

- the selected worker skill path from `skills/`;
- the full original ticket envelope;
- the master's routing notes;
- exact allowed areas and must-not-touch areas;
- acceptance criteria and verification commands;
- the standard output envelope fields.

Workers implement only the assigned ticket. If the worker discovers that completion requires broader scope, it reports the conflict in `findings` and returns control rather than expanding the ticket.

## Validator Handoff

The validator handoff should include:

- the selected validator skill path from `skills/`;
- the full original ticket envelope;
- complete worker output;
- changed files and verification evidence;
- any known residual risks or skipped checks.

Validators review only. They do not implement fixes, broaden scope, or ask the human for approval directly. Their result returns to the master.

## Gate Policy

Antigravity session continuity does not replace the blocking validator gate:

- `completed`: the master may prepare the final completion report.
- `fixes_required`: the master routes findings back to the worker, then sends revised output to the validator again.
- `blocked`: the master decides whether to request clarification, human approval, or a new ticket.

The master may override validator findings only after explicit human approval, and that approval must be recorded in the carried-forward session context.

## Output Discipline

Every Antigravity phase should return the standard envelope:

- `status`
- `summary`
- `artifacts`
- `findings`
- `next_recommended_role`
- `changed_files`
- `verification`

Use concise summaries and file references. Do not copy full skill bodies or full contract prose into the session prompt; point to the canonical files instead.

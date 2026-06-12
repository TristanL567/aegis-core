# Claude Code Runbook

Claude Code can run AEGIS with provider-local project agents, but the canonical role definitions stay in this repository. Generated `.claude/agents/` files belong in the target project or operator workspace, not in `aegis-core`.

This runbook is provider-specific guidance for Claude Code only. Canonical role behavior remains in `skills/`, and canonical ticket and swarm rules remain in `contracts/`.

## Recommended Pattern

- Run exactly one assigned ticket at a time. Finish the worker step, validator gate, and completion report before starting another ticket.
- Preserve the loop as `master -> worker -> validator -> master`.
- Use Claude Code subagents as transport wrappers around the canonical skills, not as independent role definitions.
- Keep human approval centralized through the master. Workers and validators should not ask the human directly unless the master routes that request.
- Treat validators as blocking by default. A worker result does not advance until the selected validator returns an approving result.

## Agent Setup

An operator may create provider-local `.claude/agents/` files in a target project to make role selection convenient. Those files should be derived stubs that point back to the canonical source instead of copying full skill bodies.

Recommended local agent stubs:

- `master`: points to `skills/master/SKILL.md`, `contracts/swarm-contract.md`, and `contracts/ticket-contract.md`; owns routing, scope checks, human approval, and completion reporting.
- `worker`: points to the selected worker skill in `skills/`, such as `skills/backend-worker/SKILL.md`, `skills/chart-worker/SKILL.md`, `skills/model-interpreter-worker/SKILL.md`, or `skills/ticket-planner-worker/SKILL.md`; implements only the assigned ticket scope.
- `validator`: points to the selected validator skill in `skills/`, usually `skills/code-validator/SKILL.md` or `skills/ds-validator/SKILL.md`; reviews only and does not implement fixes.

Use `prompts/07-providers/claude-code-setup.md` as copy/paste setup material when creating those local stubs. Do not commit generated provider-local agent files to this repository unless a separate ticket explicitly allows that path.

## Ticket Flow

1. Start with the master agent and provide the full ticket envelope, branch context, allowed areas, must-not-touch areas, acceptance criteria, and verification expectations.
2. The master selects one worker skill and one validator skill. If the ticket is incomplete, the master returns `blocked` or requests clarification.
3. Dispatch the worker with the full ticket envelope plus the master's routing decision. The worker must stay inside the ticket scope.
4. Send the complete worker output to the validator with the original ticket envelope, changed files, and verification evidence.
5. If the validator returns `completed`, route the validator result back to the master for final completion reporting.
6. If the validator returns `fixes_required`, route the findings back through the master to the worker, then run the validator again.

## Prompt Assembly

Each Claude Code role session or subagent invocation should include:

- **Canonical references**: the relevant `skills/.../SKILL.md` path and required contracts from `contracts/`.
- **Execution references**: `execution/runbooks/shared-orchestration-loop.md`, this runbook, and prompt files under `prompts/`.
- **Ticket envelope**: objective, scope, allowed areas, must-not-touch areas, acceptance criteria, verification commands, and branch context.
- **Prior artifacts**: master routing decision, worker output, validator findings, changed files, and verification notes needed for the current step.
- **Output envelope instruction**: require `status`, `summary`, `artifacts`, `findings`, `next_recommended_role`, `changed_files`, and `verification`.

Do not paste full skill bodies or full contract prose into generated agent files. Load or reference the current canonical files so role behavior stays synchronized with the library.

## Validator Gate

Claude Code may make it easy to continue a conversation after a worker finishes. The operator or master must still enforce the validator gate:

- `completed`: return the validator result to the master.
- `fixes_required`: do not advance; route findings back to the worker through the master.
- `blocked`: return the blocker to the master for routing or human approval.

The master may override validator findings only after explicit human approval, and that approval must be included in the carried-forward ticket context.

# Codex Execution Guide

Codex is a run-and-return execution environment: each call produces a single response and
terminates, with no native session persistence or inter-agent messaging. The operator is the
orchestration layer — you manually sequence master → worker → validator by loading each skill
as a system prompt in turn and carrying the output envelope forward.

## Recommended Pattern

- Treat each Codex run as execution for exactly one assigned ticket. Do not batch tickets
  into a single master, worker, or validator call; finish the current ticket's validator
  gate and completion report before starting another ticket.
- Load each canonical skill as the system prompt for its dedicated Codex call.
- Sequence the loop manually: master decides, worker executes, validator reviews, master
  receives the verdict and either advances or loops back.
- Pass the full output envelope from each call as the user-turn context for the next call;
  the envelope is the only thread of state Codex carries between runs.
- Never skip the validator call — without native blocking, the operator is responsible for
  holding the result and refusing to advance until the status is `completed`.

## Structuring Prompts

Combine three components into every Codex call:

1. **Skill body** — paste the full text of the canonical SKILL.md (below the YAML
   frontmatter) as the system prompt. This sets the role identity, hard rules, and output
   contract.
2. **Ticket envelope** — include the full assigned ticket envelope in every master,
   worker, and validator user turn. Use the shared example at
   `templates/aegis-execution/templates/shared/ticket-envelope.example.yaml` as the shape
   reference, and keep the ticket id, objective, allowed areas, acceptance criteria,
   verification requirements, and human constraints visible. Be explicit about what is in
   scope; Codex has no ambient context from prior calls.
3. **Output envelope instruction** — close the user turn with an explicit instruction such
   as: "Return your response using the standard output envelope: status, summary, artifacts,
   findings, next_recommended_role." This ensures the structured result is parseable before
   you route it onward.

## Ticket-Based Execution

- The master must check ticket completeness before dispatch: confirm the ticket has a clear
  objective, allowed areas, acceptance criteria, verification expectations, and any
  required dependency or branch context. If these are missing or contradictory, the master
  should return a clarification or blocked status instead of assigning a worker.
- Workers must stay inside the ticket's `allowed_areas`. When required work appears to
  touch files, contracts, skills, or templates outside those boundaries, the worker reports
  a boundary conflict in `findings` and returns control instead of expanding scope.
- Validators must receive the same full ticket envelope plus the worker output. Their
  review should check ticket boundaries, acceptance criteria, verification evidence, and
  whether the worker supplied an adequate completion report.
- Before returning work to the human, require a completion report following the shared
  example at `templates/aegis-execution/templates/shared/completion-report.example.yaml`.
  The report should identify changed files, verification performed or skipped, residual
  findings, and the recommended next role.

## Enforcing the Validator Gate

Codex has no native mechanism to block downstream progress when a validator returns
`fixes_required`. The operator must enforce this manually:

1. After receiving the validator response, read the `status` field before taking any further
   action.
2. Only advance to the next stage — returning the result to the master or surfacing a human
   approval checkpoint — when `status` is `completed`. If the status is `fixes_required`,
   extract the findings and re-dispatch the relevant worker with those findings appended to
   the user turn.

## Starter Steps

1. Point your execution repo at the library repo path and confirm the canonical skill files
   are accessible. This ensures you are loading the current skill body, not a stale copy.
2. Start a master call with the `master` skill body as the system prompt and the initial task
   envelope in the user turn. Include the full assigned ticket envelope and require the
   master to confirm ticket completeness before dispatch. Include the output envelope
   instruction so the master returns a structured handoff decision.
3. Dispatch the chosen worker by opening a new Codex call with the worker skill as the system
   prompt. Pass the full ticket envelope, task scope, any prior artifacts, and the output
   envelope instruction in the user turn.
4. Run the appropriate validator by opening another Codex call with the validator skill as
   the system prompt. Provide the full ticket envelope and worker output as the user turn,
   and require a verdict with severity-labeled findings covering boundaries, acceptance
   criteria, verification evidence, and completion-report quality.
5. Send the validator result back to the master in a new Codex call. Let the master decide
   whether to request fixes, advance to the next phase, or surface a human approval
   checkpoint.

## Good Fit

- tasks that benefit from parallel specialist execution
- code changes with real file ownership
- review loops that need a clear validator stage

See `templates/codex/operator-playbook.md` for a detailed operator flow.

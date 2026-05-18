# Codex Operator Playbook

Use this playbook in the execution repo to run the swarm manually. Codex is a run-and-return
environment: each call is stateless, and you are the orchestration layer that carries context
forward between calls.

## Prompt Assembly

Before opening any Codex call, assemble the prompt from three components:

- **Skill body** — paste the full text of the canonical SKILL.md below its YAML frontmatter
  as the system prompt. Do not paraphrase; use the canonical text verbatim so the role
  identity, hard rules, and output contract are intact.
- **Task envelope** — compose the user turn with: the task description, an explicit list of
  in-scope files or directories, any prior artifacts carried forward from earlier calls, the
  current phase label, and acceptance criteria. Codex has no ambient session context, so
  everything the model needs must be present in the user turn.
- **Ticket envelope** — include the full assigned ticket envelope in every master, worker,
  and validator call. Run one assigned ticket at a time, and use
  `templates/aegis-execution/templates/shared/ticket-envelope.example.yaml` as the shared
  shape reference.
- **Output envelope instruction** — close the user turn with an explicit instruction to
  return the standard output envelope. For example: "Return your response as structured text
  with the following fields: status, summary, artifacts, findings, next_recommended_role."
  Parse this envelope before routing onward.

Before dispatching, check that the ticket envelope includes the ticket id, objective,
allowed areas, acceptance criteria, verification expectations, dependency or branch
context, and any human constraints. If those fields are missing or contradictory, keep the
ticket with the master and request clarification instead of opening a worker call.

## Session Start

- Load the canonical `master` skill body from the library repo as the system prompt.
- Provide the full ticket envelope in the user turn, including any prior context or
  constraints from the human.
- Require the master to confirm ticket completeness before worker dispatch. The master
  should not assign work when the ticket lacks clear allowed areas, acceptance criteria, or
  verification expectations.
- Include the output envelope instruction so the master returns a structured handoff
  decision rather than free-form prose.
- Parse the master's `next_recommended_role` field to determine which worker to dispatch
  next; do not infer the handoff from summary text alone.
- If the master requests clarification or surfaces a human approval checkpoint, handle
  that before dispatching any worker.
- Record the full master response before opening the next call; it is your only audit
  trail of the routing decision.

## Worker Dispatch

- Open a new Codex call with the chosen worker skill body as the system prompt.
- Include the full ticket envelope: scoped file list, prior artifacts, current phase, and
  any constraints the master specified.
- Do not carry artifacts from unrelated phases; pass only what the worker needs for this
  assignment to avoid scope confusion.
- Require the worker to stay inside the ticket's `allowed_areas`. If the requested fix
  requires files or behavior outside those boundaries, the worker must report a boundary
  conflict in `findings` and return control instead of expanding scope.
- Include the output envelope instruction and require the worker to list all changed files
  explicitly in the `artifacts` field.
- If the worker returns `status: blocked`, extract the blocker from `findings` and route
  it back to the master rather than attempting to resolve it yourself.
- Record the worker response in full before opening the validator call.

## Validation

- Open a new Codex call with the appropriate validator skill body as the system prompt.
- Provide the full ticket envelope and full worker output — including all artifacts and
  findings — as the user turn; the validator has no other context source.
- Include the output envelope instruction and require the validator to label every finding
  with a severity tier and to return a clear `completed` or `fixes_required` status.
- Require the validator to check ticket boundaries, acceptance criteria, verification
  evidence, and completion-report quality before returning `completed`.
- Read the `status` field before doing anything else; do not advance until you have parsed
  it explicitly.
- If `status` is `completed`, carry the full validator response forward to the master call.
- If `status` is `fixes_required`, do not advance — proceed to the remediation loop below.

## Return to Master

- Open a new Codex call with the master skill body as the system prompt.
- Provide the full ticket envelope and validator result as the user turn, including the full
  findings list and the validator's `next_recommended_role`.
- Include the output envelope instruction so the master returns a structured routing
  decision rather than free-form prose.
- Let the master decide whether to advance to the next phase, request a human approval
  checkpoint, or initiate another worker dispatch.
- If the master surfaces a human approval checkpoint, pause the loop and present the
  summary and findings to the human before continuing.
- Before returning completed work to the human, require a completion report following
  `templates/aegis-execution/templates/shared/completion-report.example.yaml`. The report
  must include changed files, verification evidence or skipped-verification rationale,
  residual findings, and the recommended next role.
- Record the master response before opening any subsequent call.

## Handling fixes_required

When a validator returns `status: fixes_required`, run the following remediation loop
before returning to the master:

- Extract the full `findings` list from the validator response, including severity labels
  and affected locations for every issue.
- Open a new Codex call with the same worker skill as the system prompt. Append the
  validator findings to the user turn after the original ticket envelope so the worker has
  full context on what to fix.
- Require the worker to address every finding explicitly and to list all changed files in
  the `artifacts` field of its response.
- Re-run the same validator against the revised worker output by opening a new Codex call
  with the validator skill as the system prompt and the new worker response as the user
  turn.
- Only return to the master and advance when the validator returns `status: completed`.
  If the second validator pass still returns `fixes_required`, repeat the loop or escalate
  to the master with the full finding history for a routing decision.

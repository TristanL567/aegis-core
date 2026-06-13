# Epic: AEGIS-OVERHAUL — Aegis-Core Overhaul

> Planning artifact. Place this file's envelope at `epics/AEGIS-OVERHAUL/envelope.yaml`
> and each ticket at `epics/AEGIS-OVERHAUL/tickets/AEGIS-OVH-NNN.yaml`, or execute
> directly from this document. Canonical field definitions: `contracts/epic-contract.md`
> and `contracts/ticket-contract.md`.

---

## Epic Envelope

```yaml
epic_id: AEGIS-OVERHAUL

goal: >
  Collapse all human-facing prompt surfaces into a single categorized prompts/
  library with a uniform prompt anatomy and a closed routing state machine;
  promote the supervision and kernel invariants into the canonical contracts;
  add the missing master-validator role; quarantine non-canonical material;
  and make the prompt library and commit invariants mechanically verifiable.
  Preserve the existing architecture: AEGIS.md anchor, contracts/, skills/,
  execution/runbooks/, execution/templates/, tools/.

business_context: >
  Human-facing prompts currently live in four diverging locations
  (execution/prompts/, User-Instructions/, prompt_templates/, docs/), one of
  which contradicts the conformance contract. Entry points are ambiguous for
  humans, and non-canonical folders (sandbox/, to-do/) are visible to
  consuming agents. Enforcement of role locks (planner plans only,
  master-agent supervises only, workers edit) exists informally but is not
  contract-bound or machine-checked.

user_or_operator_outcome: >
  A human operator finds every prompt through one routing table, walks any
  workflow (relay, checkpointed, autonomous) via per-prompt next-step tables
  without thinking about routing, and trusts that binding, role locks, scope
  boundaries, and ticket-bound commits are enforced by contracts, validators,
  and git hooks rather than by memory.

design_concept: >
  One folder per audience. prompts/ is the only human surface, organized by
  lifecycle stage (init, plan, execute, validate, finish, control, providers)
  with operating mode (relay, checkpointed, autonomous) as a sub-axis of
  execute. Prompts invoke roles and cite contracts; they never define
  behavior. Invariants live once in contracts/ (kernel + supervision
  clauses) and are echoed at dispatch via role locks and inline ticket
  blocks. tools/ proves the library is closed and conformant.

architecture_boundary: >
  contracts/, skills/roles/, AEGIS.md, and tools/ may be extended but their
  existing semantics must not be weakened. skills/discipline/,
  skills/procedures/, skills/references/, execution/runbooks/,
  execution/templates/ (except new hooks/), and the orchestration loop are
  preserved. No provider-specific runtime glue enters core behavior files.

success_signal: >
  A new human user can bind an agent, plan an epic, run a ticket in any of
  the three modes, validate, override, commit, and recover a dead session
  using only prompts/README.md and the next-step tables — and
  validate_prompt_library.py plus validate_skill_library.py pass clean.

branch: aegis_overhaul
base: main
autonomy_policy: checkpointed

human_checkpoint_tickets:
  - AEGIS-OVH-003   # contract changes reviewed before prompt migration builds on them
  - AEGIS-OVH-005   # prompts/ scaffold + anatomy approved before mass migration
  - AEGIS-OVH-011   # destructive deletion of legacy surfaces
  - AEGIS-OVH-014   # final conformance pass before merge

epic_allowed_areas:
  - AEGIS.md
  - AGENT_PROMPT.md
  - README.md
  - contracts/
  - skills/roles/
  - prompts/
  - internal/
  - execution/
  - docs/
  - tools/
  - epics/AEGIS-OVERHAUL/

epic_must_not_touch:
  - skills/discipline/
  - skills/procedures/
  - skills/references/
  - epics/AEGIS-PLANNER/
  - epics/AEGIS-PLANNER-AGENT-CONTRACT/
  - .git/

tickets:
  - AEGIS-OVH-001
  - AEGIS-OVH-002
  - AEGIS-OVH-003
  - AEGIS-OVH-004
  - AEGIS-OVH-005
  - AEGIS-OVH-006
  - AEGIS-OVH-007
  - AEGIS-OVH-008
  - AEGIS-OVH-009
  - AEGIS-OVH-010
  - AEGIS-OVH-011
  - AEGIS-OVH-012
  - AEGIS-OVH-013
  - AEGIS-OVH-014

depends_on_epics: []

merge_policy:
  strategy: rebase_then_merge
  base: main
  requires_epic_validator: true   # master-validator applies gate at epic level (OVH-004)
  requires_human_approval: true
```

### Dependency graph

```text
OVH-001 (hygiene/quarantine)
OVH-002 (kernel) ──────────────┐
OVH-003 (contract promotion) ──┤  requires 002
OVH-004 (master-validator) ────┤  requires 003
OVH-005 (prompts scaffold) ────┤  requires 002, 003
OVH-006 (init prompts) ────────┤  requires 005
OVH-007 (plan prompts) ────────┤  requires 005
OVH-008 (execute prompts) ─────┤  requires 005, 003, 004
OVH-009 (validate+finish) ─────┤  requires 005, 004
OVH-010 (control+providers) ───┤  requires 005
OVH-011 (delete legacy) ───────┤  requires 006–010
OVH-012 (prompt validator) ────┤  requires 005 (run after 006–011)
OVH-013 (git hooks) ───────────┤  requires 002
OVH-014 (conformance pass) ────┘  requires all
```

---

## AEGIS-OVH-001 — Repository hygiene and non-canonical quarantine

```yaml
ticket_id: AEGIS-OVH-001
goal: >
  Create internal/ with a non-canonical marker README, move sandbox/ and
  to-do/ into it, and remove the extensionless duplicate file
  prompt_templates/custom_instructions.
dependencies: []
business_context: >
  sandbox/ contains a foreign .agents/skills tree and to-do/ contains roadmap
  notes; both are visible to consuming agents and can be ingested as if
  canonical. A byte-identical extensionless duplicate of
  custom_instructions.md exists.
user_or_operator_outcome: >
  Consuming agents see a repo where every root folder is canonical or
  explicitly marked internal; humans see no leftover artifacts.
design_concept: >
  Quarantine, do not delete: development material stays available under
  internal/ behind a single MUST-NOT-LOAD rule.
architecture_boundary: >
  Pure moves plus one new README. No content edits inside moved folders.
success_signal: >
  Root listing contains no sandbox/ or to-do/; internal/README.md states the
  exclusion rule; no extensionless duplicate remains.
tradeoffs_or_constraints:
  - Use git mv to preserve history.
  - prompt_templates/custom_instructions.md itself is migrated later (OVH-010)
    and deleted later (OVH-011); only the extensionless duplicate is removed here.
allowed_areas:
  - internal/
  - sandbox/
  - to-do/
  - prompt_templates/custom_instructions
must_not_touch:
  - AEGIS.md
  - contracts/
  - skills/
  - execution/
  - docs/
  - prompt_templates/custom_instructions.md
requirements:
  - git mv sandbox internal/sandbox; git mv to-do internal/to-do.
  - internal/README.md states: development and planning material only;
    consuming agents MUST NOT load behavior, skills, or prompts from internal/.
  - git rm prompt_templates/custom_instructions (extensionless file only).
non_goals:
  - Do not edit any file content inside sandbox/ or to-do/.
  - Do not move epics/.
  - Do not update cross-references in other docs (OVH-011 owns reference updates).
acceptance_criteria:
  - internal/sandbox/ and internal/to-do/ exist with full prior contents.
  - internal/README.md exists with the exclusion rule.
  - prompt_templates/ contains exactly one file, custom_instructions.md.
manual_verification_required: true
manual_verification_steps:
  - Confirm git log --follow shows preserved history for a sampled moved file.
verification_commands:
  - git status --short
  - git diff --stat HEAD
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
```

---

## AEGIS-OVH-002 — Invariant kernel contract

```yaml
ticket_id: AEGIS-OVH-002
goal: >
  Author contracts/kernel.md: the single-screen list of AEGIS non-negotiables,
  and reference it from AEGIS.md.
dependencies: []
business_context: >
  The core invariants (goal, dependencies, allowed_areas, must_not_touch, one
  ticket, validator blocking, ticket-bound commits, completion report) are
  scattered across contracts and prompts; a minimal binding needs them in one
  citable place.
user_or_operator_outcome: >
  Any prompt, role, or hook can cite one short file as the irreducible rule
  set; a human can read the entire kernel in under a minute.
design_concept: >
  Kernel = restatement with citations, not new authority. Each kernel item
  links to the contract section that owns its full definition.
architecture_boundary: >
  One new file in contracts/; one new short section plus one Bootstrap Load
  Order entry in AEGIS.md (kernel loads second, after AEGIS.md itself).
  No existing contract text changes.
success_signal: >
  contracts/kernel.md lists 8–10 invariants, one line each plus owning-contract
  citation, and AEGIS.md bootstrap order includes it.
tradeoffs_or_constraints:
  - Hard cap one screen (~40 lines of content).
  - Every item must cite contracts/swarm-contract.md, contracts/ticket-contract.md,
    or contracts/epic-contract.md.
allowed_areas:
  - contracts/kernel.md
  - AEGIS.md
must_not_touch:
  - contracts/swarm-contract.md
  - contracts/ticket-contract.md
  - contracts/epic-contract.md
  - skills/
  - execution/
requirements:
  - "Kernel items (minimum set): (1) ticket envelope before implementation with
    goal, dependencies, allowed_areas, must_not_touch, acceptance criteria,
    verification commands; (2) exactly one ticket at a time; (3) scope: changed
    files inside allowed_areas, never inside must_not_touch; (4) loop:
    master -> worker -> validator -> master preserved; (5) validators blocking;
    human-only override; (6) standard role envelope on every role output;
    (7) full completion report on completion; (8) commits only against a ticket,
    message format '[TICKET-ID] concise description (<=72 chars)';
    (9) supervisors do not edit (forward-reference OVH-003); (10) when intent or
    boundary unclear, block for clarification."
  - AEGIS.md gains a 'Kernel' subsection pointing to contracts/kernel.md and the
    bootstrap order entry.
non_goals:
  - Do not redefine or expand any invariant beyond existing contract semantics.
  - Do not touch the Conformance Gate items (OVH-003 owns gate changes).
acceptance_criteria:
  - contracts/kernel.md exists, one screen, all items cite an owning contract.
  - AEGIS.md Bootstrap Load Order lists contracts/kernel.md at position 2.
manual_verification_required: true
manual_verification_steps:
  - Read kernel end to end; confirm no item conflicts with its cited contract.
verification_commands:
  - git diff -- contracts/kernel.md AEGIS.md
completion_report_required: true
```

---

## AEGIS-OVH-003 — Promote supervision clauses and extend the Conformance Gate

```yaml
ticket_id: AEGIS-OVH-003
goal: >
  Bind the role locks into the canonical contracts: master-planner plans only
  (with the human), master-agent supervises only, all file edits flow through
  workers; extend the AEGIS.md Conformance Gate accordingly.
dependencies:
  - AEGIS-OVH-002 completed
business_context: >
  The no-edit rules for supervisors exist only informally; prompts must cite
  contract clauses rather than author behavior, so the clauses must exist.
user_or_operator_outcome: >
  Autonomous mode is safe by contract: supervisors coordinate, workers edit,
  validators block, and the gate checks it from evidence.
design_concept: >
  Planner -> master-agent -> worker mirrors the edit privilege ladder: only
  the bottom rung writes project files; supervisors write only ledger and
  checkpoint artifacts.
architecture_boundary: >
  Additive clauses in contracts/epic-contract.md (planner, master-agent in
  epic context) and contracts/swarm-contract.md (master never edits project
  files; worker is the only editing role); two new gate items in AEGIS.md.
  No existing clause weakened or removed.
success_signal: >
  Both contracts contain explicit supervisor no-edit clauses with the
  ledger/checkpoint carve-out, and the gate has two new evidence checks.
tradeoffs_or_constraints:
  - Clauses must be evidence-checkable (attributable file edits, dispatch
    references), not intent statements.
allowed_areas:
  - contracts/epic-contract.md
  - contracts/swarm-contract.md
  - contracts/kernel.md
  - AEGIS.md
must_not_touch:
  - contracts/ticket-contract.md
  - skills/
  - execution/
requirements:
  - "epic-contract.md adds: master-planner produces only epic envelopes, ticket
    envelopes, and handoff packages; MUST NOT edit project files, dispatch
    workers directly, or implement. master-agent coordinates; MUST NOT edit
    project files; writable artifacts limited to epic ledger and checkpoint
    files; every implementation is dispatched to a worker selected from
    skills/roles/ by ticket type; every worker result routes through a
    validator before returning."
  - "swarm-contract.md adds: the worker is the only role that edits files inside
    a ticket's allowed_areas; master edits no project files."
  - "AEGIS.md Conformance Gate adds two items: (a) no project-file edits
    attributable to master-planner or master-agent (ledger/checkpoint artifacts
    exempt); (b) every worker dispatch references an existing role path under
    skills/roles/."
  - Update kernel item 9 in contracts/kernel.md to cite the new clauses.
non_goals:
  - Do not modify the orchestration loop runbook.
  - Do not author the master-validator role here (OVH-004).
acceptance_criteria:
  - Both contracts contain the clauses verbatim in sense, with the carve-out.
  - The gate lists exactly two new items matching requirements.
  - kernel.md item 9 cites the new clause locations.
manual_verification_required: true
manual_verification_steps:
  - Confirm no existing MUST clause was weakened (diff review of both contracts).
verification_commands:
  - git diff -- contracts/ AEGIS.md
completion_report_required: true
```

---

## AEGIS-OVH-004 — Author the master-validator role

```yaml
ticket_id: AEGIS-OVH-004
goal: >
  Create skills/roles/master-validator/SKILL.md: the epic-level validator that
  aggregates per-ticket validator verdicts and applies the Conformance Gate
  over the epic ledger.
dependencies:
  - AEGIS-OVH-003 completed
business_context: >
  The relay and autonomous workflows reference a master-validator that does
  not exist in skills/roles/; prompts must not define role behavior, so the
  role must be canonical.
user_or_operator_outcome: >
  Epic completion has an independent gatekeeper that the supervisors do not
  control, in relay and autonomous modes alike.
design_concept: >
  Mirror code-validator one level up: input = epic ledger, ticket completion
  reports, per-ticket validator verdicts; output = standard role envelope with
  epic-level findings; blocking by default; reports to master-planner and human.
architecture_boundary: >
  One new role folder; follow the structure and frontmatter conventions of
  existing skills/roles/* (use code-validator as the template). No edits to
  existing roles.
success_signal: >
  validate_skill_library.py passes with the new role; the role defines inputs,
  gate application, blocking semantics, override recording, and envelope shape.
tradeoffs_or_constraints:
  - The role checks evidence (files, reports, ledger), never re-implements.
  - Must include the two new gate items from OVH-003.
allowed_areas:
  - skills/roles/master-validator/
must_not_touch:
  - skills/roles/master/
  - skills/roles/code-validator/
  - skills/roles/ds-validator/
  - contracts/
  - execution/
requirements:
  - SKILL.md sections: trigger, inputs, procedure (per-ticket verdict
    aggregation -> epic-scope evidence check -> gate application -> findings),
    blocking and override semantics (cite contracts/swarm-contract.md and
    contracts/epic-contract.md), output envelope.
  - MUST NOT edit any file; findings only.
non_goals:
  - Do not change epic-contract semantics (already done in OVH-003).
  - Do not create dispatch prompts for the role (OVH-008/009 own prompts).
acceptance_criteria:
  - skills/roles/master-validator/SKILL.md exists and conforms to library structure.
  - py -3.10 .\tools\validate_skill_library.py passes.
manual_verification_required: true
manual_verification_steps:
  - Compare section structure against code-validator for convention conformance.
verification_commands:
  - py -3.10 .\tools\validate_skill_library.py
  - git diff --stat -- skills/roles/
completion_report_required: true
```

---

## AEGIS-OVH-005 — prompts/ scaffold, routing README, and prompt anatomy

```yaml
ticket_id: AEGIS-OVH-005
goal: >
  Create the prompts/ folder tree (01-init .. 07-providers, 03-execute with
  relay/, checkpointed/, autonomous/), prompts/README.md as routing table and
  mode picker, and prompts/00-conventions.md defining the mandatory prompt
  anatomy.
dependencies:
  - AEGIS-OVH-002 completed
  - AEGIS-OVH-003 completed
business_context: >
  All subsequent migration tickets need the target structure and the uniform
  template to write against; the README is the single human entry surface.
user_or_operator_outcome: >
  A human finds any prompt via two tables (task -> file; mode comparison) and
  every prompt file looks identical in shape.
design_concept: >
  README is a routing table, never a prompt archive. The only prompt text it
  may contain is the canonical invocation, quoted, marked
  'canonical source: prompts/01-init/use-aegis-core.md'.
architecture_boundary: >
  New folder only; placeholder .gitkeep in empty subfolders; no migration of
  prompt content yet.
success_signal: >
  Tree exists; README routes to all planned files (existing or planned-marked);
  conventions file fully specifies frontmatter, sections, and rules.
tradeoffs_or_constraints:
  - Planned-but-not-yet-migrated files are listed in the README with a
    '(pending: OVH-NNN)' marker, removed by the owning tickets.
allowed_areas:
  - prompts/
must_not_touch:
  - execution/
  - User-Instructions/
  - prompt_templates/
  - docs/
  - contracts/
  - skills/
requirements:
  - "Folders: prompts/01-init, 02-plan, 03-execute/relay,
    03-execute/checkpointed, 03-execute/autonomous, 04-validate, 05-finish,
    06-control, 07-providers."
  - "README.md: Table 1 'I want to... -> file' covering every planned prompt;
    Table 2 mode comparison (relay: human routes every handoff, maximum
    overview; checkpointed: agents self-route, human approves at declared
    gates; autonomous: human sees start, checkpoints on error, and end;
    supervisors never edit). One composition paragraph: planner -> master-agent
    -> workers -> validator -> master-validator across modes."
  - "00-conventions.md defines: YAML frontmatter schema (id, stage, mode
    [relay|checkpointed|autonomous|any], audience, target_role, pairs_with,
    requires, returns); mandatory sections (When to use, Preconditions, Prompt
    in a text code block, Expected response, Next step table); placeholder
    syntax [BRACKETS]; inline kernel block format (TICKET/GOAL/DEPENDS_ON/
    ALLOWED_AREAS/MUST_NOT_TOUCH/ACCEPTANCE/VERIFY); rules: prompts invoke
    roles and cite contracts, never define behavior; canonical invocation
    lives in exactly one file; planner-generated relay prompts must themselves
    conform to this template."
non_goals:
  - Do not migrate or write any workflow prompt bodies (OVH-006..010).
  - Do not delete or edit legacy prompt locations.
acceptance_criteria:
  - All folders exist; README and 00-conventions.md complete per requirements.
  - Every README row resolves to an existing file or carries a pending marker.
manual_verification_required: true
manual_verification_steps:
  - Walk Table 1 as a new user; confirm each task phrase is unambiguous.
verification_commands:
  - git status --short -- prompts/
completion_report_required: true
```

---

## AEGIS-OVH-006 — Init prompts (binding layer)

```yaml
ticket_id: AEGIS-OVH-006
goal: >
  Author prompts/01-init/: use-aegis-core.md (with binding handshake),
  verify-binding.md, bind-strict.md, apply-to-project.md.
dependencies:
  - AEGIS-OVH-005 completed
business_context: >
  Binding is the enforcement entry point; the handshake (agent restates its
  load, role locks, and ticket state before any work) is the strongest
  prompt-level adherence mechanism.
user_or_operator_outcome: >
  The human binds any agent runtime with one paste and can reject a
  non-conformant session before work begins; verify-binding re-checks
  mid-session.
design_concept: >
  use-aegis-core demands a BINDING ACKNOWLEDGMENT: (1) bootstrap files loaded
  in order with first heading each; (2) session role and its three MUST NOTs;
  (3) the ticket envelope to work from, or the blocking missing fields. No
  planning, editing, or proposing before acceptance.
architecture_boundary: >
  Content migrates and supersedes execution/prompts/use-aegis-core.md and
  apply-to-project.md; legacy files untouched until OVH-011. All four files
  conform to 00-conventions.md.
success_signal: >
  Canonical invocation string exists only in use-aegis-core.md; all four
  prompts carry conforming frontmatter and next-step tables.
tradeoffs_or_constraints:
  - bind-strict.md is the hardened variant; refuse all work until the
    acknowledgment is explicitly accepted by the human.
  - verify-binding.md is paste-anytime; demands restatement of role locks and
    current ticket scope.
allowed_areas:
  - prompts/01-init/
  - prompts/README.md
must_not_touch:
  - execution/
  - contracts/
  - skills/
  - AEGIS.md
requirements:
  - All files conform to the 00-conventions anatomy.
  - use-aegis-core.md cites contracts/kernel.md and the AEGIS.md gate;
    Next-step routes to 02-plan or 03-execute depending on acknowledgment.
  - apply-to-project.md includes the hook-install step placeholder
    '(pending: OVH-013)'.
  - Remove the pending markers for these four files from prompts/README.md.
non_goals:
  - Do not delete legacy prompt files.
  - Do not embed contract or role text bodies; cite paths.
acceptance_criteria:
  - Four conforming files exist; invocation single-sourced; README rows live.
manual_verification_required: true
manual_verification_steps:
  - Paste use-aegis-core.md into a fresh agent session against this repo and
    confirm a correct BINDING ACKNOWLEDGMENT is producible from repo content.
verification_commands:
  - git diff -- prompts/
completion_report_required: true
```

---

## AEGIS-OVH-007 — Plan prompts (master-planner layer)

```yaml
ticket_id: AEGIS-OVH-007
goal: >
  Author prompts/02-plan/: init-master-planner.md, epic-from-idea.md,
  ticket-from-idea.md, planner-handoff.md (handoff package format).
dependencies:
  - AEGIS-OVH-005 completed
business_context: >
  Workflow: the master-planner plans epics and tickets with the human only;
  in relay mode its product is a package of ready-to-paste dispatch prompts.
user_or_operator_outcome: >
  The human turns an idea into an epic or single ticket through a guided
  planner session and receives a handoff package needing zero manual prompt
  assembly.
design_concept: >
  planner-handoff.md specifies the package: ordered list of relay prompts,
  each conforming to 00-conventions with placeholders pre-filled and the
  inline kernel block populated from the ticket envelopes, plus the envelope
  files themselves and the routing order.
architecture_boundary: >
  Prompts cite contracts/epic-contract.md planner clauses (OVH-003) for the
  role lock; they do not restate planner behavior beyond the lock block.
success_signal: >
  A planner session driven by init-master-planner.md yields envelopes
  conforming to execution/templates/ and a package conforming to
  planner-handoff.md.
tradeoffs_or_constraints:
  - init-master-planner.md requires the human to declare mode and autonomy
    policy (manual | checkpointed | autonomous_until_error) up front.
  - "Planner role lock block (top of every planner prompt): plans only, with
    the human; MUST NOT edit files, dispatch workers, or implement; artifacts
    limited to envelopes and handoff packages. (Binding: contracts/epic-contract.md)"
allowed_areas:
  - prompts/02-plan/
  - prompts/README.md
must_not_touch:
  - execution/
  - contracts/
  - skills/
  - epics/
requirements:
  - All files conform to 00-conventions anatomy with next-step tables
    (epic-from-idea -> planner-handoff -> 03-execute/<mode>/...).
  - epic-from-idea.md and ticket-from-idea.md require outputs matching
    execution/templates/epic-envelope.example.yaml and
    ticket-envelope.example.yaml field sets.
  - Remove the four pending markers from prompts/README.md.
non_goals:
  - Do not modify the envelope templates.
  - Do not author execute-stage relay prompts (OVH-008).
acceptance_criteria:
  - Four conforming files exist; handoff package format fully specified
    (contents, ordering, naming, kernel-block population rule).
manual_verification_required: true
manual_verification_steps:
  - Dry-run epic-from-idea.md on a toy idea; confirm envelope field coverage.
verification_commands:
  - git diff -- prompts/
completion_report_required: true
```

---

## AEGIS-OVH-008 — Execute prompts (relay, checkpointed, autonomous)

```yaml
ticket_id: AEGIS-OVH-008
goal: >
  Author prompts/03-execute/: relay/ (dispatch-master-agent, relay-to-worker,
  relay-to-validator, relay-to-master-validator), checkpointed/
  (run-ticket-checkpointed, resume-from-checkpoint), autonomous/
  (run-epic-autonomous, supervision-contract, resume-from-ledger).
dependencies:
  - AEGIS-OVH-003 completed
  - AEGIS-OVH-004 completed
  - AEGIS-OVH-005 completed
business_context: >
  These are the two workflows the operator validated in practice (human-routed
  relay; fully autonomous with non-editing supervisors) plus the checkpointed
  middle mode implied by the existing autonomy policy.
user_or_operator_outcome: >
  In relay mode the human routes blindly via next-step tables; in autonomous
  mode one paste runs an epic under contract-bound supervision; checkpointed
  stops at declared gates.
design_concept: >
  Every dispatch prompt opens with the role lock block citing OVH-003 clauses
  and embeds the inline kernel block (actual ticket fields, not a path).
  Next-step tables condition on the returned envelope (status / 
  next_recommended_role), making relay a closed state machine.
architecture_boundary: >
  supervision-contract.md cites contracts/epic-contract.md and
  contracts/swarm-contract.md clauses; it owns no behavior. Prompts supersede
  execution/prompts/start-master.md and start-ticket-run.md (legacy untouched
  until OVH-011).
success_signal: >
  A full relay walk (dispatch-master-agent -> relay-to-worker ->
  relay-to-validator -> relay-to-master-validator) is possible following only
  next-step tables; run-epic-autonomous references supervision-contract and
  halts to 06-control/halt.md semantics on gate failure.
tradeoffs_or_constraints:
  - Master-agent dispatch must instruct worker selection from skills/roles/ by
    ticket type, spawn-or-reuse, with the dispatch citing the role path.
  - Autonomous prompts must require ledger writes at every transition so
    resume-from-ledger and recover-context (OVH-010) have state to rebuild.
allowed_areas:
  - prompts/03-execute/
  - prompts/README.md
must_not_touch:
  - execution/
  - contracts/
  - skills/
  - AEGIS.md
requirements:
  - All nine files conform to 00-conventions anatomy.
  - All dispatch prompts include role lock block + inline kernel block
    placeholders + Expected response (standard role envelope) + Next step table.
  - relay-to-master-validator.md targets skills/roles/master-validator/.
  - Remove pending markers from prompts/README.md.
non_goals:
  - Do not modify execution/runbooks/shared-orchestration-loop.md (prompts cite it).
  - Do not author halt/recover prompts (OVH-010).
acceptance_criteria:
  - Nine conforming files; every target_role resolves to an existing
    skills/roles/ path; every Next-step reference resolves to an existing or
    pending-marked prompt file.
manual_verification_required: true
manual_verification_steps:
  - Tabletop a relay run on a toy ticket; confirm no routing dead end.
verification_commands:
  - git diff -- prompts/
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
```

---

## AEGIS-OVH-009 — Validate and finish prompts

```yaml
ticket_id: AEGIS-OVH-009
goal: >
  Author prompts/04-validate/ (validate-ticket, conformance-check,
  authorize-override, drift-correction) and prompts/05-finish/
  (completion-report, clean-commit, close-epic).
dependencies:
  - AEGIS-OVH-004 completed
  - AEGIS-OVH-005 completed
business_context: >
  The contracts require human-only validator overrides, but no prompt for
  authorizing one exists; drift correction and epic closure are likewise
  unprompted today.
user_or_operator_outcome: >
  The human can route validation, record a conformant override (finding ID,
  justification, residual risk), halt scope drift, and close an epic with a
  reconciled ledger.
design_concept: >
  authorize-override.md makes the override expensive and auditable by
  construction; drift-correction.md is the paste for 'you left allowed_areas:
  halt, report changed files, await re-scope'.
architecture_boundary: >
  validate-ticket, conformance-check, completion-report, clean-commit migrate
  and supersede their execution/prompts/ counterparts (legacy untouched until
  OVH-011). close-epic requires master-validator approval before ledger close.
success_signal: >
  Seven conforming files; override prompt captures finding ID, justification,
  residual risk, and instructs the master to record it per
  contracts/swarm-contract.md.
tradeoffs_or_constraints:
  - clean-commit.md enforces the kernel commit format
    '[TICKET-ID] concise description (<=72 chars)' and cites contracts/kernel.md.
allowed_areas:
  - prompts/04-validate/
  - prompts/05-finish/
  - prompts/README.md
must_not_touch:
  - execution/
  - contracts/
  - skills/
requirements:
  - All files conform to 00-conventions anatomy with next-step tables
    (validate -> finish on approval; validate -> authorize-override or back to
    execute on findings).
  - conformance-check.md walks the full AEGIS.md gate including the two
    OVH-003 items.
  - Remove pending markers from prompts/README.md.
non_goals:
  - Do not weaken validator-blocking semantics in any phrasing.
acceptance_criteria:
  - Seven conforming files; override and drift prompts exist with required fields.
manual_verification_required: true
manual_verification_steps:
  - Confirm authorize-override.md cannot be completed without a finding ID.
verification_commands:
  - git diff -- prompts/
completion_report_required: true
```

---

## AEGIS-OVH-010 — Control and provider prompts

```yaml
ticket_id: AEGIS-OVH-010
goal: >
  Author prompts/06-control/ (status-report, halt, recover-context) and
  prompts/07-providers/ (claude-code-setup, codex-setup, antigravity-setup,
  custom-instructions rewritten against current contracts).
dependencies:
  - AEGIS-OVH-005 completed
business_context: >
  Sessions die and contexts overflow; recovery must be a paste, not an
  improvisation. prompt_templates/custom_instructions.md teaches a
  pre-ticket-era workflow and is the most dangerous file in the repo.
user_or_operator_outcome: >
  The human can demand ledger-format status, halt gracefully with persisted
  state, and rebuild a dead session from ledger + envelopes + completion
  reports; provider setups map AEGIS roles onto each runtime.
design_concept: >
  custom-instructions.md is rewritten from scratch: it must reference the
  binding handshake, ticket envelope, role locks, and gate — zero 'activate
  the skill and break work into phases' residue.
architecture_boundary: >
  Provider prompts may describe runtime mapping (e.g. Claude Code subagents
  and git worktrees for parallel masters) but keep all behavior citations
  pointing at contracts/ and skills/; supersede
  execution/prompts/claude-code-agent-setup.md and
  antigravity-master-session.md, and execution/runbooks/codex.md prompt
  content where applicable (legacy untouched until OVH-011).
success_signal: >
  Seven conforming files; recover-context rebuilds role, mode, active ticket,
  and next step from artifacts alone; custom-instructions contains the word
  'ticket' and cites contracts/kernel.md.
tradeoffs_or_constraints:
  - recover-context.md must work in all three modes (relay resumes at the next
    next-step row; autonomous resumes from ledger).
allowed_areas:
  - prompts/06-control/
  - prompts/07-providers/
  - prompts/README.md
must_not_touch:
  - execution/
  - prompt_templates/
  - contracts/
  - skills/
requirements:
  - All files conform to 00-conventions anatomy.
  - status-report.md demands output in the epic-ledger format of
    execution/templates/epic-ledger.example.md.
  - Remove pending markers from prompts/README.md.
non_goals:
  - Do not add provider-specific behavior to core files.
  - Do not delete prompt_templates/ (OVH-011).
acceptance_criteria:
  - Seven conforming files exist; custom-instructions has no legacy phrasing.
manual_verification_required: true
manual_verification_steps:
  - Diff new custom-instructions against prompt_templates/custom_instructions.md;
    confirm full conceptual replacement.
verification_commands:
  - git diff -- prompts/
completion_report_required: true
```

---

## AEGIS-OVH-011 — Delete legacy prompt surfaces and update all references

```yaml
ticket_id: AEGIS-OVH-011
goal: >
  Remove execution/prompts/, User-Instructions/, and prompt_templates/; merge
  docs/human-usage-guide.md into prompts/README.md; update every path
  reference in AEGIS.md, AGENT_PROMPT.md, README.md, docs/, and
  execution/runbooks/ to the new prompts/ locations.
dependencies:
  - AEGIS-OVH-006 completed
  - AEGIS-OVH-007 completed
  - AEGIS-OVH-008 completed
  - AEGIS-OVH-009 completed
  - AEGIS-OVH-010 completed
business_context: >
  Four diverging prompt surfaces are the root usability defect; they must die
  in one auditable step after migration is verified.
user_or_operator_outcome: >
  Exactly one human surface remains; no link or doc points at a deleted path.
design_concept: >
  Deletion is gated on a pre-check that every legacy prompt has a successor in
  prompts/ (or a recorded decision to drop it), enumerated in the completion report.
architecture_boundary: >
  Root README is rewritten to one page: what AEGIS is; humans -> prompts/,
  agents -> AEGIS.md. AGENT_PROMPT.md and AEGIS.md path updates only — no
  semantic changes to the contract or gate.
success_signal: >
  Repo-wide search finds zero references to execution/prompts/,
  User-Instructions/, or prompt_templates/; human-usage-guide content lives in
  prompts/README.md; docs/human-usage-guide.md removed or reduced to a pointer.
tradeoffs_or_constraints:
  - git rm, not filesystem delete; one commit for deletions, one for reference
    updates, both ticket-bound.
allowed_areas:
  - execution/prompts/
  - User-Instructions/
  - prompt_templates/
  - prompts/README.md
  - docs/
  - AEGIS.md
  - AGENT_PROMPT.md
  - README.md
  - execution/runbooks/
must_not_touch:
  - contracts/
  - skills/
  - prompts/01-init/
  - prompts/02-plan/
  - prompts/03-execute/
  - prompts/04-validate/
  - prompts/05-finish/
  - prompts/06-control/
  - prompts/07-providers/
  - execution/templates/
requirements:
  - Pre-deletion mapping table (legacy file -> successor | dropped+reason) in
    the completion report.
  - runbook edits limited to path-reference updates; no procedural changes.
  - AEGIS.md 'Canonical Sources' and invocation pointer updated to
    prompts/01-init/use-aegis-core.md.
non_goals:
  - Do not alter prompt bodies under prompts/ beyond the README merge.
  - Do not change runbook procedure content.
acceptance_criteria:
  - "grep -r for the three legacy paths returns only matches inside
    epics/AEGIS-OVERHAUL/ (this epic's own planning text) and internal/."
  - Root README <= 1 page with the two-audience pointer.
manual_verification_required: true
manual_verification_steps:
  - Click-walk every link in README.md, AEGIS.md, AGENT_PROMPT.md, prompts/README.md.
verification_commands:
  - git grep -n "execution/prompts/" -- . ':!epics/AEGIS-OVERHAUL' ':!internal'
  - git grep -n "User-Instructions" -- . ':!epics/AEGIS-OVERHAUL' ':!internal'
  - git grep -n "prompt_templates" -- . ':!epics/AEGIS-OVERHAUL' ':!internal'
completion_report_required: true
```

---

## AEGIS-OVH-012 — Prompt library validator

```yaml
ticket_id: AEGIS-OVH-012
goal: >
  Implement tools/validate_prompt_library.py proving the prompt library is
  uniform and the routing state machine is closed.
dependencies:
  - AEGIS-OVH-005 completed
business_context: >
  The restructure must become an enforced invariant, not a one-time cleanup;
  drift, dangling roles, and dead-end routing must fail mechanically.
user_or_operator_outcome: >
  One command tells the operator the prompt library is conformant; CI-ready
  exit codes.
design_concept: >
  Pure-stdlib Python in the style of the existing tools/ validators; checks
  are file-evidence based.
architecture_boundary: >
  One new script in tools/; optionally a short usage note in docs/testing.md.
success_signal: >
  Validator passes on the migrated library and demonstrably fails on each
  seeded defect class.
tradeoffs_or_constraints:
  - Stdlib-only frontmatter parsing (no external YAML dependency) acceptable;
    document the simplification.
allowed_areas:
  - tools/validate_prompt_library.py
  - docs/testing.md
must_not_touch:
  - prompts/
  - contracts/
  - skills/
  - tools/validate_skill_library.py
  - tools/validate_ticket_scope.py
requirements:
  - "Checks: (1) every prompts/**/*.md except README and 00-conventions has
    frontmatter with id, stage, mode, audience, target_role, pairs_with,
    requires, returns; (2) every target_role resolves to an existing
    skills/roles/<role>/SKILL.md or 'none'; (3) every pairs_with path exists;
    (4) every Next-step file reference resolves inside prompts/; (5) the
    canonical invocation string occurs in exactly one file
    (prompts/01-init/use-aegis-core.md) plus at most one quoted occurrence in
    prompts/README.md, and the two strings are identical; (6) mandatory
    sections present (When to use, Preconditions, Prompt, Expected response,
    Next step); (7) every file under prompts/03-execute/ contains the inline
    kernel block placeholders; (8) prompts/README.md Table 1 rows all resolve;
    no pending markers remain; (9) no two prompt files share an id; (10) no
    file under prompts/ defines role behavior markers (heuristic: forbid
    'You are the canonical definition' style ownership claims; cite-only)."
  - Exit 0 clean / 1 violations with file:line diagnostics; runnable as
    py -3.10 .\tools\validate_prompt_library.py.
non_goals:
  - Do not validate skills/ structure (existing tool owns it).
  - Do not auto-fix; report only.
acceptance_criteria:
  - All ten checks implemented; clean pass on migrated library; each check
    proven by a temporary seeded failure during ticket verification (reverted).
manual_verification_required: true
manual_verification_steps:
  - Seed one defect per check class in a scratch copy; confirm detection.
verification_commands:
  - py -3.10 .\tools\validate_prompt_library.py
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
```

---

## AEGIS-OVH-013 — Git hook templates for mechanical kernel enforcement

```yaml
ticket_id: AEGIS-OVH-013
goal: >
  Ship execution/templates/hooks/ with commit-msg (ticket-bound commit format)
  and pre-commit (staged paths vs active-ticket scope, wiring
  validate_ticket_scope.py), plus an install step in
  prompts/01-init/apply-to-project.md.
dependencies:
  - AEGIS-OVH-002 completed
  - AEGIS-OVH-006 completed
business_context: >
  Prompts and validators are LLMs checking LLMs; commit-level invariants need
  a layer that cannot be talked out of compliance.
user_or_operator_outcome: >
  In a target project with hooks installed, a commit without a valid
  '[TICKET-ID] description' or touching out-of-scope paths is physically rejected.
design_concept: >
  Hooks are templates the human installs in the target project; AEGIS-CORE
  ships them, never installs them silently. Active ticket is identified via a
  documented convention (e.g. .aegis/active-ticket file in the target repo).
architecture_boundary: >
  New files under execution/templates/hooks/ only, plus the install section in
  apply-to-project.md and a usage note in docs/testing.md. No changes to
  tools/validate_ticket_scope.py.
success_signal: >
  Local test repo rejects a malformed commit message and an out-of-scope
  staged file; accepts a conformant commit.
tradeoffs_or_constraints:
  - Hooks must run cross-platform (Git Bash on Windows); keep to POSIX sh +
    python invocation; document the py/python3 launcher difference.
  - Commit regex: ^\[[A-Z0-9-]+\] .{1,72}$ and the referenced ticket file must
    exist under the target's ticket directory (path configurable in hook header).
allowed_areas:
  - execution/templates/hooks/
  - prompts/01-init/apply-to-project.md
  - docs/testing.md
must_not_touch:
  - tools/
  - contracts/
  - skills/
  - prompts/02-plan/
  - prompts/03-execute/
requirements:
  - hooks/README.md documents install (copy to .git/hooks or core.hooksPath),
    configuration header variables, and the .aegis/active-ticket convention.
  - apply-to-project.md replaces its '(pending: OVH-013)' placeholder with the
    install step.
non_goals:
  - Do not enforce hooks inside aegis-core's own repo by default.
  - Do not add CI pipeline configs (out of scope; note as follow-up).
acceptance_criteria:
  - Both hooks + README exist; demonstrated accept/reject behavior recorded in
    the completion report from a scratch target repo.
manual_verification_required: true
manual_verification_steps:
  - Scratch repo: install hooks, attempt bad-message commit, out-of-scope
    commit, then conformant commit; record all three outcomes.
verification_commands:
  - git diff --stat -- execution/templates/hooks/ prompts/01-init/apply-to-project.md
completion_report_required: true
```

---

## AEGIS-OVH-014 — Final conformance pass and epic closure

```yaml
ticket_id: AEGIS-OVH-014
goal: >
  Run all validators, verify the full link graph, tabletop one end-to-end walk
  per mode, and produce the epic-level conformance evidence for
  master-validator review.
dependencies:
  - AEGIS-OVH-001 completed
  - AEGIS-OVH-011 completed
  - AEGIS-OVH-012 completed
  - AEGIS-OVH-013 completed
business_context: >
  The epic's promise is 'clean and easy to use'; that is only credible with an
  end-state audit independent of the per-ticket validations.
user_or_operator_outcome: >
  The human merges aegis_overhaul knowing the structure validators pass, no
  dead links exist, and each mode walks end to end.
design_concept: >
  This ticket produces evidence and at most trivial fixes (typos, broken
  links). Any substantive defect is reported as a finding and spawns a new
  ticket; it is not fixed here.
architecture_boundary: >
  Read-mostly. Write access only for link/typo fixes inside prompts/, docs/,
  README.md.
success_signal: >
  Both validators exit 0; legacy-path greps clean; three tabletop transcripts
  (relay, checkpointed, autonomous on a toy ticket/epic) attached to the
  completion report; master-validator envelope returned.
tradeoffs_or_constraints:
  - Fix-here threshold: single-line, semantics-free changes only.
allowed_areas:
  - prompts/
  - docs/
  - README.md
must_not_touch:
  - contracts/
  - skills/
  - tools/
  - execution/
requirements:
  - Run py -3.10 .\tools\validate_prompt_library.py and
    py -3.10 .\tools\validate_skill_library.py; both must pass.
  - Re-run the three OVH-011 git grep checks; must be clean.
  - Tabletop transcripts demonstrate no routing dead end in any mode.
  - Route the epic through skills/roles/master-validator/ per OVH-004 before
    declaring the epic complete.
non_goals:
  - No substantive content or structure changes.
acceptance_criteria:
  - All commands exit 0; transcripts attached; master-validator approval (or
    human-authorized override) recorded in the epic ledger.
manual_verification_required: true
manual_verification_steps:
  - Human reads prompts/README.md cold and completes the relay tabletop
    unaided; record friction points as findings.
verification_commands:
  - py -3.10 .\tools\validate_prompt_library.py
  - py -3.10 .\tools\validate_skill_library.py
  - git grep -n "execution/prompts/" -- . ':!epics/AEGIS-OVERHAUL' ':!internal'
completion_report_required: true
```

---

## Execution notes for the master-planner

- Suggested batches respecting dependencies: **B1** = 001, 002 → **B2** = 003 (checkpoint), 004, 013-prep → **B3** = 005 (checkpoint) → **B4** = 006–010 (parallelizable across workers; disjoint allowed_areas) → **B5** = 011 (checkpoint), 012, 013 → **B6** = 014 (checkpoint).
- 006–010 are deliberately scoped to disjoint `prompts/` subfolders so multiple workers can run in parallel under one master-agent without scope collision; only `prompts/README.md` is shared — serialize README edits or assign README pending-marker removal to a single worker per batch.
- Every commit on `aegis_overhaul` uses the kernel format: `[AEGIS-OVH-NNN] concise description`.
- Validator routing: code-validator for 012 and 013 (scripts/hooks); code-validator or a docs-capable validator for 001–011; master-validator (once 004 lands) for the epic gate at 014.

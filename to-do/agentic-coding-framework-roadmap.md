# AEGIS Agentic Coding Framework Roadmap

This document collects follow-up work for the AEGIS framework after the move toward a single `aegis-core` repository. The goal is to keep agentic coding controlled, reviewable, and useful to the human operator.

## Current Direction

AEGIS should stay ticket-driven:

- one ticket at a time;
- one branch or clearly declared integration branch;
- explicit `allowed_areas` and `must_not_touch`;
- small diffs;
- validator gate before completion;
- clean commit with ticket ID, goal, acceptance criteria, and validation evidence.

The framework should help a human keep overview. Do not optimize for autonomous volume before the scope, audit trail, and review workflow are solid.

## To-Do Backlog

### TODO-001: Revise Worker Skill Architecture

Goal: collapse the current worker set to the most important durable roles, then expand technical depth through reusable skillsets rather than many shallow worker prompts.

Current problem:

- too many narrowly named workers can become hard to route;
- too few technical details make workers generic;
- duplicated guidance across workers increases drift.

Recommended shape:

- `master`: unchanged, owns routing, human approval, ticket state, and validator loops.
- `ticket-planner-worker`: keeps backlog and ticket generation.
- `engineering-worker`: handles code implementation with declared technical mode.
- `artifact-worker`: handles docs, prompts, charts, reports, and non-code artifacts.
- `analysis-worker`: handles data/model interpretation, diagnostics, and research-style outputs.
- `code-validator`: general validation gate.
- optional specialized validators later: security, data science, UX, architecture.

Add technical skillsets as reusable references, for example:

- `skills/_skillsets/backend.md`
- `skills/_skillsets/frontend.md`
- `skills/_skillsets/testing.md`
- `skills/_skillsets/data-pipelines.md`
- `skills/_skillsets/ml-analysis.md`
- `skills/_skillsets/infra.md`
- `skills/_skillsets/docs-and-prompts.md`

Each skillset should explain:

- what this type of work owns;
- common files and boundaries;
- expected tests or validation;
- typical failure modes;
- what to refuse or route back to master;
- concise implementation style rules.

Prompt:

```text
You are the AEGIS master-agent.

Task: create a ticket backlog for revising the worker skill architecture.

Goal:
Collapse the worker set to a smaller number of durable worker roles while adding deeper technical skillsets that workers can reference.

Constraints:
- Do not edit files yet.
- Preserve master -> worker -> validator -> master.
- Preserve ticket-based execution.
- Keep skills provider-agnostic.
- Do not remove existing skills until migration tickets exist.

Produce:
- recommended target role taxonomy;
- mapping from current skills to target roles;
- proposed `_skillsets/` documents;
- migration tickets with allowed_areas, must_not_touch, requirements, non_goals, acceptance_criteria, verification_commands, and completion_report_required.
```

### TODO-002: Define Project Access Model

Goal: document how other projects access and apply AEGIS without copying stale prompts everywhere.

Supported access patterns to evaluate:

- Git submodule: target project includes `aegis-core` as a submodule.
- Git clone path: target project references a local `aegis-core` checkout.
- Versioned snapshot: target project copies selected prompts/templates for a release.
- Package-style distribution later: scripts or packaged templates expose stable commands.

Recommended first version:

- target projects reference a local or sibling `aegis-core` path;
- target project has a small `.aegis/project.yaml` manifest;
- prompts point back to canonical files in `aegis-core`;
- target project never edits canonical AEGIS files during application work.

Example manifest fields:

```yaml
project_label: MT project
aegis_core_path: ../aegis-core
default_branch: main
work_branch_prefix: aegis/
validation_commands:
  - <project-specific command>
manual_verification:
  required: true
  examples:
    - UI smoke test
    - notebook/model output review
must_not_touch:
  - secrets
  - production data
  - generated artifacts
```

Prompt:

```text
You are the AEGIS master-agent.

Task: plan how a target project should access and use aegis-core.

Target project label:
<for example, MT project>

Known context:
<paste project structure, branch, validation commands, and constraints>

Requirements:
- Keep AEGIS canonical files in aegis-core.
- Do not copy full skill bodies unless explicitly required.
- Define how the target project references aegis-core.
- Define the target project's .aegis/project.yaml shape.
- Define how ticket envelopes include project-specific allowed_areas, must_not_touch, validation_commands, and manual_verification.

Return:
- recommended access mode;
- required target project files;
- setup tickets;
- risks and blockers.
```

### TODO-003: Enforce Human-Readable Code and Limited Scope

Goal: make every implementation ticket produce concise, reviewable code and a small audit trail.

Rules to add to execution guidance:

- Every code ticket starts from a branch named for the ticket.
- Every code ticket declares exact allowed areas.
- Every worker reports the final changed files.
- Every validator checks for unrelated refactors and unnecessary abstractions.
- Every completion report includes a human-readable diff summary.
- If code became longer or more abstract, the worker must justify why.
- No broad cleanup, formatting, or dependency changes unless the ticket explicitly owns them.

Potential addition to completion reports:

```yaml
human_readability:
  concise: true
  unnecessary_elements_removed: true
  abstraction_added: false
  abstraction_rationale: null
  reviewer_notes:
    - <short explanation of the change in human terms>
```

Prompt:

```text
You are the AEGIS master-agent.

Task: create tickets that enforce human-readable, concise implementation work.

Requirements:
- Every implementation ticket must be branch-aware.
- Every worker must preserve limited scope.
- Every validator must check for unnecessary abstractions, unrelated refactors, broad formatting, and hidden dependency changes.
- Completion reports must include a human-readable diff summary.

Produce:
- contract updates if needed;
- validator updates if needed;
- execution prompt updates if needed;
- clean commit workflow updates if needed;
- one-ticket-at-a-time migration plan.
```

## Useful Framework Expansions

### Project Manifest

Add optional `.aegis/project.yaml` support for target projects. This gives the master a stable place to read project label, branch conventions, validation commands, manual checks, protected paths, and local AEGIS path.

Revalidation: high value, low risk. This should be one of the next major additions because it reduces repeated prompt setup and prevents private paths from leaking into reusable docs.

### Ticket Ledger

Maintain a local ticket ledger such as `aegis/tickets/` in the target project, with one markdown or YAML file per ticket.

Revalidation: high value, medium risk. It improves traceability, but only if kept lightweight. Avoid building a complex issue tracker too early.

### Definition of Ready and Definition of Done

Add standard readiness and done checks for tickets.

Ready means:

- goal is clear;
- dependencies are known;
- allowed areas and must-not-touch are explicit;
- validation commands are known;
- manual verification is declared.

Done means:

- worker completed only the ticket;
- validator approved or human override is recorded;
- completion report exists;
- commit contains only ticket-owned files.

Revalidation: high value, low risk. This directly addresses AI slope.

### Scope Firewall Tooling

Create a small script that checks changed files against a ticket envelope before staging or commit.

Possible command:

```powershell
py -3.10 .\tools\validate_ticket_scope.py --ticket path\to\ticket.yaml
```

Revalidation: high value, medium risk. Useful once ticket files exist on disk. Do not build before the ticket storage format is settled.

### Diff Narrator

Require a short human-readable explanation of the diff:

- what changed;
- why it changed;
- what did not change;
- how to verify;
- what follow-up was intentionally deferred.

Revalidation: high value, low risk. This can be added to completion reports before any tooling exists.

### ADR and Decision Log Support

For architecture changes, require a lightweight decision record instead of letting implementation tickets silently introduce architecture.

Revalidation: high value for larger projects, medium risk for small changes. Keep it optional and triggered by architecture-impacting tickets.

### Validator Matrix

Use different validators based on risk:

- code validator for general correctness;
- security validator for auth, secrets, permissions, input handling;
- data validator for data science, leakage, metrics, reproducibility;
- UX validator for frontend workflows and manual visual checks;
- architecture validator for cross-module contracts.

Revalidation: high value, but only after the worker taxonomy is cleaned up. Too many validators too early creates process drag.

### Project Onboarding Report

Before first ticket in a new project, generate a short onboarding report:

- repo structure;
- test commands;
- build commands;
- deployment constraints;
- protected areas;
- likely worker skillsets;
- suggested first tickets.

Revalidation: high value, low risk. This is useful for MT and any future project.

### Prompt Evaluation Tests

Add small prompt tests that check whether a master, worker, or validator response contains required envelope fields and refuses out-of-scope work.

Revalidation: medium value, medium risk. Useful once prompts stabilize. Avoid brittle tests that assert exact prose.

### Run Log and Audit Trail

Store per-ticket run logs:

- ticket envelope;
- worker result;
- validator result;
- completion report;
- commit SHA.

Revalidation: high value, medium risk. This is the real antidote to losing overview. Keep the format simple.

### Risk Labels

Add standard labels to tickets:

- `risk:low`
- `risk:medium`
- `risk:high`
- `requires:manual-verification`
- `requires:security-validator`
- `requires:data-validator`
- `scope:docs`
- `scope:code`
- `scope:infra`

Revalidation: medium value, low risk. Useful if it stays simple and informs validator selection.

## Collaboration and Software Engineering Ideas

- Use small RFCs for features before ticket backlogs.
- Keep a project glossary for domain terms.
- Add review checklists per technology area.
- Add release-note generation from completed tickets.
- Add migration playbooks for database or API contract changes.
- Add incident-style postmortems when an AI change causes regression.
- Add dependency-change policy: no new dependencies without explicit ticket approval.
- Add generated-file policy: generated files can only change when named in `allowed_areas`.
- Add branch naming convention: `aegis/<ticket-id>-short-name`.
- Add commit convention: ticket ID, goal, acceptance, validation.
- Add periodic framework retrospectives: what slowed the human down, what improved clarity, what created noise.

## Revalidated Priority Order

1. Define the target worker taxonomy and technical skillsets.
2. Add project access model and `.aegis/project.yaml`.
3. Add definition of ready/done and human-readable diff summary.
4. Add ticket ledger and run log format.
5. Add scope firewall tooling.
6. Add specialized validators only after the worker taxonomy is stable.
7. Add prompt evaluation tests after prompt formats settle.

Avoid adding heavy automation before the process is clear. The framework should first make the human's overview stronger, then automate the parts that are already stable.

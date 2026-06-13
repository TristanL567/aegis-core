---
standalone: true
trigger:
  - "A new or unfamiliar target project needs graph or context evidence before ticket planning, onboarding, or first implementation."
  - "An architecture-impacting ticket, module-boundary uncertainty, domain or business flow discovery, or diff impact review needs broader system context than local code reading provides."
  - "Understand Anything or comparable map evidence is available and can answer a bounded ticket question without expanding scope."
non_trigger:
  - "The ticket is small, mechanical, or already has enough local context from nearby files, tests, docs, or user-provided evidence."
  - "The task is implementation, refactoring, validation, or code reading that can proceed safely without graph/context evidence."
  - "Graph exploration would expand the ticket beyond allowed_areas or distract from a narrow acceptance criterion."
  - "Understand Anything is not installed or available; this procedure does not install or run external tools by itself."
failure_modes_addressed:
  - "AI changes a system it does not understand because it skipped available architecture, dependency, domain-flow, or impact context."
  - "Graph exploration becomes false authority or scope expansion instead of bounded evidence for an AEGIS ticket."
attention_signals:
  - "The project is new to the agent, large, layered, or has unclear module ownership."
  - "The ticket mentions architecture, public interfaces, domain flows, business process, cross-module impact, or diff ripple effects."
  - "Local file reading leaves unresolved uncertainty about where behavior lives, which modules depend on it, or what business flow it supports."
  - "Generated map evidence would need confirmation against source files before influencing the ticket."
procedure:
  - "Confirm the ticket envelope first, including allowed_areas, must_not_touch, validation commands, and completion-report requirements."
  - "State why map evidence is needed and which bounded question it should answer."
  - "If Understand Anything evidence is already available or the operator provides it, inspect only the command, view, artifact, or summary relevant to the bounded question."
  - "Confirm generated map claims against source files, tests, docs, routes, schemas, or other primary project evidence."
  - "Report the ticket decision affected by the evidence and any remaining risk."
  - "Do not install Understand Anything, run external tools without operator direction, create graph artifacts, commit graph artifacts, or expand implementation scope."
scope_boundary:
  - "Covers requesting, consuming, and reporting codebase map evidence for one bounded AEGIS ticket question."
  - "Covers Understand Anything as optional advisory evidence while AEGIS remains authoritative for ticketing, roles, validators, contracts, and conformance."
  - "Does not install or run Understand Anything by itself, define final artifact policy, commit .understand-anything artifacts, implement code, alter runbooks, or update other procedures."
  - "Does not replace ordinary local code reading when nearby files and tests are enough."
composition_points:
  - "Understand Anything runbook explains operator-level use and artifact caution."
  - "Design-clarification-interview can use map evidence to ask sharper product, workflow, or architecture questions."
  - "Ubiquitous-language-map can use graph/search evidence to align business terms with code and docs."
  - "Module-boundary-review can use map evidence for dependencies, public interfaces, and coupling."
  - "Test-first-change can use map evidence to locate relevant tests or seams without replacing pre-change evidence."
  - "Code-validator can use reported map evidence as context while retaining independent validator judgment."
reference_pointers: []
verification:
  - "Verify map_need explains why local context was insufficient for this ticket."
  - "Verify evidence_source names the command, dashboard view, artifact, or operator-provided summary used."
  - "Verify source_confirmation names source files, tests, docs, routes, schemas, or primary evidence checked against the generated map claim."
  - "Verify ticket_decision_impact states what changed in planning, review, or implementation because of the evidence."
  - "Verify artifact_policy states that generated graph artifacts were not committed unless explicitly allowed by the ticket."
output_contract:
  - "status: completed, blocked, or not_applicable."
  - "map_need: why graph or context evidence was needed for this ticket."
  - "evidence_source: Understand Anything command, dashboard view, graph artifact, operator-provided summary, or comparable source used."
  - "source_confirmation: source files, tests, docs, routes, schemas, or primary evidence checked against generated claims."
  - "ticket_decision_impact: planning, review, validation, or implementation decision affected by the map evidence."
  - "artifact_policy: generated artifacts created, not created, ignored, or explicitly excluded from commit."
  - "residual_risk: stale graph risk, unconfirmed claims, context gaps, or remaining manual review needs."
---

# Codebase Map Generation

Use this procedure when a ticket genuinely needs system-wide graph or context
evidence from Understand Anything or comparable map output.

AEGIS remains authoritative. Graph evidence is advisory: it can inform ticket
planning, module-boundary review, domain-flow discovery, or diff impact review,
but it does not replace ticketing, roles, validators, contracts, scope checks, or
the Conformance Gate. This procedure does not install or run Understand Anything
by itself and must not create or commit `.understand-anything` artifacts.

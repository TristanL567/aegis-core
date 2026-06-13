---
standalone: true
trigger:
  - "Planning, implementation, or review depends on project or domain vocabulary that is ambiguous, inconsistent, overloaded, or not shared between the user, code, docs, tests, schemas, routes, or UI."
  - "A ticket or request uses business terms that do not clearly match code identifiers, data fields, API names, documentation, or user-facing labels."
  - "The agent must reason about behavior, module ownership, or acceptance criteria but key terms have multiple plausible meanings."
non_trigger:
  - "The needed vocabulary is already defined in the ticket, docs, code, tests, and user request with consistent meaning."
  - "The task is to rename code identifiers, rewrite documentation, implement behavior, refactor modules, or migrate schemas; this procedure only maps language."
  - "The task is broad glossary authoring unrelated to one planning, implementation, or review decision."
  - "The task is design clarification about product intent rather than term alignment; use design-clarification-interview for missing design concept."
failure_modes_addressed:
  - "AI talks at cross-purposes because user intent, business terms, code identifiers, and documentation use different language."
  - "The agent implements or reviews the wrong behavior because it treats aliases, overloaded terms, or stale names as equivalent without evidence."
attention_signals:
  - "A business term appears in the user request but related code, schema, route, test, or documentation uses a different name."
  - "The same term appears with different meanings across modules, docs, tickets, UI labels, API fields, or tests."
  - "A code identifier looks generic, abbreviated, legacy, or inconsistent with user-facing language."
  - "The request depends on a domain distinction such as account, customer, user, order, position, risk, exposure, calibration, deployment, or access."
  - "Review comments or prior discussion suggest people are using similar terms for different concepts."
procedure:
  - "Collect the smallest relevant evidence set from the user request, ticket, code identifiers, docs, schemas, routes, tests, UI labels, or review comments."
  - "Identify the terms that affect planning, implementation, or review decisions."
  - "Map each term to its current meaning, source evidence, related code or docs, aliases, forbidden synonyms, and open ambiguities."
  - "Flag conflicts where terms are overloaded, stale, missing from code, or used differently by business language and implementation artifacts."
  - "Stop with a concise term map and open questions; do not generate code, rename identifiers, rewrite docs, or choose implementation behavior from unresolved vocabulary."
scope_boundary:
  - "Covers vocabulary alignment for one planning, implementation, or review context."
  - "Produces a concise term map that can inform tickets, implementation, review, or later documentation work."
  - "Does not implement code, refactor names, rewrite documentation, migrate data, change schemas, change API contracts, or create scanners."
  - "Does not replace design-clarification-interview, test-first-change, module-boundary-review, ticket planning, or validator review."
composition_points:
  - "Design-clarification-interview owns missing product or workflow intent; this procedure owns term alignment once vocabulary ambiguity is visible."
  - "Ticket-planner-worker can use the term map to write clearer ticket language and acceptance criteria."
  - "Future test-first-change can use the term map to name behavior and assertions consistently."
  - "Future module-boundary-review can use the term map to check whether module names and ownership match domain concepts."
  - "Validators can use the term map as review evidence when language mismatch could hide an incorrect implementation."
  - "codebase-map-generation may provide optional advisory map evidence for aligning business terms with code, docs, schemas, routes, tests, or UI labels."
reference_pointers: []
verification:
  - "Verify each mapped term includes meaning, source evidence, related code or docs, aliases or forbidden synonyms, and open ambiguities."
  - "Verify the map distinguishes evidence-backed meanings from assumptions and unresolved questions."
  - "Verify the output includes no code, patch, rename instruction, documentation rewrite, schema change, or implementation commitment."
  - "Verify any blocking vocabulary ambiguity is surfaced before planning, implementation, or review proceeds."
output_contract:
  - "status: completed, needs_clarification, or not_applicable."
  - "term_map: entries with term, meaning, source evidence, related code/docs, aliases or forbidden synonyms, and open ambiguities."
  - "language_conflicts: overloaded, stale, missing, or inconsistent terms that affect the work."
  - "open_questions: concise questions for the human when vocabulary cannot be resolved from evidence."
  - "usage_guidance: preferred terms for the current ticket or review, limited to evidence-backed language."
  - "scope_guard: confirmation that the procedure produced no code, renames, refactors, documentation rewrites, or schema changes."
---

# Ubiquitous Language Map

Use this procedure when planning, implementation, or review depends on business
terms or project vocabulary that are ambiguous across the user request, code,
docs, tests, schemas, routes, or UI.

The output is a concise term map. It must not generate code, rename identifiers,
rewrite documentation, or change implementation behavior.

---
trigger:
  - "A planned or completed change risks crossing module ownership, expanding a public interface, adding shared helpers, moving behavior across layers, or introducing new module boundaries."
  - "A change creates or modifies APIs, services, adapters, data access boundaries, UI component boundaries, package exports, shared utilities, or cross-module dependencies."
  - "A review must decide whether a proposed design creates deep modules with simple interfaces or shallow fragmented modules with complex coupling."
non_trigger:
  - "The task is ordinary implementation inside a clearly owned module with no public interface, dependency, ownership, or boundary change."
  - "The task is design clarification about missing product or workflow intent; use design-clarification-interview."
  - "The task is test-first behavior verification; use test-first-change for the evidence loop."
  - "The task is a broad architecture refactor or migration plan that needs its own ticket; this procedure reviews one bounded boundary risk."
  - "The task is to implement code, move files, rename modules, or refactor; this procedure produces review guidance only."
failure_modes_addressed:
  - "AI creates shallow architecture, scattered helpers, or leaky interfaces that increase long-term entropy."
  - "The agent splits behavior into many tiny modules or exposes internals through public interfaces, making coupling harder to understand and change."
attention_signals:
  - "New shared utility, helper, abstraction, adapter, service, package export, public method, route, event, prop, schema, or interface appears."
  - "A change requires multiple modules to know each other's internal data shape, sequencing, errors, flags, or lifecycle."
  - "Logic is moved across layers without a clear owner for invariants, side effects, persistence, validation, or presentation."
  - "A public interface grows to expose implementation details instead of hiding cohesive internal complexity."
  - "The change creates many small files or modules where callers must coordinate behavior that one deeper module could own."
procedure:
  - "Identify affected modules, current owners, public interfaces, internal responsibilities, and dependencies involved in the change."
  - "Classify whether the proposed boundary change is necessary, optional, or outside the ticket scope."
  - "Assess depth: prefer a simple public interface that hides cohesive internal complexity over many shallow modules with complex coupling."
  - "Flag leaky interface, scattered helper, cross-layer dependency, duplicated ownership, or public API expansion risks."
  - "Recommend one of: keep change inside current boundary, allow the boundary change, narrow the interface, defer to a separate architecture ticket, or block pending clarification."
  - "Stop with review findings only; do not generate code, move files, rename modules, or implement a refactor."
scope_boundary:
  - "Covers architecture boundary review for one proposed or completed change with module ownership, public interface, coupling, or depth risk."
  - "Covers deep-vs-shallow module assessment: simple interfaces should hide cohesive internal complexity; shallow fragmented modules with complex coupling should be avoided."
  - "Does not implement code, refactor modules, move files, rename identifiers, change contracts, create tools, or rewrite architecture docs."
  - "Does not replace design-clarification-interview, ubiquitous-language-map, test-first-change, broad architecture planning, or validator review."
composition_points:
  - "Design-clarification-interview should run first when product, workflow, or architecture intent is not clear enough to judge the boundary."
  - "Ubiquitous-language-map should run first when module names or domain terms are ambiguous."
  - "Test-first-change supplies behavior evidence before implementation when the boundary decision depends on executable behavior."
  - "Code-validator can use this procedure to review whether implementation preserved module ownership and public interface discipline."
  - "Ticket-planner-worker can split broad refactors into separate tickets when this review finds a boundary change outside current scope."
reference_pointers: []
verification:
  - "Verify affected modules, public interfaces, dependencies, and ownership boundaries are named from observable project evidence."
  - "Verify coupling risks distinguish internal complexity hidden behind a simple interface from shallow modules that force callers to coordinate internals."
  - "Verify the recommendation states whether the boundary change is allowed, narrowed, deferred, or blocked."
  - "Verify the output includes no code, patch, file move, rename, or refactor implementation."
output_contract:
  - "status: completed, blocked, or not_applicable."
  - "affected_modules: modules, packages, layers, components, or services involved."
  - "public_interfaces: APIs, exports, methods, routes, events, props, schemas, or contracts changed or at risk."
  - "coupling_risk: dependencies, internal knowledge, sequencing, duplicated ownership, or leaky interface concerns."
  - "deep_shallow_assessment: whether the design hides cohesive complexity behind a simple interface or creates shallow fragmented modules with complex coupling."
  - "allowed_boundary_change: boundary change allowed by the ticket, narrowed, deferred, or blocked."
  - "recommendation: concise action for implementation or review, including any separate architecture ticket needed."
  - "scope_guard: confirmation that the procedure produced no code, moves, renames, or refactor implementation."
---

# Module Boundary Review

Use this procedure when a change may cross module ownership, expand a public
interface, or create shallow fragmented modules.

Prefer deep modules: simple public interfaces that hide cohesive internal
complexity. Avoid shallow architecture where many tiny modules, scattered
helpers, or leaky interfaces force callers to coordinate implementation details.
This procedure produces review guidance only and must not generate code or
implement refactors.

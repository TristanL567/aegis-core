---
trigger:
  - "Implementation is requested before product, business, design, architecture, or user-workflow intent is clear enough to preserve the human's design concept."
  - "A ticket, request, mockup, issue, or discussion names a desired change but leaves user outcome, workflow, domain meaning, constraints, or architectural fit underspecified."
  - "The agent is likely to choose UI, API, module, data, or behavior shape from plausible defaults rather than shared design intent."
non_trigger:
  - "The ticket already contains clear business intent, user workflow, acceptance criteria, architectural context, and enough implementation boundaries to proceed."
  - "The task is pure mechanical cleanup, formatting, dependency update, or generated artifact refresh with no product, workflow, or architecture decision."
  - "The task is implementation after clarification has already produced an accepted design brief."
  - "The task is code generation, refactoring, testing, or module review; this procedure stops before implementation."
failure_modes_addressed:
  - "AI builds plausible code without sharing the human's design concept."
  - "The agent fills missing product, business, workflow, or architecture intent with generic assumptions and then implements the wrong shape."
attention_signals:
  - "Ambiguous phrases such as make it better, add support, improve UX, clean up flow, integrate with, or handle edge cases without concrete intent."
  - "Missing user role, user goal, business rule, workflow step, success condition, non-goal, domain term, or architectural boundary."
  - "Multiple plausible designs would satisfy the literal request but create different product behavior, module ownership, data shape, or review burden."
  - "The human has not confirmed the desired concept, tradeoff, or boundary before implementation."
  - "A ticket says to proceed quickly but would require inventing intent to write code."
procedure:
  - "Classify whether missing product, business, design, architecture, or user-workflow intent blocks implementation."
  - "List the smallest set of clarification questions needed to remove the blocking ambiguity; prefer focused questions over broad discovery."
  - "If enough context exists, synthesize a concise design brief with intent, user/workflow outcome, constraints, non-goals, architecture boundary, and acceptance signals."
  - "Ask the human to answer the blocking questions or confirm the design brief before implementation begins."
  - "Stop without generating code, changing files, or choosing implementation details that depend on unconfirmed design intent."
scope_boundary:
  - "Covers pre-implementation clarification for underspecified product, business, design, architecture, and user-workflow intent."
  - "Produces focused clarification questions or a concise design brief that can feed a later ticket or implementation step."
  - "Does not generate code, edit files, choose final implementation mechanics, create tests, review module boundaries, or rewrite ticket contracts."
  - "Does not replace master routing, ticket planning, validator review, test-first-change, ubiquitous-language-map, or module-boundary-review."
composition_points:
  - "Master invokes this procedure before routing implementation when ticket intent is too ambiguous to preserve the human's design concept."
  - "Ticket-planner-worker can use the resulting design brief to draft a sharper ticket envelope."
  - "Future ubiquitous-language-map owns durable domain vocabulary after clarification reveals important recurring terms."
  - "Future test-first-change owns the test loop after behavior is clear enough to specify."
  - "Future module-boundary-review owns architecture boundary review after the intended change shape is known."
  - "codebase-map-generation may provide optional advisory map evidence for product, workflow, or architecture questions when local context is insufficient."
reference_pointers: []
verification:
  - "Verify that every blocking ambiguity is either expressed as a clarification question or resolved in the design brief."
  - "Verify the output includes no code, patch, file edit instruction, or implementation commitment."
  - "Verify the brief, when produced, names design intent, business or user outcome, constraints, non-goals, architecture boundary, and acceptance signals."
  - "Verify implementation remains blocked until the human answers the questions or confirms the design brief."
output_contract:
  - "status: needs_clarification, completed, or not_applicable."
  - "blocking_ambiguities: concise list of missing design, business, workflow, or architecture facts."
  - "clarification_questions: focused questions for the human when ambiguity remains."
  - "design_brief: concise brief when enough information exists, including intent, outcome, constraints, non-goals, architecture boundary, and acceptance signals."
  - "implementation_gate: before implementation, state whether implementation is blocked or cleared by confirmed design intent."
  - "scope_guard: confirmation that the procedure produced no code and made no file changes."
---

# Design Clarification Interview

Use this procedure before implementation when the request lacks enough product,
business, design, architecture, or user-workflow intent to preserve the human's
design concept.

The procedure is intentionally pre-code. Its outputs are focused clarification
questions or a concise design brief. It must not generate code, edit files, or
commit to implementation details that depend on unconfirmed intent.

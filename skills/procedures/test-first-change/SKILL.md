---
trigger:
  - "A ticket changes executable behavior and a test, reproduction, fixture, command, or other reproducible check is feasible before implementation."
  - "A bug fix, feature, API behavior, UI interaction, data transformation, model behavior, deployment behavior, or validation rule needs evidence before code changes."
  - "The agent is likely to implement multiple changes before proving the current behavior or failure mode."
non_trigger:
  - "The task is docs-only, comment-only, prompt-only, planning-only, or formatting-only with no executable behavior change."
  - "The task is an exploratory spike where the ticket explicitly says no durable implementation or test is expected."
  - "The task is pure cleanup or refactoring that must preserve behavior and already has adequate existing regression coverage."
  - "Tests or reproducible checks are genuinely infeasible; record the reason and use manual review or explicit pre-change evidence instead."
failure_modes_addressed:
  - "AI writes too much code before proving the behavior with a test or check."
  - "The agent changes implementation first, then invents verification after the fact, making it hard to know which behavior was fixed or preserved."
attention_signals:
  - "The ticket changes externally visible behavior, business logic, data output, API response, UI interaction, validation, error handling, or runtime behavior."
  - "A failing scenario, bug report, acceptance criterion, expected output, or reproducible command can be expressed before implementation."
  - "Existing tests cover nearby behavior but not the requested change."
  - "The implementation path looks broad or tempting before a narrow behavioral target has been proven."
  - "The user asks for a fix or feature but the current behavior has not been captured."
procedure:
  - "Classify the change as executable behavior work and identify the smallest observable behavior to prove."
  - "Before implementation, create or run a failing test, reproduction, fixture, command, or explicit pre-change evidence when feasible."
  - "If no feasible test or reproduction exists, record why and define the strongest available manual or observational check before changing code."
  - "Implement the smallest code change needed to satisfy the failing test, reproduction, or pre-change evidence."
  - "Run the targeted check and relevant regression checks; if they fail, revise within the ticket scope."
  - "Clean up only code made necessary by the change, then rerun verification and report residual risk."
scope_boundary:
  - "Covers behavior-changing implementation where pre-change executable or reproducible evidence is feasible."
  - "Covers the loop from failing test, reproduction, or pre-change evidence through minimal implementation, verification, and bounded cleanup."
  - "Does not cover docs-only work, exploratory spikes, pure cleanup, broad refactors, new test tooling, contract changes, role changes, validator changes, or execution prompt changes."
  - "Does not require inventing fragile tests when tests are infeasible; infeasibility must be explicit and replaced by the strongest available check."
composition_points:
  - "Design-clarification-interview should run first when behavior intent is unclear."
  - "Ubiquitous-language-map should run first when behavior names or domain terms are ambiguous."
  - "Future module-boundary-review can compose after behavior is defined when implementation risks crossing ownership boundaries."
  - "codebase-map-generation may provide optional advisory map evidence for locating likely tests or seams, but it does not replace failing tests, reproduction, or pre-change evidence."
  - "Code-validator uses this procedure's evidence to check that implementation did not outrun verification."
  - "Clean-commit composes after verification passes and cleanup remains scoped."
reference_pointers: []
verification:
  - "Verify pre-change evidence exists: failing test, reproduction, baseline command output, fixture, or documented reason tests are infeasible."
  - "Verify implementation is tied to the smallest proven behavior and does not expand into unrelated changes."
  - "Verify the targeted check passes after implementation and relevant regression checks are reported."
  - "Verify cleanup or refactor notes are limited to code made necessary by the behavior change."
output_contract:
  - "status: completed, blocked, or not_applicable."
  - "behavior_under_change: concise description of the executable behavior being changed."
  - "pre_change_evidence: failing test, reproduction, baseline output, explicit check, or infeasibility rationale."
  - "implementation_step: smallest implemented change tied to the evidence."
  - "verification_result: targeted check and relevant regression results after implementation."
  - "cleanup_refactor_notes: cleanup performed, or why none was needed, limited to ticket scope."
  - "residual_risk: remaining manual checks, skipped tests, or infeasible verification limits."
---

# Test-First Change

Use this procedure when a ticket changes executable behavior and tests or
reproducible checks are feasible.

Start with a failing test, reproduction, or explicit pre-change evidence before
implementation when feasible. If no such check is feasible, record why before
code changes. Keep implementation minimal, verify the behavior, and limit
cleanup to what the change made necessary.

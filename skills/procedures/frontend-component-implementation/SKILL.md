---
trigger:
  - "A task asks to add, modify, repair, or integrate one frontend component or a tightly scoped component behavior."
  - "A component change risks spreading into page-level architecture, broad layout refactors, inconsistent controls, framework churn, styling churn, or unverified UI behavior."
  - "A review must decide whether a component implementation stayed within the requested boundary and matches existing UI conventions."
non_trigger:
  - "The task is a full page redesign, design-system migration, app architecture change, routing overhaul, or broad layout refactor."
  - "The task is an accessibility audit of an existing UI rather than implementation of a component; use future accessibility-audit for that concern."
  - "The task is creating React, TypeScript, CSS, frontend domain, or accessibility procedural skills."
  - "The task is backend endpoint, chart artifact, deployment, investment, quant, ML, or SQL workflow work."
failure_modes_addressed:
  - "Component work expands into broad page architecture or inconsistent UI controls."
  - "A small component implementation is treated as permission to redesign larger UI structure, introduce new patterns, create layout drift, or leave UI behavior unverified."
attention_signals:
  - "A requested component boundary, existing component pattern, local design convention, state model, prop contract, event behavior, or reusable control already exists."
  - "New controls, layout wrappers, styling systems, framework patterns, state libraries, or component abstractions appear beyond the component scope."
  - "Expected states such as loading, empty, error, disabled, selected, expanded, focused, validation, or responsive variants."
  - "Keyboard, focus, semantic, name, form, visual, responsive, and manual behavior that needs checking for the component."
  - "Reference pointer conditions for semantic structure, keyboard and focus, names and ARIA, forms, responsive behavior, framework patterns, and language idioms."
procedure:
  - "Classify the work as scoped component implementation rather than page architecture, design-system migration, or accessibility audit."
  - "Inventory the requested component boundary, existing local patterns, expected states, data and prop contracts, interaction behavior, and files in scope."
  - "Open the matching frontend-accessibility and language-idioms drawers from reference_pointers when component semantics, behavior, layout, framework, or language details need reference knowledge."
  - "Implement or review the component using existing conventions and avoid broader page structure, framework, styling, or control-pattern churn unless explicitly required."
  - "Verify component behavior, state coverage, responsive layout, keyboard and focus behavior, and manual visual behavior."
  - "Report implemented scope, verification evidence, residual UI concerns, and excluded broader work."
scope_boundary:
  - "Covers implementation or review of one component or tightly scoped component behavior, including local conventions, expected states, UI behavior, layout fit, and manual review."
  - "Covers using accessibility and language reference drawers to support implementation decisions without turning the procedure into an audit."
  - "Does not cover accessibility-audit content, full page redesign, design-system migration, broad UI architecture, framework migration, React or TypeScript skill creation, CSS skill creation, or frontend domain skill creation."
  - "Does not cover backend endpoint work, charting, deployment, ML, quant, investment, SQL, or broad product design."
composition_points:
  - "reference_pointers bind this procedure to frontend-accessibility drawers for semantic structure, keyboard and focus, names and states, forms, visual responsiveness, and framework accessibility patterns."
  - "reference_pointers bind this procedure to language-idioms drawers for TypeScript and JavaScript, HTML and CSS, and shell or config conventions."
  - "Future accessibility-audit owns systematic accessibility findings, issue severity, assistive technology evidence, and audit reporting for existing UI."
  - "New-api-endpoint owns backend endpoint work when component implementation needs API behavior."
  - "Chart-artifact-generation owns auditable chart artifacts when component work requires generating a chart artifact."
reference_pointers:
  - ref: frontend-accessibility
    section: semantic-structure
    open_when: "Open when the component's markup, element choice, heading, list, table, landmark, or DOM order affects meaning."
  - ref: frontend-accessibility
    section: keyboard-and-focus
    open_when: "Open when component interaction requires keyboard access, focus order, focus visibility, focus restoration, or composite widget behavior."
  - ref: frontend-accessibility
    section: names-states-and-aria
    open_when: "Open when controls, icons, roles, names, descriptions, selected, expanded, disabled, invalid, or hidden states need semantics."
  - ref: frontend-accessibility
    section: forms-and-errors
    open_when: "Open when the component contains fields, labels, instructions, validation, required states, or error feedback."
  - ref: frontend-accessibility
    section: visual-and-responsive-accessibility
    open_when: "Open when text fitting, contrast, target size, motion, zoom, layout reflow, or responsive behavior affects component usability."
  - ref: frontend-accessibility
    section: framework-accessibility-patterns
    open_when: "Open when React, component library, portal, ref, hydration, controlled state, or framework composition affects accessible behavior."
  - ref: language-idioms
    section: typescript-javascript-idioms
    open_when: "Open when component props, state, async behavior, event handlers, modules, or TypeScript and JavaScript conventions affect implementation."
  - ref: language-idioms
    section: html-css-idioms
    open_when: "Open when markup, CSS layout, styling hooks, responsive constraints, or browser primitives affect implementation."
  - ref: language-idioms
    section: shell-config-idioms
    open_when: "Open when component work needs command, environment, script, or configuration convention checks."
verification:
  - "Verify UI behavior: expected component states, interactions, event handling, disabled or loading behavior, error or empty states, and data or prop boundaries are checked."
  - "Verify layout/manual review: component fit, responsive states, text fitting, visual regressions, focus visibility, and manual visual behavior are reviewed in the relevant UI context."
  - "Verify keyboard and focus behavior when the component is interactive."
  - "Verify the implementation stays within the component boundary and does not introduce broad page architecture, framework, styling, or control-pattern churn without explicit scope."
  - "Verify excluded concerns such as accessibility audit, design-system migration, React or TypeScript skill creation, CSS skill creation, and frontend domain skill creation are named rather than handled inside this procedure."
output_contract:
  - "status: completed, blocked, or not_applicable."
  - "component_scope: component, files, behavior, states, and local patterns reviewed or changed."
  - "implementation_summary: concise description of the scoped component change."
  - "ui_behavior_review: states, interactions, data or prop boundaries, and behavior checks performed."
  - "layout_manual_review: responsive, visual, text-fitting, focus visibility, and manual review findings."
  - "scope_guard: broad page, framework, layout, styling, or control-pattern changes avoided or explicitly justified."
  - "excluded_concerns: accessibility audit, design-system migration, broad architecture, domain skills, backend, charting, or other concerns left to owning procedures or roles."
---

# Frontend Component Implementation

Use this procedure when a frontend task is to add or modify one component without expanding into broader page architecture or inconsistent UI controls. It exists to prevent the confirmed failure mode where component work expands into broad page architecture or inconsistent UI controls.

Open only the needed `frontend-accessibility` and `language-idioms` drawers through `reference_pointers`. Keep detailed frontend, accessibility, framework, and language knowledge in the drawers and keep this procedure focused on component boundary, existing conventions, states, UI behavior, layout, and manual review.

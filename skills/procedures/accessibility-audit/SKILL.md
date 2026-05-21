---
trigger:
  - "A task asks to audit, review, verify, or report accessibility behavior for an existing UI screen, flow, or component after or apart from implementation."
  - "A UI has been visually reviewed or appears visually acceptable, but keyboard, semantic, contrast, focus, ARIA, form, or screen-reader-relevant behavior has not been checked."
  - "A review must identify accessibility findings, evidence, severity, or reproducible accessibility concerns."
non_trigger:
  - "The task is implementing or modifying one frontend component; use frontend-component-implementation for that concern."
  - "The task is visual redesign, brand polish, design-system migration, full page architecture, or broad frontend refactor."
  - "The task is creating frontend, React, TypeScript, CSS, or accessibility domain skills."
  - "The task is backend endpoint, chart artifact, deployment, investment, quant, ML, or SQL workflow work."
failure_modes_addressed:
  - "Visual-only UI review misses keyboard, semantic, contrast, or screen-reader checks."
  - "A UI is accepted as correct because it looks fine while keyboard behavior, semantic structure, focus, ARIA names and states, forms and errors, contrast, responsive accessibility, or screen-reader-relevant behavior is unverified."
attention_signals:
  - "Claims that a UI is done, reviewed, polished, or visually correct without evidence of keyboard, focus, semantic, form, contrast, or assistive technology checks."
  - "Interactive controls, forms, dialogs, menus, route changes, dynamic content, icons, disabled states, error states, loading states, or responsive variants."
  - "Missing accessible names, roles, states, focus order, focus visibility, keyboard path, labels, error messages, live status, contrast, or zoom behavior."
  - "Automated accessibility scan output that needs manual interpretation or manual review gaps."
  - "Reference pointer conditions for semantic structure, keyboard and focus, names and states, dynamic content, visual accessibility, and audit evidence."
procedure:
  - "Classify the work as accessibility audit rather than component implementation, visual redesign, or frontend architecture work."
  - "Inventory the UI scope, critical user paths, interactive elements, forms, dynamic states, responsive states, and available automated or manual evidence."
  - "Open the matching frontend-accessibility drawers from reference_pointers when semantic, keyboard, name, state, dynamic, visual, or audit evidence needs reference knowledge."
  - "Perform or review manual and tool-assisted checks for keyboard access, focus, semantic structure, names and states, forms and errors, contrast, responsive behavior, and screen-reader-relevant behavior."
  - "Map findings to affected elements or flows with evidence, severity, expected behavior, and reproduction notes."
  - "Report audit status, findings, passing evidence scope, residual gaps, and excluded implementation work."
scope_boundary:
  - "Covers accessibility audit of existing UI behavior, including manual or tool-assisted checks, keyboard, focus, semantics, names and states, forms and errors, contrast, responsive accessibility, dynamic content, and evidence reporting."
  - "Covers identifying findings and evidence without owning component implementation or visual redesign."
  - "Does not cover frontend-component-implementation, visual redesign, design-system migration, broad frontend architecture, React or TypeScript skill creation, CSS skill creation, or accessibility domain skill creation."
  - "Does not cover backend endpoint work, charting, deployment, ML, quant, investment, SQL, or broad product design."
composition_points:
  - "reference_pointers bind this procedure to frontend-accessibility drawers for semantic structure, keyboard and focus, names and states, dynamic content, visual responsiveness, and audit evidence."
  - "Frontend-component-implementation owns scoped component changes when the audit produces implementation work."
  - "Future visual redesign or design-system migration work owns broad visual changes beyond accessibility findings."
  - "Chart-artifact-generation owns auditable chart artifacts if audit reporting requires generating a chart artifact."
  - "Worker roles remain fallback routers for broader frontend work not covered by this procedure."
reference_pointers:
  - ref: frontend-accessibility
    section: semantic-structure
    open_when: "Open when landmarks, headings, native elements, document order, lists, tables, or semantic structure need audit review."
  - ref: frontend-accessibility
    section: keyboard-and-focus
    open_when: "Open when keyboard access, focus order, focus visibility, focus traps, restoration, or composite widget behavior needs audit review."
  - ref: frontend-accessibility
    section: names-states-and-aria
    open_when: "Open when accessible names, descriptions, roles, ARIA, selected, expanded, disabled, invalid, or hidden states need audit review."
  - ref: frontend-accessibility
    section: dynamic-content-and-announcements
    open_when: "Open when loading, saving, route changes, dialogs, async updates, live regions, or status announcements need audit review."
  - ref: frontend-accessibility
    section: visual-and-responsive-accessibility
    open_when: "Open when contrast, text scaling, target size, motion, zoom, layout reflow, or responsive behavior needs audit review."
  - ref: frontend-accessibility
    section: audit-evidence
    open_when: "Open when findings need manual checks, automated scan interpretation, assistive technology evidence, severity, or reproducible reporting."
verification:
  - "Verify manual or tool-assisted accessibility checks were performed or reviewed for the scoped UI, and identify which checks were not possible."
  - "Verify keyboard access, focus order, focus visibility, semantic structure, accessible names and states, forms or errors, contrast, responsive behavior, and screen-reader-relevant behavior are checked where applicable."
  - "Verify automated scan results are not treated as complete coverage without manual review of interaction and user-path behavior."
  - "Verify each finding includes affected element or flow, evidence, expected behavior, severity or impact, and reproduction notes."
  - "Verify excluded concerns such as component implementation, visual redesign, design-system migration, and frontend domain skill creation are not handled inside this procedure."
output_contract:
  - "status: completed, blocked, or not_applicable."
  - "audit_scope: UI screen, flow, component, states, and user paths reviewed."
  - "checks_performed: manual and tool-assisted checks performed, skipped, or blocked."
  - "findings: accessibility issues with affected element or flow, evidence, expected behavior, severity or impact, and reproduction notes."
  - "passing_evidence_scope: areas checked with no finding, limited to the evidence actually reviewed."
  - "residual_gaps: checks not performed, unavailable assistive technology coverage, or unresolved uncertainty."
  - "excluded_concerns: component implementation, visual redesign, design-system migration, frontend domain skills, backend, charting, or other concerns left to owning procedures or roles."
---

# Accessibility Audit

Use this procedure when an existing UI needs accessibility review beyond visual correctness. It exists to prevent the confirmed failure mode where visual-only UI review misses keyboard, semantic, contrast, or screen-reader checks.

Open only the needed `frontend-accessibility` drawers through `reference_pointers`. Keep detailed accessibility knowledge in the drawers and keep this procedure focused on audit evidence: manual or tool-assisted checks, keyboard and focus behavior, semantics, names and states, forms, contrast, responsive behavior, and screen-reader-relevant behavior.

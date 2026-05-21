---
trigger:
  - "A task asks to review, approve, modify, or justify a cloud IAM, service account, role, policy, secret, bucket, database, queue, deployment access, or trust-policy change."
  - "An access change looks like a quick fix, but may grant broad permissions, cross a trust boundary, expand inherited access, or create privilege-escalation risk."
  - "A review must decide whether a cloud access-policy change is least-privilege, auditable, reversible, and manually approved."
non_trigger:
  - "The task is deployment failure triage, rollout diagnosis, logs, health checks, runtime config, or dependency drift; use deployment-failure-triage for that concern."
  - "The task is cloud provider reference content, provider-specific runtime docs, deployment docs, runbook creation, or cloud skill creation."
  - "The task is application feature implementation, backend endpoint behavior, frontend behavior, database migration, or test-only CI cleanup without IAM change ownership."
  - "The task is incident command policy, charting, investment, quant, ML, accessibility, or SQL workflow work."
failure_modes_addressed:
  - "AI grants over-broad permissions or misses trust-boundary impact."
  - "A cloud access change is accepted before checking least privilege, principal identity, resource scope, conditions, inherited access, deny rules, audit evidence, rollback, manual approval, or access-policy side effects."
attention_signals:
  - "New or changed users, groups, roles, service accounts, managed identities, trust policies, permission policies, bucket policies, secrets, keys, databases, queues, or deployment access."
  - "Broad actions, wildcard resources, cross-account access, public access, impersonation, pass-role, policy administration, key or secret access, logging mutation, or production write access."
  - "Missing principal owner, access purpose, approval, expiration, rollback path, audit logging, condition boundaries, deny-rule review, or inherited access review."
  - "Trust boundary changes across account, project, subscription, tenant, namespace, workload identity, federation, production, or external principal."
  - "Reference pointer conditions for principals, least privilege, policy risk, audit evidence, and provider context."
procedure:
  - "Classify the work as cloud IAM change review rather than deployment triage, provider documentation, or application implementation."
  - "Inventory the principal, resource, action set, conditions, inherited access, deny controls, trust boundary, owner, purpose, approval evidence, rollback path, and audit coverage."
  - "Open the matching cloud-operations drawers from reference_pointers when principal, permission, policy risk, audit, or provider context needs reference knowledge."
  - "Check whether narrower permissions, tighter resources, conditions, time bounds, or separate principals would satisfy the stated purpose."
  - "Review trust-boundary impact, access-policy side effects, privilege-escalation paths, rollback feasibility, and manual approval or separation-of-duties evidence."
  - "Report approval status, required narrowing, blocking risks, rollback/manual review evidence, and excluded deployment or provider-doc concerns."
scope_boundary:
  - "Covers review of cloud IAM and access-policy changes for principal identity, resource and action scope, least privilege, trust-boundary impact, inherited access, deny controls, policy side effects, audit evidence, rollback, and manual approval."
  - "Covers provider-specific concepts only through reference drawers and only to interpret the IAM change."
  - "Does not cover deployment triage, cloud provider reference content, provider-specific runtime docs, provider-specific deployment docs, runbook creation, cloud skill creation, or application implementation."
  - "Does not cover backend endpoint work, frontend work, database migration implementation, charting, investment, quant, ML, accessibility, or SQL workflow work."
composition_points:
  - "reference_pointers bind this procedure to cloud-operations drawers for identity boundaries, least privilege, policy risk, audit evidence, and provider context."
  - "Deployment-failure-triage owns logs, rollout status, runtime config, dependency drift, and health checks when the issue is deployment failure rather than access-policy review."
  - "Future security policy or governance work may own organization-wide policy authoring beyond this narrow change review."
  - "Backend or frontend procedures own application changes once IAM review identifies the access boundary needed by application code."
  - "Worker roles remain fallback routers for broader or ambiguous cloud work not covered by this procedure."
reference_pointers:
  - ref: cloud-operations
    section: identity-and-principal-boundaries
    open_when: "Open when users, groups, roles, service accounts, managed identities, workload identity, federation, or trust policy boundaries need review."
  - ref: cloud-operations
    section: permission-scope-and-least-privilege
    open_when: "Open when actions, resources, conditions, inheritance, deny rules, or narrower least-privilege scope need review."
  - ref: cloud-operations
    section: policy-change-risk
    open_when: "Open when privilege escalation, cross-account access, public exposure, persistence, sensitive operations, or access-policy side effects need review."
  - ref: cloud-operations
    section: audit-evidence-and-separation
    open_when: "Open when approval evidence, ownership, logging, break-glass access, rollback review, or separation of duties needs review."
  - ref: cloud-operations
    section: provider-operations-context
    open_when: "Open when AWS, Azure, GCP, Kubernetes, serverless, managed service, or provider naming context affects IAM interpretation."
verification:
  - "Verify least privilege: principal, actions, resources, conditions, inherited access, deny controls, time bounds, and narrower alternatives are reviewed or explicitly unresolved."
  - "Verify trust boundary: account, project, subscription, tenant, namespace, workload, federation, external principal, and production boundary impacts are reviewed."
  - "Verify rollback/manual review: owner, purpose, approval evidence, separation of duties, expiration or review date, rollback path, and audit logging are checked or explicitly missing."
  - "Verify access-policy side effects: privilege escalation, public exposure, cross-account access, secret or key access, logging mutation, policy administration, and persistence risks are checked where applicable."
  - "Verify excluded concerns such as deployment triage, provider runtime docs, provider-specific deployment docs, and application implementation are not handled inside this procedure."
output_contract:
  - "status: completed, blocked, or not_applicable."
  - "change_reviewed: principal, resource, action set, policy, trust boundary, environment, and source artifact reviewed."
  - "least_privilege_review: required access, over-broad grants, narrower alternatives, conditions, inherited access, and deny controls."
  - "trust_boundary_review: account, project, subscription, tenant, namespace, workload, federation, external, and production boundary impacts."
  - "side_effect_review: privilege escalation, public exposure, cross-account access, secret or key access, logging mutation, persistence, and sensitive operation risks."
  - "rollback_manual_review: approval evidence, owner, purpose, expiration, rollback path, audit logging, and separation-of-duties findings."
  - "decision: approved_with_limits, blocked, needs_narrowing, or not_applicable with concise rationale."
  - "excluded_concerns: deployment triage, provider docs, application implementation, backend, frontend, database, charting, or other work left to owning procedures or roles."
---

# Cloud IAM Change Review

Use this procedure when a cloud IAM or access-policy change must be reviewed before it is accepted. It exists to prevent the confirmed failure mode where AI grants over-broad permissions or misses trust-boundary impact.

Open only the needed `cloud-operations` drawers through `reference_pointers`. Keep detailed cloud operations and provider knowledge in the drawers and keep this procedure focused on least privilege, trust boundaries, access-policy side effects, rollback, manual approval, and audit evidence.

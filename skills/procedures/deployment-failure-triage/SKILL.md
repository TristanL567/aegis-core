---
trigger:
  - "A task asks to triage a deployment, service startup, cloud run, container, CI/CD, or production-like runtime failure."
  - "A service failed to deploy, start, pass health checks, or behave correctly after rollout, and a config or runtime change is being considered before evidence is read."
  - "A review must determine the likely failure surface before changing deployment config, environment variables, container settings, cloud settings, or rollout config."
non_trigger:
  - "The task is IAM access review, permission policy change review, or identity boundary review; use future cloud-iam-change-review for that concern."
  - "The task is provider-specific runtime doc creation, runbook creation, cloud skill creation, or deployment platform documentation."
  - "The task is implementing application code, backend endpoint behavior, frontend behavior, database migration, or test-only CI cleanup without deployment symptoms."
  - "The task is incident command policy, security policy authorship, charting, investment, quant, ML, or accessibility work."
failure_modes_addressed:
  - "AI changes deployment config before reading logs, rollout state, and recent deltas."
  - "Deployment config, environment variables, runtime settings, container config, cloud settings, or rollout config are changed before inspecting logs, health checks, rollout state, recent changes, dependency drift, or environment differences."
attention_signals:
  - "Failed rollout, crash loop, failed health check, cold start, bad status code, failed container start, queue stall, runtime error, timeout, or region-specific failure."
  - "Pressure to change env vars, secrets, resource limits, image tags, container settings, cloud settings, rollout strategy, or networking before diagnosis."
  - "Missing logs, metrics, traces, health check output, deployment events, artifact version, image digest, recent commit, config delta, dependency version, or feature flag evidence."
  - "Possible configuration drift, dependency drift, network or runtime boundary issue, provider quota, rollback risk, or blast-radius concern."
  - "Reference pointer conditions for rollout state, logs, config drift, runtime boundaries, rollback, and provider context."
procedure:
  - "Classify the work as deployment failure triage rather than IAM review, provider doc authoring, or application feature implementation."
  - "Pause deployment config or runtime changes until evidence has been inventoried unless an explicit emergency containment action is required."
  - "Inventory rollout state, health checks, logs, metrics, recent commits, config and environment deltas, image or artifact versions, dependencies, and affected scope."
  - "Open the matching cloud-operations drawers from reference_pointers when rollout, observability, drift, runtime boundary, rollback, or provider context needs reference knowledge."
  - "Compare symptoms against recent changes, dependency drift, environment differences, networking or runtime boundaries, and rollback or blast-radius options."
  - "Report triage findings, evidence gaps, safe next checks, manual confirmations, and excluded IAM or provider-doc concerns."
scope_boundary:
  - "Covers diagnostic triage for deployment, startup, rollout, health check, container, cloud runtime, CI/CD, and production-like runtime failures before config or runtime changes."
  - "Covers logs, rollout status, health checks, recent-change review, config and dependency drift, runtime boundaries, rollback options, blast radius, and manual confirmation."
  - "Does not cover IAM review, provider-specific runtime docs, provider-specific deployment docs, runbook creation, cloud skill creation, or security policy authorship."
  - "Does not cover application feature implementation, backend endpoint work, frontend work, database migration, investment, quant, ML, accessibility, or charting work."
composition_points:
  - "reference_pointers bind this procedure to cloud-operations drawers for deployment state, observability, configuration drift, runtime boundaries, rollback, and provider context."
  - "Future cloud-iam-change-review owns IAM access, permission policy, identity boundary, and privilege-risk review."
  - "Backend or frontend implementation procedures own application code fixes after deployment evidence identifies an application-owned cause."
  - "New-api-endpoint owns backend endpoint implementation when triage identifies endpoint behavior rather than deployment configuration as the cause."
  - "Worker roles remain fallback routers for broader or ambiguous cloud work not covered by this procedure."
reference_pointers:
  - ref: cloud-operations
    section: deployment-state-and-rollout
    open_when: "Open when release state, rollout phase, health checks, version ownership, traffic split, or currently serving artifact needs triage."
  - ref: cloud-operations
    section: observability-and-logs
    open_when: "Open when logs, metrics, traces, alerts, dashboards, deployment events, or symptom correlation need triage."
  - ref: cloud-operations
    section: configuration-and-dependency-drift
    open_when: "Open when env vars, secrets, image tags, dependencies, feature flags, infrastructure drift, or environment differences may explain the failure."
  - ref: cloud-operations
    section: networking-and-runtime-boundaries
    open_when: "Open when DNS, TLS, load balancers, ingress, egress, resource limits, provider quotas, or runtime constraints may explain symptoms."
  - ref: cloud-operations
    section: rollback-and-blast-radius
    open_when: "Open when recovery options, rollback safety, degradation, containment, customer impact, or data safety need review."
  - ref: cloud-operations
    section: provider-operations-context
    open_when: "Open when AWS, Azure, GCP, Kubernetes, serverless, managed service, or provider naming context affects interpretation."
verification:
  - "Verify logs and observability evidence were read or explicitly unavailable, including relevant timestamps, service or version scope, errors, metrics, traces, or events."
  - "Verify rollout status and health checks were reviewed, including currently serving version, desired versus observed state, failed probes, traffic split, affected environment, and affected region or tenant when applicable."
  - "Verify recent-change review was performed, including commits, config and env deltas, image or artifact versions, dependency versions, feature flags, infrastructure changes, and provider-side changes when known."
  - "Verify manual confirmation records the triage conclusion, remaining uncertainty, safe next checks, and any config or runtime change that is justified by evidence."
  - "Verify excluded concerns such as IAM review, provider runtime docs, provider-specific deployment docs, and application implementation are not handled inside this procedure."
output_contract:
  - "status: completed, blocked, or not_applicable."
  - "triage_scope: service, environment, deployment, version, region, tenant, route, job, or runtime surface reviewed."
  - "evidence_inventory: logs, metrics, traces, health checks, rollout state, recent changes, config deltas, dependency versions, and missing evidence."
  - "recent_delta_review: commits, config, env, secrets, image, dependency, feature flag, infrastructure, provider, or rollout deltas reviewed."
  - "triage_findings: likely failure surfaces, ruled-out causes, unresolved gaps, rollback or containment context, and blast-radius notes."
  - "manual_confirmation: evidence-backed next checks or changes and confirmation that config/runtime edits were not made before diagnosis except emergency containment."
  - "excluded_concerns: IAM review, provider docs, application implementation, backend, frontend, database, charting, or other work left to owning procedures or roles."
---

# Deployment Failure Triage

Use this procedure when a deployment or runtime failure must be diagnosed before changing deployment configuration or runtime settings. It exists to prevent the confirmed failure mode where AI changes deployment config before reading logs, rollout state, and recent deltas.

Open only the needed `cloud-operations` drawers through `reference_pointers`. Keep detailed cloud operations knowledge in the drawers and keep this procedure focused on logs, rollout status, health checks, recent-change review, dependency and configuration drift, runtime boundaries, rollback context, and manual confirmation.

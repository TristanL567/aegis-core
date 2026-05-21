# Cloud Operations Reference

## Scope

Reference scope: Axis-2 knowledge for cloud deployment failure triage and IAM
change review, including rollout state, logs and metrics, configuration and
dependency drift, networking, identity boundaries, least privilege, audit
evidence, rollback context, and provider-specific concepts as reference
material only.

It is not a procedural skill and is not independently executable.

## Consuming Skills

- `deployment-failure-triage`: expected `reference_pointers` sections are
  `deployment-state-and-rollout`, `observability-and-logs`,
  `configuration-and-dependency-drift`, `networking-and-runtime-boundaries`,
  `rollback-and-blast-radius`, and `provider-operations-context`.
- `cloud-iam-change-review`: expected `reference_pointers` sections are
  `identity-and-principal-boundaries`, `permission-scope-and-least-privilege`,
  `policy-change-risk`, `audit-evidence-and-separation`, and
  `provider-operations-context`.

## Sections

| id | topic | open when |
| --- | --- | --- |
| deployment-state-and-rollout | Release state, rollout phases, health checks, deployments, and version ownership. | Open when a deployment failure depends on what changed, where it rolled out, or what is currently serving. |
| observability-and-logs | Logs, metrics, traces, alerts, dashboards, and symptom correlation. | Open when cloud triage depends on runtime evidence rather than code inspection alone. |
| configuration-and-dependency-drift | Environment variables, secrets, images, dependencies, feature flags, and infrastructure drift. | Open when failure may come from runtime configuration or dependency mismatch. |
| networking-and-runtime-boundaries | DNS, load balancers, TLS, routing, egress, ingress, service limits, and runtime constraints. | Open when deployment symptoms cross network, platform, or service boundary layers. |
| rollback-and-blast-radius | Rollback choices, degradation, customer impact, data safety, and containment. | Open when triage needs impact framing or recovery option context. |
| identity-and-principal-boundaries | Users, groups, roles, service accounts, workloads, trust policies, and federation. | Open when an IAM change depends on who or what receives access. |
| permission-scope-and-least-privilege | Actions, resources, conditions, inheritance, deny rules, and privilege minimization. | Open when IAM review depends on whether access scope is necessary and bounded. |
| policy-change-risk | Privilege escalation, cross-account access, public exposure, persistence, and sensitive operations. | Open when a permission change could expand control, data access, or operational risk. |
| audit-evidence-and-separation | Approval evidence, change reason, ownership, logging, break-glass access, and separation of duties. | Open when IAM review needs governance, traceability, or accountability evidence. |
| provider-operations-context | AWS, Azure, GCP, Kubernetes, serverless, managed services, and provider naming differences. | Open when provider-specific terms or platform concepts affect interpretation. |

## Out Of Scope

- Activation rules, workflow steps, output contracts, or procedural behavior.
- Cloud procedural skills, provider-specific runtime docs, runbooks, or tooling.
- Role prompt content, deployment automation, incident command policy, security
  policy authorship, or validator tooling.

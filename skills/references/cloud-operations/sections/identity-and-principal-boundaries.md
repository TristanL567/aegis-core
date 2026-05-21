relevant-when: Open this drawer when an IAM change depends on who or what receives access.

# Identity And Principal Boundaries

- IAM review starts by naming the principal: human user, group, role, service
  account, workload identity, managed identity, federated subject, or external
  account.
- Trust policy and permission policy are separate concerns. A principal may be
  allowed to assume a role while the role's permissions define what it can do.
- Workload identity should be scoped to the workload boundary: service,
  namespace, function, job, tenant, environment, account, project, subscription,
  or cluster.
- Cross-account and federated access need issuer, audience, subject, external
  id, session constraints, and revocation path evidence where applicable.
- Shared service accounts and broad groups weaken accountability because they
  hide which workload or person actually used the access.
- Principal boundaries should distinguish production from nonproduction,
  human from machine, temporary from durable, and break-glass from routine
  access.

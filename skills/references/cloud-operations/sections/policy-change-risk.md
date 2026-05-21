relevant-when: Open this drawer when a permission change could expand control, data access, or operational risk.

# Policy Change Risk

- High-risk IAM changes include policy administration, role assumption,
  privilege delegation, key management, secrets access, audit log mutation,
  network perimeter changes, and production write access.
- Privilege escalation can appear through indirect permissions: attach policy,
  pass role, create service account token, update function code, modify
  workload identity, write deployment config, or change trust relationships.
- Public, cross-account, cross-tenant, or externally federated access needs
  explicit justification and resource-level constraints.
- Data exposure risk depends on resource sensitivity, action type, export
  ability, encryption controls, logging, and whether access is read, write,
  delete, administer, or impersonate.
- Persistence risk increases when access is durable, hard to audit, broad,
  inherited, or able to create new credentials.
- A permission can be operationally necessary and still require compensating
  controls such as time bounds, approval evidence, monitoring, or break-glass
  classification.

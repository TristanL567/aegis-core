relevant-when: Open this drawer when IAM review depends on whether access scope is necessary and bounded.

# Permission Scope And Least Privilege

- Permission scope includes allowed actions, denied actions, resources,
  conditions, tags, regions, accounts, projects, subscriptions, and inherited
  policies.
- Least privilege means the access is sufficient for the stated task and no
  broader than necessary across action, resource, time, environment, and
  principal.
- Conditions can narrow access by source network, MFA, resource tag, request
  tag, session name, organization boundary, time, region, or workload identity
  claim.
- Explicit deny rules, service control policies, permission boundaries, and
  resource policies can override apparent grants.
- Wildcards are highest risk when they apply to sensitive services, write
  actions, policy management, secrets, keys, identity, networking, logging, or
  production resources.
- Review should account for inherited access through groups, roles, managed
  policies, nested assignments, and resource-level grants.

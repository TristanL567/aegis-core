relevant-when: Open this drawer when failure may come from runtime configuration or dependency mismatch.

# Configuration And Dependency Drift

- Runtime drift can come from environment variables, secrets, config maps,
  feature flags, image tags, dependency versions, infrastructure modules,
  region settings, certificates, or provider defaults.
- Mutable tags and implicit latest versions make reproduction harder; stable
  digests, lockfiles, pinned modules, and recorded config snapshots improve
  evidence.
- Secret rotation, expired credentials, missing permissions, wrong key versions,
  and region-specific secret stores can break only some deployments.
- Feature flags can change behavior without a code deploy and should be checked
  against the affected users, tenants, routes, and timestamps.
- Infrastructure drift includes manual console changes, partial apply failures,
  stale state, unmanaged resources, and provider-side default changes.
- Dependency evidence should distinguish application dependency failure from
  network path, IAM permission, quota, schema, contract, or data-shape mismatch.

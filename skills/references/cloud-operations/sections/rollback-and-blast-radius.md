relevant-when: Open this drawer when triage needs impact framing or recovery option context.

# Rollback And Blast Radius

- Blast radius should identify affected environments, regions, tenants,
  customers, routes, jobs, data flows, queues, and privileged operations.
- Rollback safety depends on database migrations, schema compatibility,
  message formats, cached data, irreversible external effects, and whether old
  versions can read new state.
- Recovery options include rollback, roll forward, disable a feature flag,
  shift traffic, scale capacity, restart workers, pause jobs, drain queues,
  restore config, or degrade noncritical features.
- Rollback can be risky when the failed deployment already performed writes,
  changed schema, altered permissions, or triggered external side effects.
- Containment should favor the smallest effective scope: tenant, route, queue,
  region, feature, or permission boundary before broad service shutdown.
- Impact evidence should distinguish user-visible failure from internal alert,
  delayed processing, degraded latency, data risk, and security exposure.

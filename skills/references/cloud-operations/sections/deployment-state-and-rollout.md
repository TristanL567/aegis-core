relevant-when: Open this drawer when a deployment failure depends on what changed, where it rolled out, or what is currently serving.

# Deployment State And Rollout

- Deployment triage should identify the exact artifact, version, image digest,
  commit, configuration bundle, migration, and infrastructure change that
  reached each environment.
- Rollout state includes desired version, observed version, replica health,
  readiness, liveness, traffic split, canary stage, and whether old and new
  versions are serving simultaneously.
- A failure can be partial: one region, availability zone, tenant, route,
  worker, queue, function, or dependency path may be affected while others are
  healthy.
- Health checks can fail because of the application, dependency reachability,
  slow startup, credential errors, resource limits, bad probes, or platform
  scheduling.
- Deployment timestamps should be compared with first symptom time, alert time,
  traffic shift, autoscaling events, and dependency change windows.
- Ownership evidence should distinguish application code changes from platform,
  infrastructure, configuration, data, and third-party service changes.

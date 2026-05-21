relevant-when: Open this drawer when cloud triage depends on runtime evidence rather than code inspection alone.

# Observability And Logs

- Useful triage evidence includes structured logs, error rates, latency,
  saturation, resource usage, traces, deployment events, audit events, and
  dependency health.
- Logs should be filtered by time window, environment, service, version,
  region, tenant, correlation id, request path, worker name, and severity where
  those dimensions exist.
- Metrics should separate symptom from cause: high latency, retries, queue
  depth, CPU, memory, connection exhaustion, throttling, and error counts can
  amplify each other.
- Distributed traces are strongest when they show failing spans, dependency
  calls, retries, timeout boundaries, and changed code paths.
- Alert absence is not evidence of health when dashboards lack coverage,
  thresholds are stale, sampling is high, or telemetry broke during deploy.
- Evidence should include enough timestamp and scope detail to tie the observed
  symptom to a deployment, platform, dependency, or IAM change.

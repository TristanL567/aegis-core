relevant-when: Open this drawer when deployment symptoms cross network, platform, or service boundary layers.

# Networking And Runtime Boundaries

- Cloud failures can sit at DNS, TLS, load balancer, ingress, service mesh,
  firewall, security group, route table, NAT, egress, private endpoint, or
  identity-aware proxy boundaries.
- Runtime limits include CPU, memory, disk, ephemeral storage, file handles,
  connection pools, request body size, timeout ceilings, concurrency, and
  provider quotas.
- Symptoms should be mapped to the boundary where they appear: client request,
  edge, load balancer, application, worker, queue, database, cache, or external
  service.
- TLS and certificate failures often depend on hostname, certificate chain,
  expiration, trust store, SNI, and environment-specific termination points.
- Network policy changes can affect only egress, only ingress, only private
  routes, or only cross-region and cross-account paths.
- Platform-specific status codes and timeout behavior should be interpreted as
  provider reference context, not as a procedure for any one provider.

relevant-when: Open this drawer when IAM review needs governance, traceability, or accountability evidence.

# Audit Evidence And Separation

- IAM change evidence should name requester, owner, approver, purpose, ticket or
  change record, affected principals, affected resources, environment, and
  expiration or review date.
- Approval should be independent enough for the risk level. Self-approval is
  weak for production, privileged, security-sensitive, or cross-boundary access.
- Auditability depends on logs for policy changes, role assumption, token use,
  secret access, key use, administrative actions, and failed access attempts.
- Break-glass access should be time-bound, monitored, justified, and reviewed
  after use.
- Separation of duties matters when a principal can both change controls and
  operate the resource protected by those controls.
- Evidence should distinguish intended access from effective access after
  inheritance, conditions, denies, resource policies, and organization controls.

---
trigger:
  - "A ticket envelope is available and worker output, staged files, or a supplied changed-file list must be checked against allowed_areas and must_not_touch."
  - "A validator, worker, or master needs executable evidence that changed paths stay inside one ticket's declared scope."
  - "A completion report claims scope compliance for a ticket-owned change and changed paths can be enumerated."
non_trigger:
  - "No ticket envelope with allowed_areas and must_not_touch is available."
  - "The task is broad repository triage, cross-ticket planning, or ledger maintenance rather than validating one ticket's changed paths."
  - "The question is about code correctness, security, maintainability, human readability, or acceptance criteria beyond changed-file scope."
  - "The user explicitly asks for prose-only review and no executable validation."
failure_modes_addressed:
  - "Files outside allowed_areas are modified while the completion report claims the work stayed inside ticket scope."
  - "Files under must_not_touch are modified because the model treats protected paths as advisory instead of blocking."
  - "Validators rely only on prose judgment for scope checks even when the ticket envelope can be checked mechanically."
  - "Completion reports claim scope compliance without executable evidence from a deterministic scope firewall."
attention_signals:
  - "The ticket path and ticket YAML containing allowed_areas and must_not_touch, either as a plain YAML envelope or markdown YAML frontmatter."
  - "Changed file paths from git diff --name-only, git diff --cached --name-only, or an explicit changed-file list."
  - "Directory entries ending in / that must be treated as path prefixes."
  - "Protected paths that also appear inside allowed areas; must_not_touch takes priority."
  - "Completion-report language that says scope was preserved but does not name a validator command or result."
procedure:
  - "Read the ticket envelope and identify allowed_areas and must_not_touch exactly as declared in plain YAML or markdown YAML frontmatter."
  - "Enumerate changed paths from explicit evidence or from staged files when validating commit readiness."
  - "Run tools/validate_ticket_scope.py with --ticket and either repeated --changed-file values or --staged."
  - "Treat a nonzero exit as a blocking scope violation and report each violating path with the tool's reason."
  - "Treat exit 0 as executable scope evidence, then continue any adjacent correctness, acceptance, or readability review separately."
scope_boundary:
  - "Covers deterministic changed-file validation for one ticket envelope's allowed_areas and must_not_touch path lists."
  - "Does not implement a ticket ledger, infer ownership for ambiguous changes, validate acceptance criteria, review code correctness, or decide cross-ticket orchestration."
  - "Does not stage files, commit changes, modify protected paths, alter clean-commit behavior, or add provider-specific workflow."
composition_points:
  - "Code validator invokes this procedure and tools/validate_ticket_scope.py before relying on prose scope judgment."
  - "Clean-commit composes with this procedure when staged files need a mechanical scope check before commit readiness."
  - "Operating discipline supplies always-on one-ticket boundaries and protected-path behavior."
  - "Master role handles sequencing and remediation routing when the scope firewall rejects a change."
reference_pointers: []
verification:
  - "Run a passing example with a changed file inside allowed_areas and confirm the tool exits 0 with a concise success message."
  - "Run a rejecting example with a changed file outside allowed_areas or under must_not_touch and confirm the tool exits nonzero with a clear violation message."
  - "For staged validation, run the tool with --staged from the repository root and compare the reported paths to git diff --cached --name-only when needed."
output_contract:
  - "status: passed, failed, or not_applicable."
  - "ticket: ticket envelope path used for validation."
  - "changed_files: paths checked, whether supplied explicitly or read from staged git state."
  - "scope_firewall_command: exact validate_ticket_scope.py command or staged-mode equivalent."
  - "scope_firewall_result: exit status and concise pass/fail evidence."
  - "findings: blocking scope violations, if any, naming outside allowed_areas or under must_not_touch."
---

# Ticket Scope Validation

Use this procedure when a ticket-owned change needs executable scope evidence. The scope firewall is `tools/validate_ticket_scope.py`; it reads either a canonical plain YAML ticket envelope or a markdown ticket with YAML frontmatter, then checks changed paths against `allowed_areas` and `must_not_touch`.

Run it with explicit paths:

```powershell
py -3.10 .\tools\validate_ticket_scope.py --ticket .\epics\EXAMPLE\tickets\TICKET.yaml --changed-file tools/example.py
```

Run it against staged paths:

```powershell
py -3.10 .\tools\validate_ticket_scope.py --ticket .\epics\EXAMPLE\tickets\TICKET.yaml --staged
```

Exit 0 means every checked path is inside or equal to an allowed area and not inside or equal to a protected path. A nonzero exit means at least one checked path violates the ticket envelope. `must_not_touch` has priority over `allowed_areas`, so a protected path is rejected even if it also matches an allowed area.

This procedure only validates changed-file scope. Continue using the validator role, operating discipline, and ticket acceptance criteria for correctness, security, maintainability, verification completeness, and human-readable reporting.

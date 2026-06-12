---
id: verify-binding
stage: init
mode: any
audience: human
target_role: none
pairs_with:
  - prompts/01-init/use-aegis-core.md
  - prompts/06-control/status-report.md
requires:
  - AEGIS.md
  - contracts/kernel.md
returns:
  - binding verification
  - standard role envelope
---

# Verify Binding

## When to use

Use this prompt mid-session when an agent may have drifted from AEGIS-CORE
binding, lost ticket state, or started routing without clear role locks.

## Preconditions

- The session claims to be using AEGIS-CORE.
- The operator can provide any known ticket, ledger, or prior envelope context.

## Prompt

```text
Verify your current AEGIS-CORE binding before doing any further work.

Load or re-check:
- AEGIS.md
- contracts/kernel.md
- contracts/swarm-contract.md
- contracts/ticket-contract.md
- contracts/epic-contract.md when epic routing is active
- the active skills/roles/<role>/SKILL.md file for your current role

Return:
1. current role and role path, or "unbound";
2. role lock and MUST NOT rules, citing the canonical file paths;
3. active ticket ID, goal, allowed_areas, must_not_touch, acceptance criteria,
   and verification commands, or the missing fields that block work;
4. current routing state from the last standard role envelope;
5. whether any work occurred before a valid ticket envelope or outside the
   current role lock.

Known context:
[KNOWN_CONTEXT]

Do not edit, stage, commit, continue execution, or request validation while this
verification is incomplete.
```

## Expected response

- Binding status and role path.
- Ticket readiness or missing-field blockers.
- Any drift findings.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | master | `prompts/03-execute/relay/dispatch-master-agent.md` |
| completed | validator | `prompts/04-validate/conformance-check.md` |
| needs_clarification | human | `prompts/01-init/bind-strict.md` |
| blocked | human | `prompts/06-control/recover-context.md` |

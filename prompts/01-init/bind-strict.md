---
id: bind-strict
stage: init
mode: any
audience: human
target_role: skills/roles/master/
pairs_with:
  - prompts/01-init/use-aegis-core.md
  - prompts/01-init/verify-binding.md
requires:
  - AEGIS.md
  - contracts/kernel.md
returns:
  - strict binding acknowledgment
  - standard role envelope
---

# Bind Strict

## When to use

Use this hardened binding prompt when the operator wants the agent to refuse all
work until it proves AEGIS-CORE load order, role lock, and ticket state.

## Preconditions

- The agent can access AEGIS-CORE files.
- The operator wants an explicit acceptance gate before planning or execution.

## Prompt

```text
Enter strict AEGIS-CORE binding mode.

You must not plan, edit, validate, stage, commit, push, summarize completion, or
route work until the human explicitly accepts your STRICT BINDING ACKNOWLEDGMENT.

Load:
- AEGIS.md
- contracts/kernel.md
- contracts/swarm-contract.md
- contracts/ticket-contract.md
- contracts/epic-contract.md when epic work is requested
- the active role file under skills/roles/

Return a STRICT BINDING ACKNOWLEDGMENT with:
- loaded files in order and first heading from each file;
- declared current role and target role path;
- three role-specific MUST NOT rules, citing canonical paths;
- current ticket envelope, or every missing field required before work;
- planned next prompt from prompts/README.md after human acceptance.

Requested role or workflow:
[REQUESTED_ROLE_OR_WORKFLOW]

Target project or ticket context:
[TARGET_PROJECT_OR_TICKET_CONTEXT]

If any required file, role, or ticket field is unavailable, return
status: blocked and next_recommended_role: human.
```

## Expected response

- Strict acknowledgment.
- Blocking missing fields if any.
- No plan or implementation content.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | human | human accepts binding, then use the named next prompt |
| needs_clarification | human | `prompts/01-init/verify-binding.md` |
| blocked | human | `prompts/06-control/halt.md` |

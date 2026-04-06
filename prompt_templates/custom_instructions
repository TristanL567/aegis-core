# Aegis Core Prompt Playbook

This file contains provider-facing starter prompts that align with the canonical
`master / worker / validator` model in this repository.

## 1. Kick Off the Swarm

Use this when you want the `master` skill to take ownership of a new task.

> "Activate the `master` skill for project **[PROJECT_NAME]**.
>
> **Goal:** [DESCRIBE_THE_OBJECTIVE]
>
> **Context:** [PATHS, DATA SOURCES, CONSTRAINTS, OR ARCHITECTURE NOTES]
>
> **Instructions:**
> 1. Break the work into the next actionable steps or phases.
> 2. Assign the right `worker` skill for each execution step.
> 3. Route execution outputs through a `validator` before asking me for approval.
> 4. Only ask me for approval when a true checkpoint is ready."

## 2. Route a Backend Task

> "Activate the `backend-worker` skill.
>
> **Task:** [BACKEND TASK]
> **Context:** [FILES, APIS, REQUIREMENTS, CONSTRAINTS]
>
> When complete, return a structured result and recommend routing to a validator."

## 3. Route a Modeling Interpretation Task

> "Activate the `model-interpreter-worker` skill.
>
> **Task:** [INTERPRETATION TASK]
> **Context:** [MODEL TYPE, METRICS, FEATURE OUTPUTS, DOMAIN CONTEXT]
>
> Use both a statistical lens and a domain lens. Flag anomalies explicitly."

## 4. Route a Chart Task

> "Activate the `chart-worker` skill.
>
> **Task:** [CHART REQUEST]
> **Data Source:** [PATH]
> **Output Destination:** [PATH]
> **Styling Constraints:** [LIST CONSTRAINTS]
>
> Return artifacts and recommend validation if the output is ready for review."

## 5. Run Validation

General review:

> "Activate the `code-validator` skill and review the latest worker output.
>
> Return a blocking verdict if the work has issues, and route the result back to the master."

Data science review:

> "Activate the `ds-validator` skill and review the latest data or modeling output.
>
> Check for leakage, inefficiency, and reproducibility issues. Route the result back to the master."

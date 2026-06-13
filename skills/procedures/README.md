# Procedure Index

One row per procedure folder under `skills/procedures/`. `standalone` reflects local `standalone: true` metadata; absent metadata is indexed as `false`.

| procedure | trigger summary | composing roles | standalone |
| --- | --- | --- | --- |
| accessibility-audit | Audit, review, verify, or report accessibility behavior for an existing UI screen, flow, or component. | none found | false |
| backtest-validation | Validate, review, trust, compare, or report a trading strategy, factor model, volatility strategy, option strategy, or portfolio signal backtest. | none found | false |
| chart-artifact-generation | Generate, export, render, save, or deliver a chart artifact such as PNG, SVG, PDF, HTML, or workbook-embedded chart. | chart-worker | false |
| clean-commit | Prepare, review, or describe a git commit for a single ticket-owned change. | code-validator, ds-validator | false |
| cloud-iam-change-review | Review, approve, modify, or justify cloud IAM, service account, role, policy, secret, deployment access, or trust-policy changes. | none found | false |
| codebase-map-generation | Produce graph or context evidence for a new or unfamiliar target project before planning, onboarding, or first implementation. | code-validator, master | true |
| deployment-failure-triage | Triage deployment, service startup, cloud run, container, CI/CD, or production-like runtime failures. | none found | true |
| design-clarification-interview | Clarify product, business, design, architecture, or workflow intent before implementation proceeds. | master-planner, ticket-planner-worker | true |
| frontend-component-implementation | Add, modify, repair, or integrate one frontend component or tightly scoped component behavior. | none found | false |
| investment-thesis-evidence-check | Review, accept, strengthen, summarize, or qualify an investment thesis, stock or fund note, sector view, or portfolio rationale. | none found | false |
| model-calibration-review | Review whether predicted probabilities, confidence scores, risk estimates, or probability bins are reliable for decisions. | none found | false |
| model-output-interpretation | Interpret, explain, summarize, or narrate existing model output, diagnostics, feature effects, predictions, or attributions. | model-interpreter-worker | false |
| module-boundary-review | Review planned or completed changes that risk crossing module ownership, public interfaces, shared helpers, or layers. | none found | false |
| new-api-endpoint | Add a new API endpoint, route, handler, controller action, RPC method, webhook receiver, or externally callable backend surface. | backend-worker, code-validator, ds-validator | false |
| portfolio-rebalancing-review | Review, accept, reject, or qualify a portfolio rebalance suggestion, allocation update, target-weight correction, or drift-based trade plan. | none found | false |
| risk-metric-reconciliation | Compare, reconcile, trust, summarize, or explain risk metrics across portfolios, strategies, funds, reports, backtests, or risk artifacts. | none found | false |
| test-first-change | Change executable behavior where a test, reproduction, fixture, command, or reproducible check is feasible before implementation. | none found | false |
| ticket-scope-validation | Check worker output, staged files, or changed-file lists against ticket `allowed_areas` and `must_not_touch`. | code-validator, ds-validator | false |
| training-run-diagnostics | Diagnose training runs, model performance issues, failed experiments, surprising metrics, or degraded model results before model-code changes. | none found | false |
| ubiquitous-language-map | Map ambiguous, inconsistent, overloaded, or misaligned vocabulary across requests, code, docs, tests, schemas, routes, or UI. | ticket-planner-worker | true |

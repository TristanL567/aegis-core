---
trigger:
  - "A task asks to generate, export, render, save, or deliver a chart artifact such as a PNG, SVG, PDF, HTML chart, or workbook-embedded chart."
  - "A chart-producing script, notebook, worker, or report step must leave behind an auditable artifact path and evidence that the artifact is reproducible."
  - "A completion report claims a chart artifact was produced and the artifact can be checked for existence, nonblank visual output, and data limitation notes."
non_trigger:
  - "The task is visual-style conformance, brand polish, typography, accessibility palette review, or chart appearance QA; use the future visual-style-conformance procedure for that concern."
  - "The task is chart data-quality investigation, source-data validation, outlier diagnosis, missingness analysis, or data provenance review; use the future chart-data-quality-investigation procedure for that concern."
  - "The task is model interpretation, statistical explanation, causal analysis, or analytical claim validation rather than artifact generation."
  - "The task is frontend chart embedding, interactive application integration, dashboard wiring, or client-side rendering behavior; use a future frontend chart embedding procedure for that concern."
  - "The task is broad report writing, narrative synthesis, document structure, or prose-heavy analytical communication; use a future report-writing procedure for that concern."
failure_modes_addressed:
  - "AI-generated chart artifacts can be produced without a reproducible artifact path, data-quality note, or visual/nonblank verification."
attention_signals:
  - "Requested artifact formats, filenames, output directories, render commands, export functions, and downstream consumers that need a stable path."
  - "Chart source inputs, generated data files, scripts, notebooks, seeds, parameters, and commands needed to reproduce the artifact."
  - "Visual evidence that the exported chart may be blank, clipped, unreadable, stale, or saved to an unexpected path."
  - "Data limitations such as missing data, filtering, aggregation, stale extracts, incomplete coverage, or provisional values that materially affect the artifact."
  - "Reference pointer conditions for chart claim, chart type, context, encoding, scales, styling, and export legibility."
procedure:
  - "Classify the chart artifact request, expected output format, destination path, source inputs, and generation path."
  - "Open the matching charting reference drawers from reference_pointers when artifact design or export details need reference knowledge."
  - "Generate or update the artifact through a reproducible script, notebook, command, or documented render path."
  - "Save the artifact to a stable path and record the generation evidence needed to regenerate it."
  - "Verify artifact existence, nonblank/manual visual review, and any required data-quality note."
  - "Route excluded concerns to their owning procedures or roles."
scope_boundary:
  - "Covers the narrow procedure for producing an auditable chart artifact: generation path, stable artifact path, reproducibility evidence, existence check, nonblank/manual visual review, and data-quality note when limitations affect the artifact."
  - "Does not cover visual-style conformance, brand polish, typography systems, palette approval, accessibility style review, or chart appearance governance."
  - "Does not cover chart data-quality investigation, source-data auditing, missingness diagnosis, outlier analysis, provenance review, or statistical interpretation of the underlying data."
  - "Does not cover model interpretation, frontend chart embedding, dashboard integration, interactive client behavior, broad report writing, or narrative synthesis."
composition_points:
  - "reference_pointers bind this procedure to charting-artifact-reference drawers for chart claim, encoding, scale, styling, and export legibility knowledge."
  - "Future visual-style-conformance procedure owns appearance, brand, accessibility palette, typography, and visual polish checks beyond nonblank artifact usability."
  - "Future chart-data-quality-investigation procedure owns source-data validation, missingness, outliers, provenance, and data limitation diagnosis beyond noting known artifact limitations."
  - "Future frontend chart embedding procedure owns application integration, dashboard wiring, responsiveness, and client-side rendering behavior."
  - "Future report-writing procedure owns narrative synthesis, report structure, surrounding prose, and non-artifact analytical communication."
reference_pointers:
  - ref: charting-artifact-reference
    section: claim-and-chart-type
    open_when: "Open when the artifact's intended analytical comparison or chart form needs to be checked."
  - ref: charting-artifact-reference
    section: context-and-encoding
    open_when: "Open when titles, labels, legends, units, source notes, or encodings need reference guidance."
  - ref: charting-artifact-reference
    section: scales-and-styling
    open_when: "Open when scale, transformation, styling, contrast, or readability choices materially affect interpretation."
  - ref: charting-artifact-reference
    section: export-legibility
    open_when: "Open when the artifact is being exported, saved, reused, or inspected at final size."
verification:
  - "Verify the chart artifact exists at the exact reported output path after generation or export."
  - "Verify the generation path is reproducible by naming the script, notebook, command, parameters, seed, or documented render path used to create the artifact."
  - "Verify the exported chart is not blank through file inspection, rendered preview, screenshot, or manual visual review appropriate to the format."
  - "Verify the artifact has been manually reviewed for obvious clipping, stale output, unreadable labels, missing title or units, and unusable export size."
  - "Verify a data-quality note is included when data limitations, filtering, aggregation, stale extracts, missing coverage, or provisional inputs materially affect the artifact."
output_contract:
  - "status: completed, blocked, or not_applicable."
  - "artifact_path: exact path to each generated or exported chart artifact."
  - "generation_path: script, notebook, command, render step, parameters, seed, or documented process sufficient to reproduce the artifact."
  - "source_inputs: data files, queries, extracts, or upstream artifacts used to generate the chart when known."
  - "existence_check: evidence that each artifact exists at the reported path after generation."
  - "visual_review: nonblank/manual visual review method, result, and any remaining visual usability concerns."
  - "data_quality_note: known data limitations affecting the artifact, or explicit none_known when no material limitation is known."
  - "excluded_concerns: adjacent visual-style, data-quality investigation, frontend embedding, model interpretation, or report-writing concerns intentionally left to their owning procedure or role."
---

# Chart Artifact Generation

Use this procedure when the work is to generate, export, render, save, or deliver a chart artifact. It keeps the completion evidence centered on the artifact path, the reproducible generation path, a nonblank/manual visual review, and any data-quality note needed for known limitations that materially affect the artifact.

This procedure uses `reference_pointers` to open only the needed `charting-artifact-reference` drawers. It does not own visual-style conformance, chart data-quality investigation, model interpretation, frontend chart embedding, or broad report writing; those concerns belong to adjacent future procedures or roles.

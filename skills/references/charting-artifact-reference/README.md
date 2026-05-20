# Charting Artifact Reference

## Scope

Reference scope: Axis-2 knowledge for chart artifacts: the shared facts,
constraints, and quality expectations that future chart procedures should use
when producing chart deliverables.

It is not a procedural skill and is not independently triggerable. The
consuming skill is `chart-artifact-generation`.

## Artifact Knowledge

- Chart artifacts should communicate a specific analytical claim or comparison,
  not simply display available data.
- The chart type should match the analytical task: comparisons, trends,
  distributions, relationships, or composition.
- Titles, subtitles, axis labels, legends, units, and source notes should make
  the artifact understandable without requiring surrounding prose.
- Encodings should favor accurate interpretation: position and length for
  precise comparison, color for grouping or emphasis, and restrained annotation
  for important context.
- Scales should be explicit and defensible. Truncation, dual axes, transformed
  scales, and aggregation choices should be visible when they materially affect
  interpretation.
- Styling should support the data rather than dominate it. Use consistent
  typography, adequate contrast, readable labels, and accessible color choices.
- Exported artifacts should preserve legibility at their intended size and
  format, including embedded or accompanying metadata needed for reuse.

## Out Of Scope

- Procedural trigger logic, workflow steps, or activation rules.
- Role prompt content.
- Implementation details for any specific chart worker.

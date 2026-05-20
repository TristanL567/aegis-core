relevant-when: Open this drawer when aggregate metrics may hide subgroup, class, or segment failures.

# Segment Evaluation

- Aggregate metrics can hide weak performance in minority classes, sparse
  slices, recent cohorts, rare labels, or high-risk operating regions.
- Segment metrics should include support counts. Very small slices can produce
  unstable estimates that should be treated as signals for review rather than
  definitive conclusions.
- Compare segment performance against the model objective and harm surface.
  Equal aggregate performance can still be unacceptable if errors concentrate
  in critical or protected segments.
- Missing segment labels, proxy segment definitions, or post-hoc slicing should
  be named as limitations when they affect interpretation.

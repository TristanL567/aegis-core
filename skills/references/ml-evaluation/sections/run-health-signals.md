relevant-when: Open this drawer when a training run needs diagnostic interpretation from logged metrics or curves.

# Run Health Signals

- Training and validation curves should be read together. Diverging curves can
  indicate overfitting; flat poor curves can indicate underfitting, weak signal,
  optimization problems, or data issues.
- Volatile validation metrics may reflect small validation sets, unstable
  splits, high learning rates, stochastic training variance, or noisy labels.
- Early stopping, checkpoint selection, and best-epoch claims should identify
  the monitored metric and whether the chosen checkpoint generalizes beyond one
  noisy validation peak.
- Compare train, validation, and test evidence before concluding that a run
  improved. A single final metric without run history is weak diagnostic
  evidence.

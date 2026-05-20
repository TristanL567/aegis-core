relevant-when: Open this drawer when evaluation credibility depends on train, validation, test, time, group, or leakage boundaries.

# Data Split Integrity

- Evaluation evidence depends on split validity. Random splits can leak future
  information, repeated entities, household or account groups, or duplicate
  examples into validation or test sets.
- Time-dependent tasks should respect chronology unless the modeling problem
  explicitly permits shuffled observations.
- Grouped data should keep related entities in the same split when information
  can transfer across group members.
- Feature construction, imputation, scaling, target encoding, and selection
  must be fit inside the training boundary before evaluation evidence is trusted.
- Leakage suspicion should downgrade confidence in all downstream metrics until
  the split and preprocessing boundaries are checked.

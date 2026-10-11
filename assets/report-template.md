# [Experiment name]

Status: [complete / partial / blocked] · Report date: [YYYY-MM-DD]

## Objective

[Question, hypothesis, and what the experiment can establish.]

## Why this experiment

[Mechanism, origin of the idea, linked primary source or dated discussion, and adaptations.]

## Available data

| Cohort | Role | Patients | Slides | Deaths / censored or class distribution |
| --- | --- | --- | --- | --- |
| [Cohort] | [Development / external] | [N] | [N] | [Counts and percentages] |

[Endpoint, inclusion criteria, representations and relevant missingness.]

## Splits

[Exact frozen split protocol; patient grouping; preprocessing, selection, and external ensembles.]

## Evaluation metrics

[Plain-language definitions, horizons, direction, confidence intervals, and comparison approach.]

## Results

### Development validation

| Configuration | [Primary metric, 95% CI] | [Secondary metric, 95% CI] |
| --- | --- | --- |
| [Experiment] | [Value and interval] | [Value and interval] |
| [Applicable manuscript baseline] | [Value and interval] | [Value and interval] |

### External validation

| Configuration | [Primary metric, 95% CI] | [Secondary metric, 95% CI] |
| --- | --- | --- |
| [Experiment] | [Value and interval] | [Value and interval] |
| [Applicable manuscript baseline] | [Value and interval] | [Value and interval] |

[Bold the best point estimates and explain that this is a descriptive ranking.]

### Comparison with manuscript models

[Paired differences and 95% intervals, or why a matched comparison is unavailable.]

[Relevant plot with a meaningful caption, if available.]

## Conclusions

[Explain what was done, whether the question was answered, how it compares to the manuscript, and what uncertainty means for the decision.]

[Discuss verified overlays when available; otherwise say whether this model provides attention.]

**Recommendation:** [Continue / Run a targeted check / Do not invest further in this configuration].

**Reason:** [Evidence tied to the tables.]

**Next step:** [One concrete action; do not execute new experiments as part of reporting.]

## Appendix

### Complete secondary results

[All remaining tables, per-fold details and diagnostics needed for this report.]

### Technical and statistical protocol

[Settings, training budget and selection, score definitions, ensemble, estimator, censoring conventions, bootstrap counts/seed and valid replicates.]

### Sources and reproducibility

[Input artifacts, code/checkpoint references, provenance and versions; exclude credentials.]

### Limitations and anomalies

[Missing outputs, protocol differences, validation qualifications and unresolved issues.]

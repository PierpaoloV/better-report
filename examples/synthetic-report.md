# Boosted trees versus a linear classifier

Status: Synthetic example · Report date: Not applicable

**All task details, counts, scores and confidence intervals below are fictional. They illustrate report structure and were not computed from real or simulated observations. This is not an experimental result.**

## Objective

Illustrate how to report whether a more flexible classifier improves detection of defective items compared with an established linear classifier.

## Why this experiment

The hypothetical idea is that combinations of sensor measurements may identify defects better than a linear decision rule. Boosted trees can capture such interactions. This is an illustrative methodological rationale, not an experiment attributed to a publication or a real user discussion.

## Available data

| Fictional population | Role | Items | Defective | Non-defective |
| --- | --- | --- | --- | --- |
| Development set | Training / validation | 400 | 200 (50%) | 200 (50%) |
| Separate production batch | Independent test | 100 | 50 (50%) | 50 (50%) |

Each item hypothetically has ten numeric sensor measurements and a binary quality-control label. There are no repeated items or missing measurements in this fictional scenario.

## Splits

The illustrative protocol uses five stratified development folds, with 320 training items and 80 validation items per fold. Each item appears in one validation fold. Preprocessing is fitted on training items only. Hyperparameters are fixed before evaluation. The separate batch is not used for model selection; its predictions average the five development models.

## Evaluation metrics

ROC AUC measures whether defective items tend to receive higher scores than non-defective items. Higher is better, and 0.5 is the usual chance reference. Accuracy measures the fraction classified correctly at a threshold fixed before test evaluation.

The displayed intervals illustrate what saved 95% confidence intervals might look like. Paired differences mean boosted trees minus the linear baseline, evaluated on the same items. No bootstrap computation was performed for this example.

## Results

### Development validation

| Configuration | ROC AUC [95% CI] | Accuracy [95% CI] |
| --- | --- | --- |
| Linear baseline | 0.720 [0.670, 0.770] | 0.680 [0.630, 0.730] |
| Boosted trees | **0.750** [0.700, 0.800] | **0.700** [0.650, 0.750] |

### Independent test

| Configuration | ROC AUC [95% CI] | Accuracy [95% CI] |
| --- | --- | --- |
| Linear baseline | 0.740 [0.650, 0.830] | 0.690 [0.600, 0.780] |
| Boosted trees | **0.770** [0.680, 0.860] | **0.710** [0.620, 0.800] |

Bold marks the highest point estimate in each column. This is a descriptive ranking, rather than proof that one method is better.

### Comparison with the established benchmark

| Population | Delta ROC AUC [95% CI] | Delta accuracy [95% CI] |
| --- | --- | --- |
| Development validation | +0.030 [-0.010, +0.070] | +0.020 [-0.020, +0.060] |
| Independent test | +0.030 [-0.020, +0.080] | +0.020 [-0.030, +0.070] |

Every fictional difference interval includes zero. If these were actual paired estimates, they would not demonstrate an improvement or establish equivalence.

## Conclusions

In this hypothetical example, both methods use the same measurements. Boosted trees score slightly higher, but the uncertainty in their advantage is large enough that the evidence would not establish a reliable gain over the linear baseline. A larger model is therefore not automatically justified by its first-place ranking.

No attention overlays apply to this sensor-classification task. No feature-importance findings are invented for the example.

**Recommendation:** Run a targeted check.

**Reason:** The apparent improvement is small and uncertain; the example does not establish that the extra complexity is useful.

**Next step:** In a real study, predefine an evaluation on another production batch and assess both discrimination and the operational cost of classification errors before choosing the more complex method.

## Appendix

### Complete secondary results

No additional results exist for this fictional example. A real report would include relevant per-fold and secondary metrics here.

### Technical and statistical protocol

An actual report would record preprocessing, estimator settings, seeds, selection criteria, threshold derivation, ensemble construction and the saved uncertainty protocol. These details are intentionally not presented as executed procedures here.

### Sources and reproducibility

This example was written solely to demonstrate the reporting format. There are no input records, fitted models, checkpoints, source-result files or computed statistical outputs behind the illustrative numbers.

### Limitations and anomalies

The example cannot support any scientific or operational conclusion. Its purpose is to show the distinction between a higher observed score and a supported model improvement, and how to explain the next decision plainly.

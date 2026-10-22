# Survival reporting checks

## Populations and protocols

Read current manifests and artifact audits. Keep development training, CV validation, an independent internal test (only if one exists), and external validation distinct. In five-fold 80/20 CV, the 20% is the validation fold; there is no additional independent internal test unless specified. State when validation also selected a checkpoint. Report event/censoring counts and patients contributing cases/controls at each horizon; a small early-event count can make AUC intervals particularly wide.

Keep observed durations and censoring indicators unchanged. Specify survival time origin from verified metadata, rather than assuming diagnosis or surgery. Missing M, stage or treatment values must not be filled implicitly for a report. When the user previously authorized an assumption, label it and preserve its scope.

## Metrics and uncertainty

- C-index measures the ranking of comparable patient pairs; larger is better and 0.5 is the chance reference under the usual interpretation. It does not measure calibrated survival probabilities.
- Cumulative/dynamic AUC distinguishes deaths by a horizon from those surviving beyond it, with censoring handled by the specified estimator. Report exact days and any approximate month labels. Verify the training reference for IPCW, censor-weight lookup limits, ties and score direction. A scalar risk shared across horizons differs from a horizon-specific death probability; label both.
- Brier scores and calibration require actual probabilities or survival curves. Do not invent curves for a risk-only baseline or infer calibration from AUC.
- Report saved development metrics within each fold and their documented aggregate. Scores from independent models need not share a scale; do not silently pool them. State how the fold models produce the external prediction. Any new metric calculation must be part of the authorized analysis, not an implicit addition to reporting.
- Report the saved 95% bootstrap intervals, replication count, seed and valid counts. Patient resampling within folds versus across external patients must match the saved protocol. Fixed-model evaluation bootstrap does not include model refitting or checkpoint-selection uncertainty.
- Report paired patient bootstrap differences when available from saved or authorized analysis: same subjects, resampling draws, endpoints, and metric/censoring definitions. State `experiment minus reference`. A difference interval crossing zero does not demonstrate superiority or equivalence. Separate model intervals and being above chance cannot establish a between-model difference. If paired evidence is missing, state that limitation rather than starting a bootstrap as part of reporting alone.
- Preserve the actual statistical protocol. If repeated exploratory comparisons lack multiplicity adjustment, do not describe unadjusted evidence as confirmatory or claim an adjustment was performed. Put methodological details in the appendix and phrase conclusions accordingly; respect the requested manuscript/report style.

## Stratification and morphology

For Kaplan–Meier groups, report the cutoff, its training-only derivation, group counts, hazard ratio/interval and log-rank result when available. An OOF risk cutoff applied to an ensemble may involve different calibration; explain this if relevant. Never optimize a cutoff on external outcomes during reporting. Ranking and dichotomized stratification are different questions.

WSI attention maps require verified feature coordinates, image/mask identity, physical resolution, normalization, and fold/ensemble attribution. Identify low/high risk case selection and any outcome-informed selection. Do not imply that attention proves morphology, recurrence risk, or clinical mechanism. Describe visible structures tentatively unless reviewed by a qualified pathologist.

## Manuscript and benchmark comparisons

Locate the applicable manuscript or benchmark and the saved results for the requested split protocol instead of hardcoding their numbers. Select the relevant Cox, censor-aware regression, discrete-time, or aggregator baseline. Check encoder, resolution, ROI, eligible population and documented exclusions. A recomputed baseline may have different intervals from its original report because the estimator or draws changed; label which protocol was used. Clinical staging from another publication is contextual and cannot establish equivalence on these patients.

# Scientific experiment reporting

Use these checks when the task concerns scientific experiments. Keep the report's result-first structure and focus its detail on the requested work; these checks do not require a fixed list of sections. For survival analyses, also read [survival-reporting.md](survival-reporting.md).

## Explain the experiment

- State the question and why the approach could help. Cite the primary paper, dated discussion or methodological rationale when relevant; describe adaptations and claim exact reproduction only when verified.
- Verify current populations, eligibility, endpoint, inputs, missingness, and class or event counts from saved sources. In biomedical work, distinguish patients and slides; report representation, resolution and ROI when they affect interpretation.
- Describe the frozen evaluation protocol: grouping unit, split or fold roles, tuning and checkpoint selection, training-only preprocessing, and external ensemble construction. Distinguish development validation, an independent internal test if one exists, and external evaluation.
- Explain each reported metric briefly, including direction, units, horizons and the available uncertainty method. Preserve the actual protocol; missing estimates or settings stay explicitly unavailable.

## Report and compare results

Use relevant saved metrics, comparisons, manifests and figures. Compare with the applicable manuscript or established benchmark on matching patients, endpoints, score conventions and estimators. Cross-study values provide context; they are not paired comparisons. When the same input supports multiple approaches, describe it once and identify any departures in the focal experiment.

Report estimates with saved 95% confidence intervals when available. Keep development and external results separate when needed for readability. Show paired differences with their direction and intervals when available; separate model intervals cannot establish a between-model difference. Mark the best point estimate as a descriptive ranking, including the comparator; lower is better for error metrics. Keep consequential negative findings visible and preserve relevant secondary or per-fold results in supporting material.

Reading saved results and checking arithmetic are reporting activities. Re-evaluation, bootstrapping, refitting or a new comparison must belong to the authorized task; otherwise report the missing evidence without manufacturing it. If analysis was authorized and performed, distinguish new calculations from previously saved results.

## Figures and attention

Reuse relevant figures that answer the experimental question, with captions explaining what they show and why it matters. Suitable figures may include discrimination or paired-difference plots, learning curves, calibration or survival curves. Do not add redundant plots to fill a template.

When attention outputs are relevant and available, include verified overlays and representative patches where useful. State case-selection criteria, image/mask identity, feature-coordinate alignment, physical resolution, ROI, normalization or color scale, and model/fold or ensemble attribution. Do not substitute another model's map. Attention indicates model weighting; distinguish visual hypotheses from pathologist-confirmed findings and avoid causal or tissue-identity claims unsupported by evidence. If an expected overlay is unavailable or unverifiable, say so; unrelated reports need no attention disclaimer.

## Interpret and preserve provenance

Answer the experimental question in plain language. A positive result alone does not establish clinical usefulness; a disappointing result alone does not establish that the data are the cause. Carry limitations that change interpretation into the opening summary.

Keep the detailed protocol, secondary tables, settings, source paths, code/checkpoint references, versions, and source hashes when available in supporting material. Include what is needed to inspect or reproduce the reported work, without copying entire logs into the main report.

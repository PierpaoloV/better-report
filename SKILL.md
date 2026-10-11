---
name: better-report
description: Create or update scientific experiment reports as Markdown files, with readable main results, technical appendices, manuscript baseline comparisons, and plain-language recommendations. Use for experiment reports, consolidated benchmark reports, and formal reporting of completed or partial experiments. Also use when the user explicitly invokes better-report. PDF conversion requires a separate explicit request. Brief progress questions do not require generating new report files unless requested.
---

# Better report

Produce reports that let the reader understand the question, the evidence, and the next decision. Write all report content in English, including titles, narrative, table labels, figure captions, conclusions, recommendations, and appendices. Use another language only when explicitly requested.

## Workflow

1. Identify the requested experiments, their completion status, frozen populations and protocols, and the applicable manuscript or established benchmark baselines. Read saved metrics, comparisons, manifests, and existing figures before writing. Ask only for a material ambiguity that cannot be resolved from these sources.
2. Create a dedicated, dated report directory. Treat source data, clinical CSVs, splits, features, checkpoints, training code, and other agents' directories as read-only. Report creation does not authorize training, changing endpoints, new statistical experiments, publishing, or sending messages. Preserve existing reports unless their replacement was requested.
3. For survival experiments, read [survival-reporting.md](references/survival-reporting.md). Use [report-template.md](assets/report-template.md) for each experiment. A consolidated report may share common data/split/metric sections, but must give each experiment its own title, objective, rationale, results, and conclusions, with explicit references to shared sections.
4. Write a readable main body with the most useful tables and figures. Put all remaining technical detail, complete secondary results, settings, provenance, and limitations in the appendix. Keep information that changes interpretation in the main body. Do not impose a page limit or create a separate full-page cover.
5. Deliver the completed `.md` report files. Check that every linked figure resolves, tables are readable, and numeric values match their sources. Link the Markdown deliverables in the final reply. PDF conversion is a separate task requiring a separate explicit user request; this reporting workflow does not automatically create PDF, HTML, or rendering-provenance files.

## Mandatory order and content

Use these sections in this order. The experiment name is the document title.

| Section | Required content |
| --- | --- |
| Objective | The precise question or hypothesis and what a useful result would establish. |
| Why this experiment | Why the method could help; where the idea came from (primary paper, a dated user discussion, or a methodological rationale). Cite the source and describe adaptations. Do not claim an exact reproduction unless verified. |
| Available data | Relevant cohorts, patients, slides, events/censoring or class counts, eligibility, endpoint, representations, resolution, ROI and material missingness. Verify current counts; do not reuse old cover statistics. |
| Splits | Frozen protocol, patient-level grouping, fold counts and roles, selection/tuning procedure, training-only preprocessing, and external ensemble construction. |
| Evaluation metrics | Brief definitions, direction of improvement, horizons and units, uncertainty method, and how models are compared. Detailed estimators belong in the appendix. |
| Results | Tables with estimates and 95% confidence intervals when available; manuscript comparators and paired differences where available; meaningful figures with explanatory captions. Mark missing and pending results explicitly. |
| Conclusions | Explain what was done and learned in everyday language, compare with the principal manuscript experiments, interpret available overlays, and give an explicit recommendation with its reason and next concrete step. |

## Tables and figures

- Separate development CV and external results when combining them would make a table hard to read. Label validation results accurately. Include the primary configurations and relevant controls; preserve complete results in the appendix rather than hiding unsuccessful configurations.
- Use readable names, consistent decimal precision, and estimate plus interval (for example `0.710 [0.640, 0.780]`). Prefer at most five columns per table; split large grids logically. Define abbreviations once. Use percentages together with denominators.
- Bold the highest point estimate per metric and population, including comparators. Identify this as a descriptive ranking. Show paired differences separately; do not turn a rank into a claim of demonstrated superiority. For error metrics, highlight the lowest estimate.
- Compare against the applicable principal manuscript experiment on matching patients, endpoints, score conventions, and estimators. Explain a mismatch instead of calculating an invalid difference. Cross-study values are contextual references, not paired comparisons.
- Use figures that answer a question: discrimination or paired-difference forest plots, justified learning curves, calibration, survival curves, or verified attention overlays. Every figure needs an explanation of what it shows and why it matters. Reuse relevant existing figures; avoid decorative or redundant plots.
- If attention exists, include verified WSI overlays and, when informative, matched low/high risk cases or cross-model views of the same slides. State case-selection criteria, model/fold or ensemble, color scale, ROI, and patch alignment. Show representative high-attention patches when available. Attention indicates model weighting; it does not establish tissue identity or a causal mechanism. Distinguish visual hypotheses from pathologist-confirmed findings. If this model has no attention output, say so and do not substitute another model's map.

## Conclusions and recommendations

Explain the input, the change being tested, and its practical result as if addressing a non-expert. Answer the objective directly, with numbers from the tables. Distinguish ranking patients, separating risk groups, and predicting an individual's survival probability. Explain material uncertainty plainly without drowning the reader in caveats.

End with one recommendation: **Continue**, **Run a targeted check**, or **Do not invest further in this configuration**. Give the evidence, the unresolved question (if any), and one concrete next step. A disappointing result alone does not prove that the data are the cause. A positive result alone does not establish clinical usefulness.

## Deliverables and checks

Produce Markdown report files only. Include status and date below the title. The appendix contains the full technical protocol, secondary tables, artifact/source paths, source hashes when available, and reproducibility details. Keep credentials and identifiable patient information out of reports.

Before delivery, reconcile counts and key estimates against saved sources; verify bolding and paired-difference direction; check that prose does not imply completion of pending experiments; inspect Markdown structure and image links; and confirm the original inputs were not changed. For a brief status reply, apply the same clarity and comparison principles without regenerating files automatically.

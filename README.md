# better-report

A reusable Codex skill for clear scientific experiment reports in Markdown. It connects the research question to the evidence, compares results with established benchmarks, and ends with a plain-language recommendation and a concrete next step.

Reports are written in **English unless another language is explicitly requested**. The skill produces **Markdown report files only**. PDF conversion requires a separate explicit request.

## What a report contains

1. **Experiment name** — the report title, with completion status and date.
2. **Objective** — the question being tested.
3. **Why this experiment** — why the idea could help and where it came from.
4. **Available data** — relevant populations, inputs, eligibility and missingness.
5. **Splits** — training, validation and external evaluation roles.
6. **Evaluation metrics** — what each metric measures and how uncertainty is assessed.
7. **Results** — readable tables, confidence intervals when available, benchmark comparisons and relevant figures.
8. **Conclusions** — an explanation for a non-expert, followed by a recommendation, its reason and the next step.
9. **Appendix** — complete secondary results, settings, statistical details and reproducibility information.

The main body stays readable, with the most useful tables. Remaining technical details belong in the appendix. The skill distinguishes the highest observed score from evidence of a model improvement, and includes attention overlays when those outputs are available and verified.

## Install

Clone the repository and copy the skill files into your Codex skills directory:

```bash
git clone https://github.com/PierpaoloV/better-report.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills/better-report"
cp better-report/SKILL.md "${CODEX_HOME:-$HOME/.codex}/skills/better-report/"
cp -R better-report/agents better-report/assets better-report/references "${CODEX_HOME:-$HOME/.codex}/skills/better-report/"
```

The package consists of instructions, a template and a conditional survival-reporting reference; it has no required Python dependencies. Its metadata enables normal automatic skill selection, and it can also be invoked explicitly as `$better-report`.

## Example use case

You have finished a benchmark comparing a linear classifier with boosted trees. Saved files contain validation metrics, independent-test metrics and paired bootstrap comparisons. You want a report that explains whether the added complexity helped, without turning a slightly higher point estimate into a claim of superiority.

Example prompt:

```text
Use $better-report to write an English Markdown report for the completed
classifier benchmark. Read the saved metric and comparison files in the
experiment directory. Compare with the established linear baseline, put the
key tables in the main body, and put technical details in the appendix.
Explain the findings for a non-expert and give a recommendation and next step.
Treat data, splits, checkpoints and training code as read-only.
```

See [the synthetic example report](examples/synthetic-report.md) for the intended format. **Its task, sample counts, metrics and intervals are entirely fictional and illustrate presentation only.** They were not computed from an experiment or taken from a research project.

For your own task, supply the relevant saved artifacts and baseline references. The skill reports available evidence; it does not fit models or fabricate missing results.

## Package contents

| File | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Invocation guidance, workflow and reporting requirements |
| [agents/openai.yaml](agents/openai.yaml) | Skill UI metadata and invocation policy |
| [assets/report-template.md](assets/report-template.md) | Starting structure for an experiment report |
| [references/survival-reporting.md](references/survival-reporting.md) | Additional checks for censoring, survival metrics and risk groups |
| [examples/synthetic-report.md](examples/synthetic-report.md) | Fictional example showing the report format |

## Scope

Report creation treats source data, splits, features, checkpoints, training code and other agents' work as read-only. It does not authorize new training, changes to labels or endpoints, publication, or external messages. Figures and attention outputs should be attributed to the actual experiment and interpreted within their limits.

This repository contains generic reporting instructions and a synthetic example. It contains no real research data, trained models, experiment results, project reports, patient records, or credentials.

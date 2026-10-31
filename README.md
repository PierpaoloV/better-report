# better-report

A general-purpose skill for reporting completed or partial work with clear conclusions, proportionate context, and evidence the reader can assess. It supports task summaries, comparisons, findings, and revisions to existing reports across domains.

## What changes in this branch

- Make priorities explicit: accuracy and consequential limits, the requested answer, sufficient evidence, then brevity and presentation.
- Check the scope and version of evidence before combining it; distinguish observations, descriptive calculations, interpretations, and proposals.
- Report supported partial results when missing or conflicting evidence blocks a conclusion.
- Distinguish completed execution from verified outcomes and update superseded recommendations throughout a report.
- Keep ordinary explanations and simple acknowledgements outside formal reporting.
- Separate specialist methodological notes from the installed general skill.
- Add fictional examples and behavioral evaluation cases with a separate grading rubric.

These instructions guide an agent; they are not an automatic factual or methodological validator.

## When to use it

| Request | Expected behavior |
| --- | --- |
| "Summarize what you did and found." | Apply the reporting workflow at the appropriate depth. |
| "Update this report using the revised results." | Integrate new evidence and revise affected conclusions. |
| "Compare these options and report the findings." | Keep the alternatives and conditions needed for the decision. |
| "What is cross-validation?" | Give an ordinary explanation; the topic alone is not a reporting trigger. |
| "Are you done?" | Give a direct status answer; do not force a report structure. |

Explicit invocation remains `$better-report`. Automatic selection remains enabled, subject to the host's skill routing. General instructions do not certify specialist analyses: use the task's methodological requirements, project conventions, and relevant specialist skills.

## Examples

The installed skill links to [short reporting examples](references/reporting-examples.md) for brief tasks, incomplete evidence, changed recommendations, and conflicting counts.

The longer [classifier report](examples/synthetic-report.md) and [venue comparison](examples/synthetic-research-report.md) illustrate presentation. All examples are fictional; they are not measurements of model behavior.

## Install or test a branch in Codex CLI

Check out the revision you want before copying. The package has no runtime Python dependency or bundled report-generation program.

Bash:

```bash
git clone https://github.com/PierpaoloV/better-report.git
cd better-report
git switch general-reporting-evidence-tests
dest="${CODEX_HOME:-$HOME/.codex}/skills/better-report"
mkdir -p "$dest/agents" "$dest/assets" "$dest/references"
cp SKILL.md "$dest/"
cp agents/openai.yaml "$dest/agents/"
cp assets/report-template.md "$dest/assets/"
cp references/reporting-examples.md "$dest/references/"
```

PowerShell:

```powershell
git clone https://github.com/PierpaoloV/better-report.git
Set-Location better-report
git switch general-reporting-evidence-tests
$codexBase = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
$skillDest = Join-Path $codexBase 'skills/better-report'
New-Item -ItemType Directory -Force -Path $skillDest, "$skillDest/agents", "$skillDest/assets", "$skillDest/references" | Out-Null
Copy-Item -LiteralPath SKILL.md -Destination $skillDest
Copy-Item -LiteralPath agents/openai.yaml -Destination "$skillDest/agents/"
Copy-Item -LiteralPath assets/report-template.md -Destination "$skillDest/assets/"
Copy-Item -LiteralPath references/reporting-examples.md -Destination "$skillDest/references/"
```

For an existing installation, inspect its contents first. These commands replace the listed files but do not remove unrelated or obsolete files. Legacy specialist files left from an earlier installation are no longer referenced by the skill.

These commands target Codex CLI. Other hosts may have their own installation mechanism.

## Package and repository layout

| Location | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | General reporting workflow and activation boundaries |
| [agents/openai.yaml](agents/openai.yaml) | Codex interface metadata |
| [assets/report-template.md](assets/report-template.md) | Optional substantial-report template |
| [references/reporting-examples.md](references/reporting-examples.md) | Installed examples of different report scopes |
| [examples/](examples/) | Longer fictional illustrations |
| [evaluations/](evaluations/) | Maintainer-only requests and separate grading criteria |
| [archive/](archive/) | Historical specialist notes; not installed or automatically invoked |

## Validation

Use [the evaluation procedure](evaluations/README.md) to run each request in a fresh session and grade the actual output. Keep evaluator criteria out of the reporting agent's context. Check factual behavior rather than exact phrasing. Compare the same cases with and without the skill before claiming an improvement.

Run `python evaluations/check_structure.py` for package links, metadata, and evaluation-fixture integrity. This static check does not run a model or prove reporting quality. PyYAML is needed only for this maintainer check.

See [the recorded smoke run](evaluations/results/2026-10-31.md) for the cases actually executed and their limits.

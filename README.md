# better-report

A reusable skill for reporting the results of a task clearly, with enough project context to understand why they matter and enough detail to understand what was done. It supports research, analyses, experiments, software work and other completed or partial tasks.

## One report, the right level of detail

Think of the project as a tree: the root is the problem, branches are areas of work, and leaves are findings or outputs. A project update shows branch headlines. After a specific task, the report briefly orients the reader and then explains the work just completed.

The overview and useful detail arrive **together, in one delivery**. The reader does not have to ask for each level or click through a tree. An actual diagram is optional. Limits that change the conclusion stay visible in the summary.

The skill leads with the result, explains the decisive actions and their evidence, and keeps detail proportional to the request. The body contains what the reader needs to understand and judge the work; detailed settings and secondary results belong in supporting material. Existing figures are optional and must add understanding. When further action is useful, the report closes in prose with what to do, why now and what it enables. A completed task may need no next step, and fixed section headings are not mandatory.

Use the requested language, format and destination, or the project's established convention. Otherwise use the user's language. Task wrap-ups can stay in chat; requested report files default to Markdown when no format is specified. Other requested formats use the appropriate available tools.

## Examples

- [New classifier in an existing project](examples/synthetic-report.md): a shared-data overview, three approaches, and the details behind a new 91% result.
- [Venue research](examples/synthetic-research-report.md): a concise comparison that distinguishes a candidate from a confirmed booking option.

**Both examples are entirely fictional.** They illustrate presentation, not executed work or evaluated model behavior.

Example prompt after completing a task:

```text
Use $better-report to report what you just completed. Show where it fits in
the project, then explain the work, results and evidence in the same report.
Keep other branches at headline level and include the limits that matter.
```

## Install or test a branch

Clone the repository, check out the revision you want to use, and copy the skill files into your Codex skills directory. To test a review branch, select that branch before copying.

```bash
git clone https://github.com/PierpaoloV/better-report.git
cd better-report
# To test a branch: git switch <branch-name>
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills/better-report"
cp SKILL.md "${CODEX_HOME:-$HOME/.codex}/skills/better-report/"
cp -R agents assets references "${CODEX_HOME:-$HOME/.codex}/skills/better-report/"
```

Normal automatic skill selection remains enabled; explicit invocation is `$better-report`. The package contains instructions and examples, with no required Python dependencies or bundled report-generation program.

## Package contents

| File | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | General reporting instructions and evidence checks |
| [agents/openai.yaml](agents/openai.yaml) | Skill UI metadata and invocation policy |
| [assets/report-template.md](assets/report-template.md) | Flexible starting point for a substantial report |
| [references/experiment-reporting.md](references/experiment-reporting.md) | Scientific methods, comparisons and provenance |
| [references/survival-reporting.md](references/survival-reporting.md) | Additional checks for censoring, survival metrics and risk groups |
| [examples/synthetic-report.md](examples/synthetic-report.md) | Fictional experiment report |
| [examples/synthetic-research-report.md](examples/synthetic-research-report.md) | Fictional research report |

Reporting does not expand the underlying task's authorization. The skill preserves the actual evidence, distinguishes missing or unverified results, and does not authorize new experiments or external actions by itself. Domain-specific checks remain conditional so that scientific reporting retains its methodological safeguards.

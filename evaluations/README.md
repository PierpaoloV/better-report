# Behavioral evaluations

These fictional fixtures exercise reporting behavior across data processing, software delivery, comparisons, procurement, and brief communication. They are maintainer material, not installed skill instructions.

## Run without leaking the grading criteria

1. Pin the skill revision, model identifier, host, date, and generation settings that are available.
2. For each case, start a fresh session with only the installed skill package and that case's request. Do not expose this directory, the rubric, other outputs, or the expected diagnosis. Copy the skill's four installed files and the single request to an isolated directory when using a filesystem agent.
3. Run the request normally. Save the unedited answer and tool activity, including whether the skill was actually loaded. Do not let the reporting agent read the rubric.
4. After the run, grade each criterion in [rubric.json](rubric.json) as pass, fail, or unassessable. Include a short quotation or observation supporting each judgment. A case passes only if every applicable criterion passes. Unassessable criteria are not passes.
5. Repeat with fresh sessions to examine variability. For a with/without comparison, use the same inputs, model, host settings, and tools; omit only the skill in the control condition. Report both benefits and regressions.

The first six cases test output behavior with explicit invocation. The last two test implicit routing only when the host exposes normal skill selection and evidence of activation. Manually loading the skill and obtaining a brief answer does not establish correct routing.

Judge factual properties and requested constraints, not exact wording or a preferred writing style. Concise answers are acceptable when they preserve the essential evidence and limits. Do not require a table except where the requested artifact requires one.

## Coverage

| Case | Behavior |
| --- | --- |
| count-conflict | Preserve unresolved discrepancies without inventing exclusions |
| execution | Distinguish a successful process from verified delivery readiness |
| comparison | Calculate a descriptive difference without inventing reliable superiority |
| update | Propagate superseding evidence through the complete report |
| brief | Respect one-sentence scope without formal-report overhead |
| mismatched-samples | Keep a decisive comparison limitation under a strict length constraint |
| ordinary-explanation | Avoid topic-based reporting activation |
| simple-status | Avoid formal reporting for a simple acknowledgement |

Run `python evaluations/check_structure.py` from the repository root for static integrity. This checks package metadata, local Markdown link targets, and one-to-one case/rubric coverage. It does not grade generated reports or test skill routing.

The suite is deliberately small. Passing it does not prove general reliability or superiority over a baseline. Record only executed cases in results; distinguish unrun, unassessable, and failed cases.

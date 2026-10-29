---
name: better-report
description: Report the results of completed or partial tasks with a concise project overview, a clear account of the work performed, and supporting evidence. Use for task wrap-ups, research findings, analyses, experiment reports, and updates to existing reports, or when explicitly invoked. Adapt the depth to the request; ordinary conversation does not need a formal report.
---

# Better report

Let the reader understand the result at a glance and the work behind it in the same delivery. Every sentence should help them understand, assess, or use the result.

## Show the project at the right scale

Think of a project as a tree: the root is the problem, branches are areas of work or approaches, and leaves are concrete findings or outputs. Use this to organize information; draw a tree only when it helps.

- For a project overview, show the objective, the relevant branches, and their result or status headlines.
- After a specific task, briefly locate the work in the project, update the relevant comparison or status, then explain that task in enough detail to understand what happened.
- For a focused question, concentrate on that branch or result and include only the context needed to interpret it. A small standalone task may need just a few sentences.

Deliver the useful overview and task detail together. Do not make the reader ask follow-up questions or open interactive nodes to learn what was done. Keep limitations that change the headline in the opening; explain other material limits alongside the result or in a short limits paragraph. Keep shared facts and numbers consistent across levels; refer back to shared inputs rather than duplicating their description.

## Write the report

1. Read the request and available evidence: the work just performed, saved outputs, relevant project context, and existing reports. Identify the goal, the affected branch, and what changed. Use the context available; do not invent missing branches or start a project-wide audit to fill a template.
2. Lead with the main result and its meaning for the goal. Distinguish work completed, checks performed, and outcomes established. A completed investigation may still have an inconclusive answer.
3. Orient the reader with a short paragraph, list, or comparison table. Keep other branches at headline level unless they affect the result. Distinguish prior results from the work just completed, and label unavailable or outdated information when it matters.
4. Explain the decisive work: the question addressed, why the approach was chosen, relevant inputs and their transformations, method or changes, checks actually performed, and findings. Keep what the reader needs to understand and judge the focal task in the body. Put implementation settings, full reproducibility details and secondary results in linked methods or supporting material. Keep relevant alternatives in the body when comparison is the task. A status report can focus on the selected approach, but must retain a decisive comparator when it explains that choice or changes the interpretation.
5. State what the evidence supports and any limitation that changes the conclusion. When further action serves the task, close the main report with a short prose paragraph explaining what to do, why now and what it would resolve or enable. Ground the priority in the evidence; do not invent effort estimates or declare other work deferrable without a basis. Completed work may need no further action.

Use [report-template.md](assets/report-template.md) as a flexible starting point for a substantial report. Combine or omit sections that add nothing; honor the user's requested structure. Brevity comes from selecting relevant information, not withholding the explanation or stripping out essential methods.

Write about the project, not the mechanics of producing its report. Remove editorial assurances such as "not silently combined here", "not newly certified here" or narration of replacing outdated entries. Express consequential gaps as project facts and explain their effect: "The review and prediction export contain different counts, so the review denominator remains unresolved." Distinguish saved results from new work when that distinction affects interpretation or was requested; keep routine reporting provenance in supporting material. Use language familiar to the intended audience, with counts and denominators where clearer than abbreviations. Define a term in the body only when necessary to understand the result; put other definitions in supporting material or omit them.

Removing reporting commentary must not remove substantive inconsistencies. Keep contradictions, comparisons and uncertainties in the main report when they change a conclusion, require a correction or condition a decision. Explain their consequence and the action needed, without presenting that action as completed. Distinguish a documented error from a question that still needs checking; preserve the relevant evidence even when the detailed audit belongs in an appendix.

## Keep claims grounded

- Connect decisive claims to the relevant file, source, observation, or check. For derived numbers, give the denominator, units, or calculation needed to interpret them. Link evidence near the claim when practical; reserve long provenance lists for an appendix.
- Make observations, calculations, interpretations, assumptions, and proposals distinguishable in ordinary prose. Never invent a missing method, result, source, or verification. Absence from the searched material is not proof of absence everywhere.
- Compare like with like: matching populations, time periods, definitions, or test conditions as applicable. Explain mismatches. Report uncertainty when available; a higher score alone does not establish a reliable improvement. For changing external information, identify the relevant date or version.
- Match the verification to the work. Research needs relevant sources, search scope and material disagreements; quantitative analysis needs traceable inputs and calculations; software work needs the changed behavior and checks actually run. Preserve failed or inconclusive findings that affect the answer.

Reporting does not expand the authorized task. Read source artifacts without rewriting them merely to produce a report. Checking a total or a link can be part of reporting; new experiments, model fitting, publication, or deployment require authorization from the underlying task. Respect authorization already given. Exclude credentials and identifiable patient information.

## Presentation and delivery

Use the requested language, format, and destination, or an established project convention. Otherwise follow the user's language. A normal task wrap-up can stay in chat; create or update a report file when requested or established by the workflow. Default to Markdown when a file is needed and no format was specified; use appropriate tools for other requested formats.

Use tables for genuine comparisons. Give each overview row a concrete result or status, including its decisive number when available; avoid replacing the headline with "see below". Reuse an existing, relevant figure when it explains the focal result more efficiently than prose or a table; availability alone is not a reason to include it. Omit it when redundant or unverifiable, unless resolving its absence is part of the task. Give numbers consistent precision, readable labels, units and denominators. Explain what a figure establishes, identify the plotted groups and map any differing labels to the report's terminology. Highlight a best value only when meaningful and identify descriptive rankings as such. Avoid repeating the same result in every section.

When updating a report, preserve valid context, integrate new evidence, and make consequential changes clear. Use an existing destination when appropriate; a new dated directory is optional. Include a date, status, and supporting appendix when they help interpret the report. Link any delivered files.

Before delivery, check the main conclusion against its evidence, reconcile key counts and comparisons, check links, and ensure completed actions are not confused with proposed or unverified ones. Remove text that does not help the reader understand, assess, or use the result.

## Scientific experiments

For scientific experiments, read [experiment-reporting.md](references/experiment-reporting.md). For survival analyses, also read [survival-reporting.md](references/survival-reporting.md). Apply their methodological checks within the same concise overview-plus-detail report.

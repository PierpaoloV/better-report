# Reporting at different scales

All scenarios below are fictional illustrations, not executed work. Adapt their logic rather than copying a fixed format.

## Brief completed task

Request: "What changed? Keep it brief."

Evidence: Three links were replaced. The supplied check output confirms that all three resolve to their intended pages.

Report: "The three links now point to the intended pages, and the recorded link checks passed."

If the evidence records only edits, report the edits; do not add successful checks. A project overview or next step adds nothing here.

## Inconclusive comparison

Request: "Which supplier is cheaper?"

Evidence: A quotes EUR 900 including support. B quotes EUR 850, with mandatory support priced separately but no support amount supplied. Both prices cover the same period and tax treatment.

Report: "The supplied quotes do not establish which supplier is cheaper overall. A costs EUR 900 including support; B starts at EUR 850 but excludes mandatory support. B is cheaper only if that support costs less than EUR 50."

The EUR 50 threshold is a descriptive calculation, not a discovered support price. Obtain B's support price if a purchasing decision is needed.

## Update a recommendation

Request: "Update the recommendation with the revised quote."

Evidence: A prior report recommended B at EUR 900 against a EUR 1,000 budget. A revised quote explicitly replaces that quote and prices the same service at EUR 1,100.

Report: "B now exceeds the EUR 1,000 budget by EUR 100, so the previous recommendation is no longer supported under the current budget."

Update the summary, price table, and recommendation together. Do not claim another option is suitable without evidence about it.

## Execution versus validation

Request: "Is the export ready?"

Evidence: The log records a successful export. The output has not been inspected and the required acceptance check is absent.

Report: "The log records a completed export, but readiness remains unverified because the required acceptance check is unavailable."

Do not upgrade a successful exit code into verified completeness or correct contents.

## Conflicting counts

Request: "Summarize completion."

Evidence: A note says 120 items were processed; an output manifest lists 118. Both refer to the same run. No exclusion or failure record is supplied.

Report: "The manifest contains 118 items, while the run note reports 120 processed. Completion against the reported 120 items is unresolved; the supplied records do not explain the two-item difference."

Do not invent two exclusions or describe the process as completely successful.

## Different evaluation conditions

Request: "Did B improve on A?"

Evidence: A scored 88% on one sample; B scored 91% on a different sample.

Report: "B scored 91% versus A's 88%, but the samples differ, so these results do not isolate an improvement from changing the method."

Preserve that qualification even in a one-sentence answer. Detailed sample definitions can follow when needed.

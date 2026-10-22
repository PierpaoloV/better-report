# Routing support tickets to the right department

**Fictional illustration: all inputs, actions, settings and results below are invented. No experiment was run and no source artifacts exist.**

**The new classifier reaches 91% accuracy: 60 fewer errors than the previous classifier on the same 2,000 historical test tickets. Its advantage has not yet been quantified with an uncertainty interval or checked in live use.**

The project aims to route incoming requests to the correct department. The shared data branch contains 12,000 usable tickets after deduplication. The approaches now compare as follows:

| Approach | Correct assignments | Errors |
| --- | --- | --- |
| Keyword rules | 76% | 480 |
| Classifier A — logistic regression | 88% | 240 |
| **Classifier B — linear SVM, new** | **91%** | **180** |

Bold marks the highest observed accuracy, a descriptive ranking.

## Work performed

The new experiment tests whether changing the classifier improves routing while keeping the data and text representation fixed. A linear SVM provides a different decision rule over the same text features, making the classifier the intended change.

| Element | Procedure in this fictional scenario |
| --- | --- |
| Shared data | 14,000 records reduced to 12,000 unique tickets by ID, retaining the latest record. |
| Inputs and targets | Subject and initial request concatenated; operator replies and assigned-department fields excluded from inputs. Target categories: payments, access, deliveries and cancellations. |
| Shared split | By opening date: first 8,000 tickets for training, next 2,000 for validation, final 2,000 for test. One record per ticket. |
| Shared transformation | Lowercase text; TF-IDF on single words and word pairs, fitted only on the training set and reused for both classifiers. |
| New configuration | Linear SVM with C = 1, fixed before evaluation; no hyperparameter search in this experiment. |
| Evaluation | Frozen models evaluated on the same 2,000 test tickets. Accuracy is the number routed correctly divided by 2,000. B: 1,820 correct; A: 1,760; rules: 1,520. |

## Meaning and limits

The new model gains **3 percentage points** over classifier A. Errors fall from 240 to 180: **60 fewer, a 25% relative reduction**. This is the strongest observed result among the three approaches on this test.

Validation-set results, category-level errors and paired uncertainty estimates are unavailable in the example. The historical comparison does not establish reliability in live use. Examining which departments gain or lose accuracy would help assess whether a pilot is justified.

No real datasets, model artifacts or source files underpin this illustration. In a real report, the metric and protocol artifacts would be linked next to the relevant results or in supporting material.

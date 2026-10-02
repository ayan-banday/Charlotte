---
date created: 2026-10-02
date updated: 2026-10-02
status: draft
---

# Agency Promise Loop: Prototype Project Documentation

## Project purpose

This project builds a prototype that tests one claim: an agency can improve its own marketing by comparing what that marketing promises with what is said on sales calls and which deals were won or lost.

The prototype takes sales call transcripts, CRM outcomes, and current marketing material. It extracts the promises made, compares them with outcomes, and drafts the next round of marketing material for human approval.

---

## 1. Background

**The promise is the central object.**

- **Marketing:** an ad, page, or outbound message promises a result.
- **Sales call:** the rep restates or bends that promise, adding timelines, guarantees, scope, and price.
- **Proposal:** the promise is written into a contract.
- **Delivery:** the client judges the work against what they believe they bought.
- **Renewal:** the client stays, expands, or leaves.

**Two outcomes the full product serves.**

- **More clients through the door:** promises that attract and convert the right buyers.
- **Higher client LTV:** promises that get kept and proven.

**Why the prototype starts with the acquisition loop.**

- **Data exists on day one.** Recorded calls and a deal list already sit in the agency's tools.
- **Feedback is fast.** New messaging shows up in reply, booking, and win rates within weeks.
- **LTV needs months.** Renewal and tenure data would leave nothing to demonstrate in a first prototype.

**Target agencies.**

- **Size:** more than 5 and fewer than 20 people, anywhere in the world.
- **Stack [Hypothesis]:** these agencies avoid HubSpot because of cost. They more likely use tools such as Pipedrive, GoHighLevel, Close, or spreadsheets, and record calls with tools such as Fathom, Fireflies, Zoom, or Meet. This needs confirmation in M1.

**Later stages, outside this prototype.**

- **Promise ledger:** promises extracted from calls follow the client into onboarding and delivery, and drift is flagged.
- **Retention loop:** monthly proof-of-value briefs, churn-risk flags, and expansion triggers.
- **Full loop:** case studies and referrals feed back into marketing, and guidance on what to say on sales calls is added.

---

## 2. Problem Statement

**What happens today.**

- **[Hypothesis]** Small agencies market themselves from intuition. What buyers respond to on sales calls rarely reaches the next piece of marketing material.
- **[Hypothesis]** Marketing claims, call promises, and deal outcomes sit in separate places, so nobody can see which promises win deals and which lose them.
- **[Fact]** Preliminary conversations with two operators in the target market indicated that a related problem exists. The specific workflow, its cost, and the buyer are not yet validated.

**Why it persists.**

- **Time:** nobody has the hours to reread transcripts and compare them with marketing material.
- **Tool fit [Inference]:** established revenue and conversation intelligence products target larger teams and mostly stop at call summaries, coaching, and reporting.
- **Substitute:** a team member can paste transcripts into a general-purpose AI tool. The prototype has to beat that baseline.

**The intended change.**

- An agency can see which promises win and lose deals, which of its marketing claims never appear in winning calls, and receives cited drafts for the next round that it approves before use.

### Who is affected

| Group | Relationship to the project |
|---|---|
| Agency founder or owner | Primary customer. Decides what the agency promises and whether to adopt the tool. |
| Sales lead or closer | Source of call evidence. Makes the promises on live calls. |
| Marketer or content owner | Receives drafts, edits them, and approves them. |
| Prospects and buyers | Their words and reactions are the evidence the system learns from. |
| Engineer co-founder | Builds the prototype from this document. |
| Project owner and advisors | Review milestones and decide whether to continue, adjust, or stop. |

---

## 3. Work Breakdown & Milestones

Each milestone has defined tasks, an output, and an exit criterion so that progress can be reviewed objectively.

### Milestone 1: Problem and pilot confirmation

**Tasks**

- Confirm the problem with three agencies of 5 to 20 people.
- Confirm who owns marketing and who runs sales calls at each agency.
- Confirm that each agency records calls and keeps a CRM or deal list.
- Confirm each agency's permission to share data.

**Output:** Locked problem statement and pilot agency list.

**Exit criterion:** A reader outside the team can identify who has the problem, what happens today, why it persists, and the intended change.

### Milestone 2: Data intake

**Tasks**

- Collect call transcripts, deal exports with won or lost status, deal value, and lead source, and the current marketing material.
- Define the minimum data format.
- Mask personal and client-confidential details.
- Record recording-consent status for each source.

**Output:** Intake format sheet and a loaded data set for each pilot.

**Exit criterion:** At least 20 outcome-labelled calls per pilot, or the shortfall is recorded and that pilot is treated as exploratory.

### Milestone 3: Promise extraction

**Tasks**

- Define promise types: outcome, timeline, price, scope, and guarantee.
- Extract promises, objections, and buyer language from each call, each with an exact quote and call reference.
- Hand-label 5 calls to measure extraction accuracy.

**Output:** Register of promises, objections, and buyer language with quotes, plus an accuracy record.

**Exit criterion:** The team can state how many hand-labelled promises were found and what was missed, and every extracted item traces to a quote.

### Milestone 4: Outcome join and marketing comparison

**Tasks**

- Join each call to its won or lost outcome.
- Compare promises and phrases in won calls against lost calls.
- Compare both against the claims in the agency's current marketing material.
- Produce a gap list: marketing claims that never appear in winning calls, and winning phrases that appear nowhere in the marketing.

**Output:** Message gap report for each pilot.

**Exit criterion:** An agency owner can read the report without help and say which gaps they recognize and which they dispute.

### Milestone 5: Draft generation and human approval

**Tasks**

- Generate three drafts of next-round marketing material per pilot from the gap report.
- Attach the source call excerpts to each draft.
- Provide an approval step with accept, edit, and reject.
- Record every edit.

**Output:** Approved drafts with citations and an edit record.

**Exit criterion:** Every draft traces to call excerpts, and nothing client-facing is used without human approval.

### Milestone 6: Ledger and round two

**Tasks**

- Log each hypothesis, what shipped, and the result.
- Ship approved drafts through each pilot's normal channels.
- Collect results over an agreed window: reply, booking, and win rates.
- Run a second round that starts from the ledger.

**Output:** Ledger and round-two drafts.

**Exit criterion:** Round two visibly uses what round one taught, and the ledger shows what was tested and what happened.

### Milestone 7: Validation against the baseline

**Tasks**

- Run the same calls and material through a general-purpose AI tool with a plain prompt.
- Compare outputs on accuracy, traceability, and usefulness to the agency.
- Collect feedback from each pilot agency.
- Document limitations, including sample size.

**Output:** Validation memo.

**Exit criterion:** The team can state where the prototype beats, matches, or loses to the baseline, and which claims remain unverified.

### Milestone 8: Handover and next step

**Tasks**

- Assemble the handover package.
- Record privacy and recording-consent findings.
- Recommend the next step: move to the promise-to-delivery stage, run more pilots, or stop.
- Record the evidence behind the recommendation.

**Output:** Final handover package.

**Exit criterion:** The project has a working prototype, supporting records, and a clearly stated next step.

---

## 4. Final Deliverable

### Primary deliverable

A working prototype that takes call transcripts, deal outcomes, and current marketing material, and returns:

- **A promise report:** promises, objections, and buyer language, each with a source quote.
- **A message gap report:** won against lost, and against current marketing claims.
- **Cited drafts:** next-round marketing material with a human approval step.
- **A ledger:** hypotheses, what shipped, and results, so each round starts from the last.

### Supporting handover package

1. Locked problem statement and stakeholder summary.
2. Requirements sheet, with each requirement marked as confirmed, requiring further research, or requiring validation.
3. Data intake format and the loaded pilot data sets.
4. Extraction accuracy record.
5. Sample gap reports and approved drafts from each pilot.
6. Ledger covering round one and round two.
7. Validation memo comparing the prototype with the general-purpose AI baseline.
8. Privacy and recording-consent notes.
9. Recommended next step with supporting evidence.



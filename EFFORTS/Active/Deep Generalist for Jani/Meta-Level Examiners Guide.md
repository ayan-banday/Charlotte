---
date created: 2026-04-29
date updated: 2026-04-29
---
# Meta Examiner's Guide — HHU Düsseldorf

## Behavioral Specification of the Gold Standard Medical Student

**Version:** 1.0 **Institution:** Heinrich-Heine-Universität Düsseldorf (HHU), Düsseldorf Curriculum of Medicine (DCM) **Scope:** Semester 8 through Approbation (Q2 + Q3) **Primary Reader:** AI systems generating subject-level and topic-level Examiner's Guides within this project. **Secondary Reader:** Any human coach or student who wants to understand what perfect looks like. **Last Updated:** 2026-04-29

---

## The One-Sentence Definition

The perfect HHU student, in every room from a block exam to the M3 commission, does one thing consistently: they reason from the patient's actual problem to the safest correct decision, out loud, without prompting, and without breaking when they hit uncertainty.

Everything in this document is an unpacking of that sentence.

---

## Why This Document Exists

Every subject-level and topic-level Examiner's Guide built within this system must answer the same question: what does this examiner reward, and what does this examiner punish? Without a meta-level model of what HHU is actually trying to produce, each subject guide risks optimising for the wrong thing. A subject guide that treats the Abdomen Block as a fact-recall exercise will produce different questions than one that treats it as a clinical decision-making exercise. This document tells the AI which one it is, what HHU's assessment system actually measures, and what behaviors separate a student who passes from one the examiners remember.

This document does not tell Jani how to study. It tells the AI how to think when building the tools Jani will use.

---

## Objective 1: The Arena Map

### What This Section Does

Maps every formal and informal arena in which Jani is judged from Semester 8 to Approbation. For each arena: the exact format and stakes, what the assessor is actually scoring, what gold standard behavior looks like in specific behavioral terms, what almost-gold behavior looks like and exactly where it breaks, and what the trap is for a smart student who half-knows the material.

---

### Arena 1: Block Final Exams (Blockabschlussklausuren)

**Format and Stakes**

Written exam at the end of each Studienblock. Format: MCQ (5 options, 1 correct, 1 point each) + Multiple-Select (4 options each judged true/false: full point if all 4 correct, 0.5 if exactly one error, 0 if two or more errors). Newer digital formats rolling out from 2025/26: Key-Feature (multi-step clinical decision sequence), Hotspot (click on correct region of an image), ROI/Region of Interest (mark area on scan or diagram), Interval questions (numerical answer with tolerance range), Long Menu (select from a large dropdown list). Students are notified of which digital formats appear at least 2 weeks before the exam. Time budget: 1.5 minutes per question. Pass threshold: 60% of total points AND 60% in every individual subject represented in the block. Resit: up to 3 total attempts. Attendance precondition: 85% of mandatory Lehrveranstaltungen attended, or the student is not admitted.

**What the Assessor Is Actually Scoring**

The examiner is scoring whether the student can take a clinical presentation, identify the most relevant finding, and select the most appropriate next action. Not the most technically comprehensive action. Not the action with the most supporting textbook evidence. The most appropriate action given the clinical context in the question. The dominant framing is: patient walks in, here is what you observe, what do you do next?

**Gold Standard Behavior**

On a standard MCQ vignette, the gold standard student does the following in sequence:

1. Reads the last sentence of the question first. The last sentence is always the actual question. This prevents the student from reading the stem with the wrong question in mind.
2. Reads the stem and immediately identifies: who is this patient (age, sex, relevant comorbidities), what is the primary problem (one sentence), and what is the time frame (acute, subacute, chronic).
3. Before reading the options, commits internally to a most-likely answer or a most-likely next step.
4. Reads the options and immediately eliminates the two that are clearly wrong. Does not linger on them.
5. Between the remaining options, identifies the ONE finding in the stem that discriminates between them. Not the most impressive finding. The discriminating one.
6. Selects the option the discriminating finding points to.

On a Multiple-Select question, the gold standard student treats each of the 4 options as an independent true/false statement and evaluates them one at a time without letting their answer on one option influence their answer on the next. They know that a single error costs them 0.5 points and two errors cost the full point.

On a Key-Feature question, the gold standard student recognizes that each sub-question in the sequence is asking about a critical decision node, not a detail. They do not overthink. They answer with the most clinically defensible choice at each node and move on.

On a negative-stem question ("Which of the following is NOT correct?"), the gold standard student rewrites the question as a positive statement before evaluating options. Instead of scanning for the wrong one, they confirm the four correct ones and the remaining option is the answer.

**Almost-Gold Behavior and the Exact Breaking Point**

The almost-gold student knows the material. They read the vignette carefully, they know the diagnosis, and they understand the treatment options. The breaking point is this: they select the most correct answer rather than the most appropriate answer. These are not the same thing in HHU block exams.

Example: A 67-year-old with acute cholangitis. The correct management in the question is urgent ERCP. The almost-gold student selects "IV antibiotics + ERCP within 72 hours" because that is the guideline-compliant, technically correct answer in a stable patient. But the vignette states the patient has a fever of 39.8, bilirubin of 8, and is confused. That is Charcot's triad plus altered consciousness: Tokyo Grade III acute cholangitis. The most appropriate answer is emergency biliary drainage, not "within 72 hours." The almost-gold student knew the guideline but did not read the severity signal in the vignette. They lost the point not because they lacked knowledge but because they did not run the clinical reasoning before selecting the answer.

**The Trap for Smart Students**

The subject-specific 60% threshold. A student who scores 95% in Surgery and Internal Medicine but 57% in Clinical Chemistry fails the entire block exam. The block has 9 subjects. The exam does not compensate between subjects. The trap is that a smart student allocates study time proportional to their interest and confidence, builds huge surpluses in the heavy subjects, and then fails on a lighter subject they de-prioritised. The block exam treats every subject as equally capable of killing you. The subject Examiner's Guide must therefore never describe any subject as safe to under-prepare. It must state the 60% floor explicitly for its subject and flag the minimum viable coverage required to clear it.

---

### Arena 2: Mini-CEX

**Format and Stakes**

Five to ten minutes at the end of a practice module week. The assessor is a physician from the clinical department. HHU's 90+ predefined skills are assessed: the clinics and institutes have identified the most important practical skills in their field, and those skills are tested at least once per practice module. Grading: ungraded Mini-CEX uses "ausgezeichnet erfüllt" / "erfüllt" / "nicht erfüllt." Graded Mini-CEX for the Blockpraktika in Surgery, Internal Medicine, Paediatrics, and Geriatrics use a numerical grade of 1-4 or "nicht erfüllt." The graded Mini-CEX grade becomes the Leistungsnachweis grade for that subject.

**What the Assessor Is Actually Scoring**

Fluency without prompting. The assessor is not scoring whether the student knows the steps. They are scoring whether the student executes the full sequence, in the right order, without being told what to do next. Every prompt the assessor provides is evidence that the student's execution is incomplete.

**Gold Standard Behavior**

The gold standard student, before the Mini-CEX begins, mentally runs the full sequence they are about to perform. They arrive already knowing: step one is this, step two is this, the critical technical detail in step four is this. During execution:

- They announce each step to the patient before doing it: "I am now going to listen to your lungs. Please take some deep breaths."
- They maintain eye contact with the patient during history-taking and with the procedure during technical steps. They do not look at the examiner.
- When they identify a finding, they state it out loud immediately: "There is dullness to percussion at the right base."
- They complete the full sequence without pausing to check whether the examiner is satisfied.
- At the end, without being asked, they state their interpretation: "Based on the findings, I am concerned about a right-sided pleural effusion. My next step would be a chest X-ray."

For the specific behavioral detail that separates gold from excellent in the Subarachnoid Hemorrhage Mini-CEX (representative example of the category):

Gold standard on SAB: Identifies thunderclap headache ("Vernichtungskopfschmerz") as the discriminating symptom immediately. Asks unprompted about nicotine, cocaine, and hypertension as risk factors. Checks vigilance using GCS rather than just asking "are you confused?" Proposes CT first, then LP if CT negative, and specifically warns about traumatic puncture. Applies Hunt and Hess scale (clinical severity), WFNS scale (GCS-based), and Fisher scale (radiological CT findings) fluently and explains which scale informs which decision. Mentions Nimodipine for vasospasm prophylaxis without being asked.

**Almost-Gold Behavior and the Exact Breaking Point**

The almost-gold student knows every step. They execute cleanly. The breaking point is a single prompt. The examiner asks: "And what would you do if the CT is negative?" The student then correctly describes the LP. That prompt drops them from ausgezeichnet to erfüllt. It is the difference between "this student is ready to practice" and "this student needs supervision."

The second breaking point is documentation. The student performs the full physical sequence correctly but does not document the findings appropriately. HHU learning goals explicitly require that students "document these findings appropriately." Failing to document is treated as an incomplete skill execution.

**The Trap for Smart Students**

The sterile glove trap. A student with strong clinical knowledge performs a complex procedure (e.g., lumbar puncture, joint aspiration) with technically correct diagnostic reasoning but breaks aseptic technique during the procedure. HHU tests sterile glove donning as a standalone skill and applies it as a criterion within complex procedures. A single aseptic error in a graded Mini-CEX drops the grade. The trap is that students mentally separate "the knowledge part" from "the technique part" and rehearse the former without drilling the latter.

---

### Arena 3: Patient Presentations (Patientenaufnahmen und -vorstellungen)

**Format and Stakes**

47 total across Q2: 40 documented by end of Year 4 (Ärztliche Kompetenzen 1), 7 more in Year 5 (Ärztliche Kompetenzen 2). Each uses the standardised HHU Dokumentations- und Feedbackbogen. Graded: bestanden (7-14 points) / nicht bestanden (0-6 points). Outstanding performance is flagged at 13-14 points. The presentations are linked to the Düsseldorfer Liste der Behandlungsanlässe: 123 defined treatment occasions, coordinated across all UKD clinics, covering the presentations a physician will encounter at any level of care. The goal is to see as many of the 123 occasions as possible across the 47 presentations.

**What the Assessor Is Actually Scoring**

Whether the student can elicit the patient's own illness narrative without contaminating it, then build a structured clinical picture from that foundation. The assessor is specifically scoring: quality of open questioning, capture of the patient's Krankheitskonzept (their own concept of what is wrong with them), diagnostic reasoning, therapeutic planning, and reflective learning.

**Gold Standard Behavior**

The gold standard patient presentation follows this exact sequence:

Step 1 — Introduction: Full name, role, semester, explicit request for permission to speak with the patient. "Guten Tag, mein Name ist [Name], ich bin Medizinstudent/in im achten Semester. Darf ich mir etwa [X] Minuten Zeit mit Ihnen nehmen?"

Step 2 — Opening: Single open question, then silence. "Was führt Sie heute zu uns?" Then the student stops talking. Minimum 60-90 seconds of uninterrupted patient speech. The student does not prompt, does not redirect, does not ask a follow-up question until the patient has finished their opening account.

Step 3 — Krankheitskonzept: After the patient finishes, the student elicits the patient's own explanatory model. "Was glauben Sie selbst, warum das passiert?" or "Haben Sie eine Idee, was dahinterstecken könnte?" This is not skipped. It is worth points.

Step 4 — Structured history: Onset, character, radiation, severity (numeric scale if applicable), timing, exacerbating factors, relieving factors, associated symptoms. Then: Vorerkrankungen, Medikamente (name, dose, frequency), Allergien, Familienanamnese, Sozialanamnese (occupation, living situation, smoking, alcohol, travel history if relevant).

Step 5 — Diagnostics: States which investigations would be ordered, in what sequence, and what finding would confirm or rule out each differential.

Step 6 — Therapy: States therapeutic options starting from the most conservative, explains the rationale for the proposed plan, mentions contraindications relevant to this specific patient.

Step 7 — Reflection: States explicitly what was learned from this case and what remains open. "Aus diesem Fall nehme ich mit, dass [X]. Offen geblieben ist für mich [Y]."

The presentation then closes with the handover formulation: patient's age, sex, admission date, Behandlungsanlass from the Düsseldorfer Liste, and the key clinical problem in one sentence.

**Almost-Gold Behavior and the Exact Breaking Point**

The almost-gold student has excellent medical knowledge. Their diagnostic reasoning is solid. Their therapeutic plan is correct. The breaking point is in Step 2. They ask the opening question and then, after 15 seconds of patient speech, interrupt with a structured follow-up: "And how long has this been going on?" That interruption closes the patient's narrative. The Krankheitskonzept is never fully elicited because the student has redirected the conversation into their own framework too early. The assessor marks down the "open questioning quality" criterion and the "Krankheitskonzept" criterion. The student loses 2-4 points they do not understand they lost, because their medical content was correct.

**The Trap for Smart Students**

Smart students use medical jargon with patients. "Do you have any dyspnoea?" instead of "Do you get short of breath?" The HHU feedback form explicitly assesses patient-appropriate communication. Using jargon is a graded error. The trap is that a student who has been immersed in medical language for 4 years starts to use it automatically. Gold standard students code-switch fluently between the clinical register (for the examiner) and plain language (for the patient).

---

### Arena 4: Evidenzbasierte Patientenberichte

**Format and Stakes**

Written case reports required for the Blockpraktika in Frauenheilkunde and Geriatrie. Graded 1-4 or "nicht erfüllt." The grade goes to the Leistungsnachweis for those subjects.

**What the Assessor Is Actually Scoring**

Whether the student can construct a written clinical argument, not a written clinical summary. The distinction: a summary lists what happened. An argument explains why each decision was made, in this patient, given this evidence.

**Gold Standard Behavior**

The gold standard Evidenzbasierter Patientenbericht has the following structure:

- Anamnese: Clear, concise, patient-specific. Not a textbook presentation of the disease. The patient's actual history with the relevant details that drove the diagnostic decisions.
- Befunde: Physical exam findings stated with precision. Not "lymph nodes palpable" but "right submandibular lymph node, approximately 2cm, firm, non-tender, fixed."
- Diagnose: Primary diagnosis stated with the ICD code. Differential diagnoses listed with the specific finding that was used to exclude each one.
- Prognose: Not "good" or "poor." A prognosis anchored in the patient's specific comorbidities, age, and biometric data. "Given the patient's age (72), preserved performance status (ECOG 1), and absence of distant metastases, prognosis for this stage is [X] with [Y] treatment."
- Therapieplan: Treatment options listed with evidence base cited. The chosen plan justified against the alternatives, including why the alternatives were not selected for this patient.
- Epikrise: The clinical argument. A coherent narrative that links the patient's initial presentation, the diagnostic pathway taken, the treatment decision, and the anticipated outcome. Every statement in the epicrisis is traceable to a specific finding documented earlier in the report. The epicrisis does not introduce new information. It synthesises what was already documented into a clinical argument.

**The Trap for Smart Students**

The epicrisis trap: the almost-gold student writes an epicrisis that repeats the findings in prose form. "The patient presented with [X], was diagnosed with [Y], and is being treated with [Z]." That is a summary. The gold standard epicrisis says: "The patient's presentation of [X], combined with the finding of [discriminating finding], confirmed [Y] and ruled out [differential]. The decision to treat with [Z] rather than [alternative] was driven by [patient-specific factor], which is supported by [evidence]."

---

### Arena 5: M2 (Zweiter Abschnitt der Ärztlichen Prüfung — Hammerexamen)

**Format and Stakes**

National written exam administered by the IMPP. 320 MCQ questions across 3 days (approximately 106-107 per day), 5 hours per day. Every question is a clinical Fallvignette: a patient case with relevant clinical information, followed by a question, followed by 5 answer options. One option is correct. The other four are distractors constructed to exploit specific misconceptions. Subject mix by long-term IMPP average: Internal Medicine approximately 20%, Pharmacology approximately 10%, Surgery and Neurology approximately 5-10% each, plus Gynaecology, Psychiatry, Ophthalmology, ENT, Dermatology, Urology, Radiology, Forensic Medicine, General Medicine, Hygiene, and Occupational Medicine. Pass: ≥60% correct, OR not more than 22% below the mean of first-time takers (Gleitklausel). Grade 1 target: ≥90%. Up to 2 resits allowed. IMPP GK2 structure: Part A covers Krankheitsbilder (disease entities aligned to ICD-10), Part B covers Gesundheitsstörungen (symptoms, clinical findings, abnormal results).

**What the Assessor Is Actually Scoring**

Whether the student can navigate a clinical case from a symptom or finding to the correct decision, under time pressure (90 seconds per question), across 22 subject areas, over 3 consecutive days. The IMPP specifically designs questions to test whether the student thinks like a clinician (symptom → differential → discriminating finding → decision) rather than like a student (topic → facts → match the fact to the option).

**Gold Standard Behavior**

The gold standard M2 student executes the following strategy for every vignette:

1. Read the final sentence of the question first. It tells you what type of question this is: diagnosis, next investigation, management, mechanism, or prognosis.
2. Scan the vignette for three things: the primary complaint (one or two words), the one finding that is abnormal or unexpected, and the time frame (acute, chronic, acute-on-chronic).
3. Form an internal hypothesis before reading the options. A one-word diagnosis or a one-step next action.
4. Read all 5 options. Immediately eliminate the 2 that cannot be correct given the primary complaint and the time frame.
5. Among the remaining 3 options, identify which one the abnormal or unexpected finding in the vignette points to.
6. Select that option.
7. On multiple-select questions: evaluate each option independently. Do not let a confident "true" on option A make option B feel more likely.

The gold standard student does not skip questions. They do not mark a question as uncertain and return to it. They make a decision and move forward. A question returned to with more time available rarely produces a better answer and frequently produces a worse one.

For Key-Feature questions in the digital format: each sub-question is answered based only on the information available at that point in the case. The student does not work backwards from later information. Each node is answered as if the later nodes do not exist.

**Almost-Gold Behavior and the Exact Breaking Point**

The almost-gold student knows the material. Their breaking point is the distractor. IMPP distractors are constructed around the most common misconceptions for each topic. They are partially correct. The almost-gold student reads a distractor that is 80% correct and, because it is plausible, selects it over the 100% correct option. The gold standard student has learned, through SIR question practice, exactly which misconception each distractor exploits for each topic. They recognise the distractor mechanism, not just the content.

Specific example of distractor construction: Vignette presents a 55-year-old male with intermittent claudication at 100 metres, ABI 0.6, no rest pain. Question: what is the most appropriate initial management? Distractor A: "Immediate surgical revascularisation." Distractor B: "Percutaneous transluminal angioplasty within 2 weeks." Correct: "Supervised exercise therapy for 6 months." The almost-gold student selects B because they know PTA is a treatment for peripheral arterial disease. The gold standard student selects C because they know that Fontaine stage IIa/IIb requires 6 months of conservative therapy as the first-line intervention before revascularisation is considered. The almost-gold student knew the treatment; they did not know the threshold for applying it.

**The Trap for Smart Students**

Time collapse. A smart student who is uncertain about a question spends 4 minutes on it instead of 90 seconds. Over a 5-hour exam, 10 uncertain questions at 4 minutes each costs 25 minutes, which is approximately 16 questions lost to time pressure at the end. The gold standard student allocates time mechanically: 90 seconds per question on the first pass, flag uncertain questions, complete the exam, then return to flagged questions with remaining time. They never let uncertainty on one question compound into time loss on questions they would have answered correctly.

---

### Arena 6: M3 (Dritter Abschnitt der Ärztlichen Prüfung)

**Format and Stakes**

Two-day oral-practical exam at the UKD or an HHU Akademisches Lehrkrankenhaus. Up to 4 candidates per commission. Commission: 1 chair + 3-4 examiners. Day 1: assigned real patient, performs anamnesis and physical examination, writes a structured Bericht (see structure below), presents the patient, is examined on examination technique. Day 2: oral viva covering Internal Medicine, Surgery, PJ elective subject, and one randomly assigned "4th subject" notified approximately 2 weeks beforehand. Each day is 45-60 minutes. Pass: "ausreichend" or higher (grade 4). Up to 2 resits. Final Approbation grade: arithmetic mean of M1 + M2 + M3, each weighted one third.

**Day 1: What the Commission Is Actually Scoring**

Whether the student can function as a junior doctor with a real patient in front of them. The commission is watching for: does the student make the patient feel safe? Does the patient understand what is happening? Does the student find the relevant clinical findings? Does the written Bericht reflect what actually happened in the room, or does it reflect a textbook case?

**Day 1: Gold Standard Behavior**

Before entering the patient's room, the gold standard student reads the patient's chart briefly. They note: age, sex, primary diagnosis, main medications. They do not try to pre-formulate the presentation. They go in with a framework, not a conclusion.

With the patient:

- Same introduction sequence as patient presentations (see Arena 3).
- Open question first, full patient narrative before structured questioning.
- Physical exam: announces each step, explains the purpose in plain language, maintains patient dignity throughout (appropriate draping, asking permission before each area of examination).
- When finding something unexpected on physical exam: does not change their facial expression or make a sound. Continues the exam. Notes it mentally. Does not alarm the patient.
- At the end of the exam: thanks the patient, tells them what happens next, does not share differential diagnoses with the patient before the commission has been consulted.

The Bericht structure for Day 1:

1. Anamnese (history): Written in the patient's words where possible. Specific. Not "patient reports headache" but "patient describes sudden-onset occipital headache beginning at 14:30 while lifting, rated 10/10, unlike any previous headache."
2. Befunde (findings): Physical exam findings written in clinical shorthand but precisely. Each system documented: Allgemeinzustand, Bewusstsein, Orientierung, then system by system.
3. Diagnose: Primary diagnosis + 2-3 relevant differential diagnoses each with one sentence justification for inclusion.
4. Prognose: Patient-specific. References comorbidities, performance status, and disease stage. Not a textbook prognosis. This patient's prognosis.
5. Therapieplan: First-line treatment with rationale, alternative if first-line is contraindicated in this patient, monitoring plan.
6. Epikrise: The clinical argument. Minimum 150 words. Links the presenting complaint, the key discriminating findings, the diagnostic pathway, and the treatment decision into a coherent narrative. A commissioner reading only the epicrisis should understand exactly what happened and why.

**Day 2: Gold Standard Behavior**

The oral viva is not a recitation of facts. The commission is watching how the student thinks when asked something unexpected, not how much they know when asked something predictable.

For trauma scenarios (a classic Day 2 scenario):

The gold standard student opens with cABCDE without waiting to be asked:

- c: Catastrophic haemorrhage. "First I control life-threatening external bleeding. Tourniquet or direct pressure."
- A: Airway with cervical spine protection. "I open the airway with jaw thrust rather than head tilt to protect the c-spine."
- B: Breathing. "I auscultate bilaterally, percuss, check for tracheal deviation. A unilateral absence of breath sounds with haemodynamic instability means tension pneumothorax: immediate needle decompression at the second intercostal space, midclavicular line, followed by chest drain."
- C: Circulation. "I assess for haemorrhagic shock: HR, BP, skin colour, cap refill, GCS. Two large-bore IVs. Fluid resuscitation with permissive hypotension target systolic 80-90mmHg in penetrating trauma, 90-100mmHg in blunt trauma until definitive haemorrhage control."
- D: Disability. "GCS, pupils, lateralising signs."
- E: Exposure. "Full exposure with environmental protection. Log roll for posterior inspection. Pelvic binder if pelvic instability suspected — placed at the level of the greater trochanters, with the scrotum positioned free of the binder to avoid compression injury."

The detail about the scrotum placement is not decoration. It is the kind of specific technical knowledge the commission uses to distinguish a student who has done the procedure from one who has read about it.

When the commission asks something the student does not know:

Gold standard verbal response: "Das ist eine gute Frage, zu der ich nicht sofort eine sichere Antwort habe. Ich würde es so angehen: zunächst würde ich [most dangerous possibility] ausschließen wollen, weil [brief reason]. Meine beste Hypothese wäre [X], aber ich bin mir nicht sicher — darf ich fragen, ob ich in die richtige Richtung denke?"

This response does four things: acknowledges the limit of their knowledge without collapsing, demonstrates that they think in terms of differential exclusion even under uncertainty, offers a hypothesis, and invites correction. The commission finds this response more impressive than a student who guesses confidently wrong.

**Almost-Gold Behavior and the Exact Breaking Point**

The almost-gold student has the knowledge. They write a technically correct Bericht. Their oral answers are medically sound. The breaking point is the epicrisis. They write: "The patient presented with headache. CT showed subarachnoid haemorrhage. The patient was treated with nimodipine and referred for neurosurgical assessment." That is a summary. The commissioner reads it and has learned nothing about how this student thinks. The gold standard epicrisis says: "The sudden-onset, maximum-severity headache on exertion in this 48-year-old with known hypertension triggered immediate consideration of subarachnoid haemorrhage. CT confirmed the diagnosis (Fisher Grade 2). Given the patient's haemodynamic stability and GCS 15, conservative management with nimodipine 60mg every 4 hours was initiated for vasospasm prophylaxis. Neurosurgical consultation was requested the same day to evaluate coiling versus clipping based on angiographic anatomy." The commission reading this epicrisis knows that the student understood the risk, made a severity-informed decision, and knows the pharmacological rationale. That student is remembered.

**The Trap for Smart Students**

The expert trap. A student who has studied exceptionally hard tries to impress the commission with niche knowledge. They volunteer information about a third-line treatment option or a recent trial result. The commission is not looking for niche knowledge. They are looking for safe practice. A student who can explain a complex mechanism but hesitates on "what is your first action when this patient's BP drops to 70 systolic" fails the safe practice criterion. Gold standard students lead with the safe action and save the nuance for follow-up questions.

---

## Objective 2: The Clinical Reasoning Engine

### What This Section Does

Defines the decision sequence that the gold standard HHU student runs in every assessment format, from the moment a patient or question appears to the moment they commit to an answer. This engine is not subject-specific. It is the underlying cognitive architecture that works across all arenas. Every subject-level Examiner's Guide must generate questions that test nodes in this sequence.

---

### The Engine: Seven Nodes

**Node 1 — Identify the Patient's Primary Problem**

Not the diagnosis. The problem. The problem is stated in the patient's terms: "this patient cannot breathe comfortably," "this patient has sudden severe abdominal pain," "this patient's blood pressure is falling."

Gold standard: states the problem in one sentence before anything else. Almost-gold: jumps directly to a diagnosis. "This is a pulmonary embolism." The problem may be: "This patient has sudden-onset dyspnoea and pleuritic chest pain with haemodynamic instability." The diagnosis comes later.

**Node 2 — Timestamp the Problem**

Acute (hours to days) / Subacute (days to weeks) / Chronic (months to years) / Acute-on-chronic (stable chronic disease with sudden deterioration).

Gold standard: timestamps immediately and uses it to narrow differentials. Acute-onset dyspnoea eliminates COPD progression. Chronic dyspnoea eliminates PE as the most likely. The timestamp is the first filter. Almost-gold: ignores the timestamp and treats all dyspnoea the same. This is how a student misses the "but the patient has had this for three months" line that eliminates their confident acute diagnosis.

**Node 3 — Localise the Problem**

Organ or system. Not diagnosis. "This is a problem in the hepatobiliary system." "This is a problem in the left lower lobe of the lung." "This is a systemic problem affecting multiple organs."

Gold standard: localises explicitly before generating differentials. Almost-gold: generates differentials based on the chief complaint without first localising. This is how students propose a cardiac cause for a problem that the vignette has already localised to the abdomen by giving a specific physical exam finding.

**Node 4 — Generate the Top Three Differentials That Explain ALL the Findings**

Not just the most likely diagnosis. Not the most dramatic diagnosis. The three diagnoses that together account for every finding in the vignette: the primary complaint, the timeline, the relevant history, the physical exam findings, and the investigation results.

Gold standard: explicitly checks each differential against all findings. "Differential 1 explains the pain and fever but does not explain the jaundice. Differential 2 explains all three. Differential 3 explains the pain and jaundice but not the fever without an additional assumption." Almost-gold: generates the most likely differential and stops. This is how students miss the compound diagnosis (e.g., cholangitis in a patient who also has a coagulopathy from underlying cirrhosis).

**Node 5 — Identify the ONE Discriminating Finding**

From the vignette or the clinical presentation, which single piece of information separates the most likely differential from the second most likely? Not the most striking finding. The discriminating one.

Gold standard: names the discriminating finding explicitly before selecting an answer or deciding a next step. Almost-gold: selects the most striking finding as the anchor, which is frequently what the distractor is constructed around. The IMPP and HHU examiners deliberately make the most striking finding point to the wrong answer. The discriminating finding is often subtle.

Example: A vignette describing right upper quadrant pain, fever, and jaundice (Charcot's triad). The most striking finding is the jaundice. Students anchor on this and select answers about biliary obstruction. The discriminating finding is whether the patient is haemodynamically stable. If they are also confused and hypotensive (Reynolds pentad), the discriminating finding changes the correct answer from "ERCP within 24 hours" to "emergency biliary decompression now."

**Node 6 — Select the Next Best Step Based on the Most Dangerous Differential**

Not the most likely diagnosis. The most dangerous one that has not been excluded. Clinical reasoning in medicine prioritises the exclusion of the diagnosis that would cause the most harm if missed over the confirmation of the most probable diagnosis.

Gold standard: asks "what is the worst thing this could be that I have not yet excluded?" and selects the investigation or action that addresses that question. Almost-gold: selects the investigation or action that confirms the most likely diagnosis. This is how students order a CT abdomen first in a patient with chest pain rather than an ECG. The CT is useful for the most likely diagnosis. The ECG excludes the most dangerous one.

**Node 7 — Apply the Emergency Threshold**

Before committing to any answer: is this a situation where waiting for the investigation result would harm the patient? If yes, treat first and investigate second.

Gold standard: recognises the emergency threshold and acts on it. "This patient has a tension pneumothorax. I do not wait for the CXR. Needle decompression now." Almost-gold: knows the treatment but proposes confirming the diagnosis first because that is what the textbook algorithm shows. The textbook algorithm assumes a stable patient. The vignette does not always give you a stable patient.

---

### Engine Validation: Applied to Real HHU/IMPP Question Types

**Validation Case 1 — Acute Abdomen (Block Exam Archetype)**

Vignette: 72-year-old woman, sudden onset diffuse abdominal pain, rigid abdomen, absent bowel sounds, HR 118, BP 90/60. History of atrial fibrillation, on warfarin. Last meal 6 hours ago.

Node 1: Primary problem — sudden diffuse abdominal pain with haemodynamic instability. Node 2: Timestamp — acute (sudden onset). Node 3: Localise — diffuse abdominal, likely peritoneal irritation or mesenteric. Node 4: Differentials — (1) perforated viscus, (2) mesenteric ischemia, (3) ruptured aortic aneurysm. Node 5: Discriminating finding — history of atrial fibrillation on warfarin. This patient has a known embolic risk. Combined with absolute absence of bowel sounds and haemodynamic instability, the discriminating finding points to mesenteric ischemia. Node 6: Next best step — the most dangerous differential not excluded is mesenteric ischemia. CT angiography abdomen with IV contrast is the appropriate investigation. Node 7: Emergency threshold — this patient is haemodynamically unstable. Resuscitation with IV fluids and surgical consult happen simultaneously with imaging, not sequentially.

Correct answer: "Emergency CT angiography + simultaneous surgical consultation and resuscitation." Distractor: "Urgent laparoscopy." Wrong because CT angiography is required first to confirm the vascular anatomy before surgical planning. Distractor: "IV proton pump inhibitor." Wrong because this is not an upper GI bleed.

**Validation Case 2 — Negative Stem (HHU Surgery Block Archetype, ~40-50% of Surgery Questions)**

Vignette: A 45-year-old presents with a 6-hour history of right iliac fossa pain, nausea, low-grade fever (37.8°C), rebound tenderness on examination. WBC 14. Which of the following is NOT an indication for immediate appendectomy?

Node 1: Primary problem — clinical presentation consistent with acute appendicitis. Node 2: Timestamp — acute, 6 hours. Node 3: Localise — right iliac fossa, consistent with appendix. Node 4: Differentials for negative stem: the question asks what is NOT an indication. The student must know the complete list of indications. Node 5: Discriminating approach — rewrite as positive. "Which of these IS an indication for appendectomy?" Confirm each of the 4 as indications. The one that is NOT an indication is the answer. Node 6: Apply — Appendix mass (phlegmon) without peritonitis is NOT an indication for immediate appendectomy; it is an indication for initial conservative management (antibiotics), with interval appendectomy at 6-8 weeks. Node 7: No emergency threshold change needed — this is a diagnostic discrimination question, not an acute management question.

---

### The Single Most Common Point Where Good Students Break the Engine

Between Node 4 and Node 5.

Good students generate solid differentials. They know the three most likely diagnoses. Then they look at the options and select the option that matches their most likely differential, without performing Node 5 (finding the discriminating finding). They skip the step that would have told them which differential the question is actually testing. This is where most points are lost by students who know the material.

The subject-level Examiner's Guide must generate SIR questions where the distractor is constructed around the most likely differential and the correct answer requires Node 5 to identify. Questions that do not require Node 5 do not train the most important skill.

---

## Objective 3: The Knowledge Architecture

### What This Section Does

Maps the structural connections between clinical subjects so the AI can build subject guides that leverage cross-subject knowledge rather than treating each subject as isolated. A student who internalises this architecture can use what they know from Surgery to reason through an Internal Medicine question they have never seen before. The Abdomen Block is the starting point for this map because it is the most immediate context.

---

### The Abdomen Block Cross-Subject Architecture

The Abdomen Block contains 9 subjects. They are not 9 separate knowledge bases. They are 9 views of the same underlying clinical territory. The mechanisms below recur across subjects and create the transferable knowledge the architecture is built on.

**Mechanism 1: The Inflammation-Infection-Sepsis-Organ Failure Chain**

This chain appears in every heavy subject in the block.

In Surgery: acute cholecystitis → cholangitis → biliary sepsis → multiorgan dysfunction. In Internal Medicine: hepatitis → acute liver failure → hepatorenal syndrome → multiorgan failure. In Urology: urinary tract infection → pyelonephritis → urosepsis → septic shock. In Clinical Chemistry/Hemostaseology: the inflammation markers (CRP, WBC, PCT) and coagulation markers (fibrinogen, D-dimer, PT/INR) that track the progression and define the intervention thresholds.

Cross-subject transfer: a student who knows the sepsis criteria (SIRS → sepsis → septic shock, now refined to qSOFA and SOFA scoring) applies the same framework to the biliary patient in Surgery, the hepatic failure patient in Internal Medicine, and the obstructed ureter patient in Urology. The intervention logic is the same: source control + antibiotics + haemodynamic support. The source differs by subject.

**Mechanism 2: The Obstruction-Ischemia-Perforation Sequence**

Obstruction of a hollow viscus, if untreated, progresses to ischemia of the wall, then perforation, then peritonitis. This sequence is the dominant narrative arc of acute surgical emergencies.

In Surgery: large bowel obstruction (sigmoid volvulus, colorectal cancer) → closed-loop obstruction → cecal ischemia → perforation → fecal peritonitis. In Urology: ureteral obstruction (stone, malignancy) → obstructive uropathy → renal parenchymal damage. The sequence is truncated in urology because the ureter lacks the pressure-building capacity of the colon, but the principle is identical. In Internal Medicine: superior mesenteric artery occlusion → small bowel ischemia → transmural infarction → perforation.

Cross-subject transfer: the moment a student identifies obstruction in any hollow organ, they know to ask: how long? how complete? what is the pressure downstream? These three questions determine urgency and determine whether conservative or operative management is indicated. The mechanism is universal. Only the anatomy differs.

**Mechanism 3: The Portal Hypertension Consequence Map**

Portal hypertension is not a Surgery topic or an Internal Medicine topic. It is a shared territory with different consequences that appear in different exam subjects.

Portal hypertension causes: oesophageal varices (Surgery: haemorrhage management, banding, TIPS), ascites (Internal Medicine: SBP risk, diagnostic paracentesis, albumin supplementation), hepatic encephalopathy (Internal Medicine: lactulose, rifaximin, precipitant identification), hypersplenism with thrombocytopenia and coagulopathy (Clinical Chemistry/Hemostaseology: coagulation cascade disruption in cirrhosis, platelet consumption). On radiology: splenomegaly, portal vein dilation, collateral vessels on Doppler ultrasound and CT.

Cross-subject transfer: a student who understands portal hypertension as a unified mechanism does not need to memorise separate protocols for each complication. They know: increased portal pressure → backpressure → each downstream consequence. The treatment of each consequence follows logically from understanding why that consequence exists.

**Mechanism 4: Biliary and Pancreatic Anatomy as a Shared Key**

The biliopancreatic junction is tested in Surgery (gallstone pancreatitis, cholangitis, ERCP indications), Internal Medicine (pancreatic exocrine insufficiency, pancreatitis grading), Radiology (imaging of biliary dilation, pancreatic duct, stones), and Clinical Chemistry (enzyme patterns: amylase/lipase for pancreatitis, ALP/GGT for biliary obstruction, ALT/AST pattern for hepatocellular vs cholestatic disease).

Cross-subject transfer: the liver enzyme interpretation matrix (ALT > AST → hepatocellular; ALP/GGT elevated disproportionately → cholestatic; all elevated with rising bilirubin → mixed) is a single tool that generates the correct interpretation in Internal Medicine and anchors the radiology question about which imaging study to order next.

**Mechanism 5: Coagulation Cascade as the Thread Between Haematology, Surgery, and Liver Disease**

Clinical Chemistry/Hemostaseology teaches the coagulation cascade. Surgery uses it for bleeding management (antifibrinolytics, FFP, PCC in emergency reversal of anticoagulation). Internal Medicine applies it to the coagulopathy of liver disease (decreased synthesis of all clotting factors except VIII, leading to elevated PT/INR without a correctable single-factor deficiency).

Cross-subject transfer: a student who knows that the liver synthesises all clotting factors except VIII does not need to memorise separately that cirrhotic patients bleed easily, that their FFP requirement is different from a warfarin-overdose patient, and that factor VIII levels can be used to distinguish hepatic from consumptive coagulopathy. They derive all of this from the mechanism.

---

### Cross-Subject Pharmacology Traps in the Abdomen Block

These are drug-related questions that appear to belong to one subject but actually test a cross-subject interaction.

**Trap 1: NSAIDs in Patients with Renal Impairment or Upper GI Disease**

NSAIDs appear in Urology (contraindicated in ureteral colic management if renal impairment), Internal Medicine (contraindicated with peptic ulcer disease, hepatic failure), Surgery (use cautiously post-operatively given renal perfusion effects). The exam tests this by giving a vignette where the "obvious" answer is NSAID analgesia but the vignette contains a contraindication that requires reading the full clinical picture.

**Trap 2: Metronidazole in Hepatic Failure**

Metronidazole is the correct treatment for anaerobic infections and is used in Crohn's disease management. In hepatic failure, metronidazole accumulates due to hepatic metabolism reduction and causes neurotoxicity. The exam gives a cirrhotic patient with an infection where metronidazole seems appropriate, and the correct answer involves dose reduction or alternative selection.

**Trap 3: Anticoagulation in Portal Hypertension with Coagulopathy**

The cirrhotic patient has an elevated INR. The "obvious" interpretation is that they are anti-coagulated and do not need anticoagulation. Wrong. Cirrhotic patients have a rebalanced coagulation: they have low pro-coagulant factors AND low anticoagulant factors (protein C, protein S). The INR does not accurately reflect bleeding risk in cirrhosis. The exam tests this by asking whether a cirrhotic patient with a portal vein thrombosis should receive anticoagulation (yes, in selected patients) or by asking whether the elevated INR in a cirrhotic patient indicates a bleeding risk (not necessarily).

**Trap 4: Proton Pump Inhibitors After Endoscopy for Upper GI Bleeding**

Post-endoscopic management of peptic ulcer bleeding with high-dose PPI is a tested topic. The trap: the dose and duration are specific. Continuous IV omeprazole 80mg bolus + 8mg/hour infusion for 72 hours post-endoscopy for a Forrest Ia or Ib lesion. The exam uses this to distinguish a student who knows "PPI after endoscopy" from one who knows the specific protocol.

---

### How the Knowledge Architecture Informs Subject Guides

Every subject Examiner's Guide built within this system must include a section titled "Cross-Subject Connections" that maps which mechanisms from Objective 3 are tested in that subject and which other subjects test the same mechanism from a different angle. When a pre-study sheet is built for a topic, it must include the mechanism name, not just the topic name. The AI generating the sheet must ask: which mechanism from the Architecture does this topic instantiate? That question determines the depth and the frame of the pre-study content.

---

## Objective 4: The M3 Performance Profile

### What This Section Does

Defines the exact verbal and structural moves that produce a gold standard M3 performance. The M3 is the final clinical synthesis. It is different from every other arena because the examiners are physicians who have been practicing medicine for 10-40 years. They notice things that are not in the mark scheme.

---

### The Patient Presentation: Exact Verbal Sequence (Day 1)

This sequence is reproduced exactly. It is not a framework. It is the script, which the student then adapts to the patient.

**Before entering the room:**

State internally: "I am here to listen first and examine second. I do not know this patient's diagnosis yet, even if I read it on the chart. I will let the examination tell me."

**Entering the room:**

"Guten Tag. Mein Name ist [Vorname Nachname]. Ich bin Medizinstudent/in im [x.] Semester und werde heute die klinische Prüfung ablegen. Mit Ihrer Erlaubnis würde ich gerne die nächsten [x] Minuten damit verbringen, mit Ihnen zu sprechen und Sie zu untersuchen. Ist das für Sie in Ordnung?"

Wait for explicit consent. Do not proceed without it.

**Opening question:**

"Was hat Sie in letzter Zeit am meisten beschäftigt — medizinisch gesehen?" (For chronic patients) OR "Was hat Sie heute hierherbracht?" (For acute presentations)

Then: sit down if possible. Put the notepad down if possible. Look at the patient. Say nothing for 90 seconds minimum.

**After the patient finishes:**

"Danke, dass Sie mir das erzählt haben. Ich möchte sicherstellen, dass ich alles richtig verstanden habe. Können Sie mir noch etwas mehr darüber erzählen, wie es sich anfühlt, wenn [primary symptom] auftritt?"

Then structured history. Then: "Was glauben Sie selbst, warum das passiert?"

**Physical exam transition:**

"Ich würde jetzt gerne zur körperlichen Untersuchung übergehen. Ich werde jeden Schritt ankündigen, bevor ich ihn ausführe. Wenn irgendetwas unangenehm ist, sagen Sie mir bitte Bescheid."

Every step announced. Every finding stated out loud. No prolonged silences.

**Closing with the patient:**

"Vielen Dank für Ihre Zeit und Ihr Vertrauen. Ich werde jetzt meine Befunde besprechen und dann werden meine Kolleginnen und Kollegen weitere Informationen mit Ihnen teilen."

---

### What the Commission Is Listening For (Not in the Mark Scheme)

**1. Hypothesis updating.** If the patient says something unexpected mid-history, does the student pause, integrate it, and adjust their line of questioning? Or do they continue with the pre-planned questions as if the new information did not exist? The commission notices the pivot or the failure to pivot.

**2. Uncertainty tolerance.** When a physical exam finding is ambiguous, does the student acknowledge it? "I am finding something here that I want to be careful about interpreting — there seems to be some dullness on the right, but I want to auscultate again to confirm." Or do they state a finding confidently when they are not sure? The commission trusts a student who is precise about what they know and what they do not.

**3. Patient orientation.** Throughout the history and exam, does the patient appear at ease? The commission cannot always hear what the patient says, but they can see whether the patient looks relaxed or tense. A patient who is visibly uncomfortable during an examination reflects on how the student is behaving toward them.

**4. Sequencing under pressure.** When asked a question in Day 2, does the student answer in a logical sequence, or do they dump information in the order it comes to mind? The gold standard student answers in: diagnosis → rationale → management → monitoring. Not the reverse.

**5. Recovery after being wrong.** When the commission corrects the student, do they collapse? Argue? Or integrate and move forward? Gold standard: "Thank you for the correction. That changes my reasoning in the following way: [update one sentence]. My revised conclusion would be [revised answer]." This response demonstrates that the student can learn in real time, which is the core competency of a junior doctor.

---

### Separating Pass from Performance They Remember

A pass in M3 looks like this: technically correct, well-structured, appropriately safe. The commission signs off. They remember almost nothing specific about this student by the following day.

A performance they remember looks like this: at some point during Day 1 or Day 2, the student said or did something that demonstrated genuine clinical thinking that the commission did not prompt. It could be a specific finding named precisely ("I note a positive Rovsing's sign with radiation to the right iliac fossa on left-sided pressure"). It could be a spontaneous safety check ("Before I start this medication, I want to confirm there is no contraindication given the patient's renal function — their creatinine was 2.1 this morning"). It could be a question the student asks the commission unprompted ("Could I ask — is the patient's bilirubin trending up or down? That would change my urgency assessment significantly").

These moments are not rehearsable as specific lines. They emerge from a student who is genuinely thinking about the patient, not performing for the commission.

---

## Objective 5: The Clinical Identity

### What This Section Does

Defines the non-technical behaviors that examiners observe across every arena and that distinguish a student who is managing the exam from a student who is thinking like a doctor. These are not graded explicitly in most arenas, but they determine how the examiner interprets borderline answers. A technically borderline student who exhibits strong clinical identity gets the benefit of the doubt. A technically borderline student with poor clinical identity does not.

---

### Non-Technical Signals: What the Examiner Notices

**Signal 1: How the Student Handles Not Knowing**

Every student is asked something they do not know in every oral arena. The examiner is watching the response, not the answer. Three categories:

- Collapse: "I'm sorry, I don't know." Full stop. This signals that the student has no strategy for uncertainty. In a clinical setting, this is dangerous.
- Confabulation: The student provides a confident answer that is wrong. This is more dangerous than collapse.
- Clinical not-knowing: "I'm not certain of the specific mechanism, but my approach would be to [describe decision-making process based on what they do know, leading to a reasonable clinical action]." This is the gold standard. It demonstrates that even without the specific fact, the student's reasoning framework is intact.

**Signal 2: How the Student Treats the Patient During Examination**

The commission watches for: does the student maintain the patient's dignity when they have to expose a body part? Do they drape appropriately? Do they tell the patient what they are about to do before they do it? Do they check in on comfort? Do they thank the patient?

These are not minor courtesies. They are competency signals. A student who exposes a patient without explanation and without draping is telling the commission how they will behave when no one is watching.

**Signal 3: How the Student Responds to Correction**

Three categories of response when the commission corrects the student:

- Argue: "But I read that [source] says [different thing]." This is a catastrophic response in the M3. Even if the student is right.
- Collapse: "Oh yes, of course, I'm sorry, you're absolutely right." Followed by immediate full adoption of the corrected view with no reasoning. This signals a student who does not actually understand why the correction is right.
- Integrate: "Thank you — that changes my understanding. If [new information from correction] is correct, then my previous reasoning was wrong at [specific node] because [reason]. My revised conclusion is [updated answer]." This signals a learner. The commission respects this.

**Signal 4: Whether the Student Is Thinking About the Patient or the Exam**

This is subtle but visible. A student thinking about the exam makes eye contact with the examiner during the physical examination. A student thinking about the patient makes eye contact with the patient. A student thinking about the exam pauses at the end of their presentation to gauge the examiner's reaction before continuing. A student thinking about the patient states their next step without checking whether the examiner is pleased first.

The commission sees this. A student who is demonstrably present with the patient, rather than performing for the commission, is trusted more.

**Signal 5: Reasoning Aloud vs. Thinking in Silence**

When performing a physical examination finding that requires interpretation, the gold standard student narrates their reasoning as they go. "I'm percussing over the liver — there is dullness from approximately the fifth intercostal space to the right costal margin — that's roughly normal liver size for this patient's build." This is not for the commission's benefit. It is because a doctor who thinks out loud is a doctor who can be corrected in real time, which is a fundamental safety behaviour.

A student who is silent during a physical exam and then announces a conclusion is harder to correct if they are wrong. The commission knows this. They trust the thinking-out-loud student more.

---

### The Relationship to Not-Knowing as a Clinical Identity Marker

The gold standard student has a healthy relationship to not-knowing. This means:

- They distinguish between "I don't know the answer" and "I don't know how to approach this." The former is a knowledge gap. The latter is a reasoning failure. Acknowledging the former is fine. The latter should not happen.
- They do not treat every question as a test of whether they know the fact. They treat every question as an opportunity to demonstrate how they would figure it out.
- They do not apologise for not knowing. They state their uncertainty precisely and then demonstrate what they would do next.

This relationship to not-knowing is what the M3 is ultimately testing. A doctor who does not know something will look it up, consult a colleague, or reason through the available evidence. A doctor who does not know something and pretends they do is dangerous. The commission has been practicing medicine long enough to tell the difference immediately.

---

## Instructions for Subject and Chapter Examiner's Guides

Every subject-level Examiner's Guide built in this project must reference this document in the following ways:

**1. Arena alignment.** The subject guide must identify which of the 6 arenas its questions are most likely to appear in. A Surgery question is most likely a block exam MCQ or a negative-stem question. It must also appear in M2 (IMPP ~5-10% Surgery) and M3 Day 2. The subject guide must calibrate its question difficulty and framing to the arena that produces the most clinical consequence.

**2. Engine alignment.** Every SIR question generated within the subject guide must require at least one node of the Clinical Reasoning Engine to answer correctly. Questions that are answerable by recall alone (Node 4 is bypassed, Node 5 is bypassed) do not prepare Jani for the block exam. They prepare him for a knowledge quiz. These are not the same test.

**3. Architecture alignment.** The subject guide must include the cross-subject connections relevant to its topic. When a pre-study sheet covers biliary pathology, it must flag the intersection with Clinical Chemistry enzyme patterns, the radiology imaging sequence, and the hemostaseology implications of a cirrhotic patient. These connections are not optional addenda. They are the knowledge transfer mechanism.

**4. Contrast pairs.** Every pre-study sheet and every SIR question must include at least one contrast pair: the gold standard answer and the almost-gold answer, with the specific breaking point identified. A question without a contrast pair does not train discrimination. It only trains recognition.

**5. Behavioral anchoring.** Any claim about what a student "should know" must be translatable into a behavioral description of what they would do or say in the room. If the claim cannot be translated into behavior, it is not precise enough to be useful.

---

_This document is the philosophical and operational foundation of all subject and chapter guides in this project. Every output generated within this project is calibrated against the one-sentence definition at the top of this document and the five behavioral objectives that unpack it._
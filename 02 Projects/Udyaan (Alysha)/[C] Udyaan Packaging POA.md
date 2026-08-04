---
date created: 2026-08-03
date updated: 2026-08-03
deliverable: Week 1 Udyaan
status: DRAFT — review with Suraj Sir
pilot_crop: G9 (Grand Naine)
---

# Udyaan Packaging — Plan of Action

**Deliverable:** How to create smart biodegradable packaging for G9 bananas, from research through prototype.

**Links:** [[C] G9 Banana Research]] · [[C] Udyaan Project Schematics]] · [[C] Udyaan Problem Statement]] · [[00 Introduction to Udyaan (Alysha)]]

---

## Objective

Design and prototype a packaging system for **G9 (Grand Naine) bananas** that:
1. Manages ethylene to extend shelf life (farm → mandi, ambient)
2. Protects from compression during transport and stacking
3. Uses relatively biodegradable materials
4. Includes a pesticide/organic indicator signal

**Success metric (pilot):** Measurable reduction in post-harvest loss vs current pack method, with positive unit economics for the farmer.

---

## Requirements

### Functional Requirements

| # | Requirement | G9-specific spec | Validation method |
|---|---|---|---|
| R1 | **Ethylene management** | Controlled permeability OR 1% vent ratio on film; optional KMnO₄ scavenger sachet (5g) | Shelf-life days vs control at 30±2°C |
| R2 | **Compression protection** | Rigid outer (CFB or molded pulp tray) + no direct fruit-on-fruit stacking load | Bruise % after simulated transport stack |
| R3 | **Moisture control** | Limit physiological weight loss to <10% over 14 days | Weight loss % measurement |
| R4 | **Shelf life extension** | ≥15 days ambient (vs ~9 days unpackaged baseline) | Days to spoilage threshold |
| R5 | **Biodegradability** | Material compostable within 180 days OR 90% biodegradation per IS/ISO standard | Supplier cert + disposal test |
| R6 | **Pesticide/organic indicator** | Visible signal change if pesticide residue above organic threshold; intact signal = organic-verified pack | Lab test with known residue samples |
| R7 | **Food safety** | No calcium carbide contact; GRAS materials only | Material safety data sheets |
| R8 | **Cost** | Pack cost < value of loss prevented per kg G9 | Unit economics worksheet |

### Non-Functional Requirements

| # | Requirement | Target |
|---|---|---|
| NF1 | Usable by farmers without training | Single-step pack process |
| NF2 | Stackable for mandi transport | Standard crate footprint |
| NF3 | Humidity tolerant | Performs at 70–90% RH |
| NF4 | Scalable production | Supplier can produce ≥1,000 units for pilot |
| NF5 | Brandable | Udyaan mark + organic signal visible on exterior |

---

## Plan of Action — 5 Phases

### Phase 1: Research + Baseline (Week 1 — now)

**Goal:** Know the current state and the science before designing.

| Step | Action | Output | Owner |
|---|---|---|---|
| 1.1 | Complete G9 research brief | [[C] G9 Banana Research]] | Ash ✓ |
| 1.2 | Interview 2–3 farmers/traders on current G9 pack + loss points | Field notes in Brain Dump | Ash |
| 1.3 | Document current pack method in Udyaan supply chain | "As-is" photo + description | Ash + Suraj Sir |
| 1.4 | Benchmark LDPE 300g/1% vent as science baseline | Benchmark table | Ash |
| 1.5 | Finalize problem statement with G9-specific funnel | [[C] Udyaan Problem Statement]] | Ash |

**Exit criteria:** Written problem statement + G9 baseline documented.

---

### Phase 2: Material Selection (Week 2)

**Goal:** Pick substrate stack that meets R1–R5.

| Step | Action | Output |
|---|---|---|
| 2.1 | Scan biodegradable film suppliers (PLA, starch, cellulose) | Supplier shortlist (3+) |
| 2.2 | Request permeability + ethylene transmission rate data | Material spec sheets |
| 2.3 | Evaluate molded pulp / banana-fiber tray for outer structure | Tray prototype options |
| 2.4 | Research chitosan coating as antimicrobial + shelf-life layer | Coating feasibility note |
| 2.5 | Research pesticide indicator inks/strips (food-contact grade) | Indicator mechanism decision |
| 2.6 | Build material stack: **outer + inner + sachet + indicator** | Material stack diagram |

**Design hypothesis (starting point):**
```
┌─────────────────────────────────────┐
│  Outer: molded biodegradable tray   │  ← compression (R2)
│  ┌───────────────────────────────┐  │
│  │ Inner: biofilm liner w/ 1%    │  │  ← ethylene (R1) + moisture (R3)
│  │ vents + optional KMnO₄ sachet │  │
│  │  ┌─────────────────────────┐  │  │
│  │  │ G9 hands (crown-treated)│  │  │
│  │  └─────────────────────────┘  │  │
│  └───────────────────────────────┘  │
│  Indicator strip on exterior seal   │  ← organic/pesticide (R6)
└─────────────────────────────────────┘
```

**Exit criteria:** Material stack selected with supplier quotes.

---

### Phase 3: Prototype (Week 3–4)

**Goal:** Physical samples for ambient storage test.

| Step | Action | Output |
|---|---|---|
| 3.1 | Order prototype materials (min viable qty) | Materials in hand |
| 3.2 | Define pack SOP: harvest stage → crown wash → dry → pack → seal | 1-page SOP |
| 3.3 | Pack 3 test batches: (a) current method (b) LDPE benchmark (c) Udyaan prototype | 3 × 20-hand batches |
| 3.4 | Run ambient storage test at 30±2°C | Daily log: weight, firmness, colour, spoilage % |
| 3.5 | Run compression simulation (stacked crate, 24hr) | Bruise count |
| 3.6 | Test indicator with known pesticide/no-pesticide samples | Indicator accuracy log |

**Exit criteria:** 15+ days shelf life on prototype OR clear data on which layer failed.

---

### Phase 4: Unit Economics + Problem Pricing (Week 4)

**Goal:** Put a rupee amount on the problem and the solution.

| Step | Action | Output |
|---|---|---|
| 4.1 | Cost per pack (materials + labour + sachet + indicator) | COGS per unit |
| 4.2 | Loss prevented per kg (baseline loss % − prototype loss %) × farmgate price | Value created per pack |
| 4.3 | Farmer ROI: value created − pack cost | Go/no-go margin |
| 4.4 | Price the problem for pitch (cohort + industry) | Priced problem statement |
| 4.5 | Draft offer letter | Week 2 deliverable |

**Exit criteria:** Positive farmer ROI at pilot scale OR documented path to get there.

---

### Phase 5: Pilot Deployment (Month 2+)

**Goal:** Real-world test with Udyaan partner farmers.

| Step | Action | Output |
|---|---|---|
| 5.1 | Select 3–5 G9 farmers in Udyaan network | Pilot roster |
| 5.2 | Train on pack SOP (1 session) | Training done |
| 5.3 | Run 2-week pilot: Udyaan pack vs their current pack | Side-by-side loss data |
| 5.4 | Collect farmer feedback (would they pay? how much?) | 3+ farmer interviews |
| 5.5 | Iterate prototype based on field data | v2 spec |
| 5.6 | Document for cohort procoding experiment | Case study |

**Exit criteria:** Field-validated loss reduction + farmer willingness to pay.

---

## Pre-Pack Protocol (G9 — Non-Negotiable)

Packaging alone won't work without proper pre-pack handling:

1. Harvest at correct maturity (75–80% for longer transit)
2. Wash hands in **alum water** to remove latex (prevents crown rot)
3. Air-dry before packing
4. Crown fungicide treatment (if not organic — document for indicator)
5. Pack within 4 hours of harvest
6. No calcium carbide at any stage (organic integrity)

---

## Decision Log

| Date | Decision | Rationale |
|---|---|---|
| 2026-08-03 | Pilot crop = G9 (Grand Naine) | High loss %, climacteric (tests ethylene layer), established market |
| 2026-08-03 | Science baseline = LDPE 300g + 1% vents | Best validated ambient spec for Grand Naine |
| 2026-08-03 | Udyaan must beat or match LDPE on shelf life with biodegradable stack | Differentiator |

---

## Open Questions

- [ ] Which supply chain leg first: farm→mandi (ambient) or export (reefer)?
- [ ] Indicator mechanism: chemical strip vs QR + batch lab test?
- [ ] Can chitosan coating replace part of the inner film?
- [ ] Who manufactures prototype — Udyaan lab or external vendor?
- [ ] Suraj Sir approval on material budget for Phase 3

---

## Last Updated

2026-08-03 — Initial POA. G9 locked. Requirements + 5-phase plan drafted.

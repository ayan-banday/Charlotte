---
date created: 2026-08-03
date updated: 2026-08-03
---

# Udyaan Project Schematics

Visual map of the problem, solution, and build sequence. Update as research validates numbers.

---

## 1. Problem Funnel — Post-Harvest Loss

```
FARM HARVEST
    │
    ▼
┌─────────────────────────────────────┐
│  PACKAGING (farm → mandi)           │  Ash est: 2–3%  │  ← PRIMARY WEDGE
└─────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────┐
│  TRANSPORT + GRADING                │  TBD %          │  compression damage here
└─────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────┐
│  MARKET REACH + SHELF LIFE          │  TBD %          │  ethylene / time decay
└─────────────────────────────────────┘
    │
    ▼
TOTAL LOSS: Ash est 30–45%  │  National official: 5–15% (veg/fruit, NABCONS 2022)
```

### Research baseline (NABCONS 2022, MoFPI)

| Commodity | Loss % | Volume lost |
|---|---|---|
| Fruits | 6.02–15.05% | 7.36 million MT |
| Vegetables | 4.87–11.61% | 11.97 million MT |
| **National $ value** | — | **~₹1.53 lakh crore/year** (~$18.3B) |

**Worst single crops:** Guava 15.05% · Tomato 11.61% · Apple 9.51%

**Note:** Official figures measure harvest + post-harvest across all stages. Ash's 30–45% may include retail/consumer-stage waste or be crop-specific — **validate with Suraj Sir + field data from Udyaan partners.**

### Funnel research tasks

- [ ] Break NABCONS losses by stage (harvest / handling / storage / transport / market)
- [ ] Pick 1–2 target commodities for pilot (tomato? leafy greens?)
- [ ] Calculate addressable loss = packaging-fixable % × crop volume × farmgate price
- [ ] Interview 3 farmers/traders on where they actually lose money

---

## 2. Solution Architecture

```
┌──────────────────────────────────────────────────────────┐
│                    UDYAAN SMART PACK                      │
├──────────────────────────────────────────────────────────┤
│  LAYER 1: Ethylene management                            │
│    → Permeable / controlled atmosphere for ripening      │
│    → Prevents premature spoilage in transit              │
├──────────────────────────────────────────────────────────┤
│  LAYER 2: Compression protection                         │
│    → Structural integrity farm → mandi → shelf           │
│    → Reduces bruising / crushing losses                  │
├──────────────────────────────────────────────────────────┤
│  LAYER 3: Biodegradable substrate                        │
│    → Fresh vegetable use case                            │
│    → Environmental compliance for organic positioning    │
├──────────────────────────────────────────────────────────┤
│  LAYER 4: Pesticide / organic indicator                  │
│    → On-pack signal if pesticides detected               │
│    → Organic farmers: packaging = trust layer            │
│    → OPEN: mechanism (chemical indicator / sensor / tag)   │
└──────────────────────────────────────────────────────────┘
```

### Solution validation questions

| Requirement | Status | Next step |
|---|---|---|
| Ethylene management | Concept | Material science research / supplier scan |
| Compression protection | Concept | Benchmark existing crates + corrugated |
| Biodegradable | Concept | Define "relatively" — compost timeline, cost |
| Pesticide/organic signal | Concept | Define "ignite signal" — tech feasibility study |
| Unit economics | Not started | Tie to finance sourcebook (Ch 4+ variable costs) |

---

## 3. Stakeholder Map

```
                    ┌─────────────┐
                    │  Suraj Sir  │  project lead
                    └──────┬──────┘
                           │
         ┌─────────────────┼─────────────────┐
         ▼                 ▼                 ▼
   ┌──────────┐     ┌────────────┐    ┌──────────┐
   │   Jane   │     │ Ma'am      │    │  Ash     │
   │ (HO mtg) │     │ Sheradha   │    │ problem  │
   └──────────┘     │ distrib +  │    │ + cohort │
                    │ curriculum │    └──────────┘
                    └────────────┘
                           │
                           ▼
              ┌────────────────────────┐
              │ 10 students (cohort)   │
              │ procoding experiments  │
              └────────────────────────┘
                           │
                           ▼
              ┌────────────────────────┐
              │ Farmers / traders /    │
              │ mandi operators        │
              └────────────────────────┘
```

---

## 4. Build Sequence (Q3 → Q4)

```
Week 1 (now)     Problem statement + funnel research
       │
Week 2           Price the problem → offer letter draft
       │
Week 3           Curriculum + industry outreach
       │
Week 4           10 students · pipeline · ₹1L contract path
       │
Q4               ₹10L revenue · 3 premium pitches · top 5 problems
```

---

## 5. Active Tasks (from Aug 3)

| # | Task | Owner | Due | Status |
|---|---|---|---|---|
| 1 | Finalize written problem statement | Ash | Aug 9 | Draft |
| 2 | Research loss funnel by stage + rupee amount | Ash | Aug 9 | Started |
| 3 | Suraj Sir conversation | Ash | Aug 9 | Pending |
| 4 | 3 student convos recorded | Ash | Aug 9 | Pending |
| 5 | Gap selling notes revised | Ash | Aug 9 | Pending |
| 6 | Define pesticide/organic indicator mechanism | Ash + team | Week 2 | Open |
| 7 | Material/supplier scan for biodegradable + ethylene | Cohort | Week 2+ | Not started |

---

## Sources

- [MoFPI / NABCONS Post-Harvest Loss Study 2022](https://www.mofpi.gov.in/sites/default/files/572.pdf)
- [FACTLY summary — ₹1.53L cr national loss](https://factly.in/from-guava-to-milk-what-food-loss-reveals-about-indias-supply-chains/)
- Ash field estimates from Jane meeting, Aug 3 2026

---

## Last Updated

2026-08-03 — Initial schematic from head office meeting. Funnel numbers flagged for validation.

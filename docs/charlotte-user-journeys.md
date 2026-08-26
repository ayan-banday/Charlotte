---
date created: 2026-08-26
date updated: 2026-08-26
purpose: User journey diagrams — how Ash uses Charlotte daily
---

# Charlotte User Journeys

Companion to `charlotte-rebuild-spec.md`. Read this when asking "what do I actually do?"

---

## System map (you ↔ surfaces)

```mermaid
flowchart TB
    subgraph capture["Capture"]
        TG[Telegram brain dump]
        CQ[Capture Queue file]
    end

    subgraph orient["Orient — Obsidian + Calendar"]
        CC[Command Center note]
        Gantt[Task Gantt / week view]
        GCal[Google Calendar events]
    end

    subgraph work["Work — IDE"]
        IDE[Cursor / Claude Code / Codex]
        CH[Charlotte]
        GF[Graphify query]
        WF[Workflow + skills]
    end

    subgraph sink["Build sink"]
        BH[Black Hole folder]
    end

    subgraph vault["Vault markdown"]
        PR[02 Projects]
        SK[Skills Library]
        WK[Week files]
    end

    subgraph external["External"]
        DRV[Google Drive team files]
    end

    TG --> CQ
    CC --> Gantt
    CC --> GCal
    GCal -->|"what to do now"| IDE
    IDE --> CH
    CH --> GF
    GF --> WF
    WF --> PR
    WF --> BH
    BH -->|"you approve promote"| DRV
    BH -->|"you approve promote"| PR
```

---

## Daily loop (typical day)

```mermaid
flowchart LR
    A[Wake] --> B[Open Obsidian Command Center]
    B --> C[See GCal events + Gantt this week]
    C --> D{Working now?}

    D -->|Walk| E[Telegram captures]
    E --> F[Capture Queue]

    D -->|Laptop| G[Open IDE]
    G --> H["Tell Charlotte what to do"]
    H --> I[Workflow runs]
    I --> J[Output to project or Black Hole]

    F --> K[6pm Routing Batch]
    K --> L[Proposals Telegram + IDE]
    L --> M{You approve}
    M -->|yes| N[Route to brain dump / week file]
    M -->|yes deliverable| O[Create GCal event]
    M -->|no| P[Log skip]

    M --> Q[Reflect in IDE optional]
    Q --> R[Week file updated]
```

---

## Work session — write a newsletter (example)

```mermaid
flowchart TD
    S1[Obsidian: event Write newsletter 9-10am] --> S2[Open IDE]
    S2 --> S3["Say: write a newsletter"]
    S3 --> S4[Charlotte loads SOUL + MEMORY only]
    S4 --> S5[Graphify: newsletter workflow + skills]
    S5 --> S6[Read Write a Newsletter.md]
    S6 --> S7[Step 1 Mine — newsletter-writing-system]
    S7 --> S8[Step 2 Hooks — content-hook-research]
    S8 --> S9[Step 3 Draft — ash-newsletter-voice]
    S9 --> S10[Step 4 Humanize — text-humanizer]
    S10 --> S11[Step 5 Image — newsletter-image-generator]
    S11 --> S12[Step 6 Save draft to Newsletter project]
    S12 --> S13[Done — draft in 02 Projects not Black Hole]
```

**Copy / poster (shorter path):** no full workflow file — Charlotte loads `direct-response-copy` or `short-form-content` + project brain dump. Same IDE session pattern.

**Webinar:** trigger `Launch a Webinar Funnel` workflow → phase 1 uses `webinar-planning` → subsequent phases chain webinar-* skills per project intro.

**Manus deck build:** Manus writes to `Black Hole/udyaan-deck-YYYY-MM-DD/`. You review in Obsidian link or filesystem. Evening batch may propose "promote to Drive" — you approve.

---

## What you touch vs what runs itself

| You do | System does on **git commit** |
|---|---|
| `git commit` / push | **Sync hook** → `vault-index.json` + Graphify `--update` |
| Telegram while walking | Append Capture Queue |
| Open Obsidian morning | Show projects + timeline + calendar |
| Say what to work on in IDE | Read vault-index slice + Graphify + workflow only |
| `new project` in IDE | Template folder; sync after you commit |
| Approve 6pm proposals | Route captures, optional GCal events |
| Promote Black Hole → Drive/project | Manual or approve evening proposal |

**No watcher app.** Commit is the sync point. Optional 17:30 scheduled sync before 6pm batch.

| System never does without approval |
|---|
| Add calendar commitment |
| File capture to brain dump |
| Promote Black Hole artifact |
| Edit Patterns.md / MEMORY.md from daily capture |

---

## One question still open

**Command Center note location:** `00 Command Center.md` at vault root vs inside `00 Self-Management/`? Spec assumes vault root for fastest Obsidian open.

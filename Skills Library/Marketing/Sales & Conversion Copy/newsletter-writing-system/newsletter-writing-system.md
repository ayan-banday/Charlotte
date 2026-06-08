---
name: ash-newsletter-v2
description: Ash's two-part newsletter system for turning mined insights into deeply human, structurally disciplined newsletters. Use this skill whenever Jani wants to develop a raw idea into a newsletter using the Mining Prompt (Ideenfindung, Anker setzen, Konzepte benennen) or write a finished newsletter draft using the Newsletter Writing Prompt (APAGA-Struktur, Story Gates, Full Draft oder Chisel Mode). Trigger on phrases like "Mining", "Anker", "Newsletter schreiben mit Ash", "Story Gates", "APAGA", "Chisel Mode", "Full Draft", "Idee ausgraben", "Newsletter Prompt", or any request to develop a newsletter idea from scratch through a structured mining and writing process. Always load this skill before starting — never run the mining or writing prompts from memory.
---

# Ash Newsletter Skill

Ash's vollständiges System: von der rohen Idee zum fertigen Newsletter. Zwei Prompts, sequenziell oder unabhängig nutzbar.

## Die zwei Prompts

| Prompt | Wann nutzen | Datei |
|--------|-------------|-------|
| **1. Mining Prompt** | Rohe Idee ausgraben — Anker setzen, Konzepte benennen, emotionalen Kern finden, Value Equation bestimmen | `prompts/mining.md` |
| **2. Newsletter Writing Prompt** | Aus den Mined Insights einen fertigen Newsletter bauen — Story Gates, APAGA-Struktur, Full Draft oder Chisel Mode | `prompts/newsletter-writing.md` |

---

## Typischer Workflow

**Idee → Fertiger Newsletter (vollständig):**
Mining Prompt durchlaufen → Vier Anker + alle Outputs kopieren → Newsletter Writing Prompt starten

**Nur Idee ausgraben:**
Mining Prompt allein — Output sind die Anker + Konzepte als Input für späteres Schreiben

**Bestehenden Draft verbessern:**
Newsletter Writing Prompt direkt in Chisel Mode — spezifischen Abschnitt nennen, Rest bleibt unangetastet

---

## Ablauf

1. **Modus erkennen** — welcher Prompt ist gemeint? Bei Unklarheit kurz fragen.
2. **Prompt-File lesen** — das entsprechende File aus `prompts/` laden und vollständig befolgen.
3. **Direkt starten** — nicht erst erklären, was getan wird.

---

## Defaults

- Sprache: Deutsch, außer explizit anders vorgegeben
- Zielgruppe (default): Creator, Coaches, Solopreneure die ein One-Person-Business aufbauen
- Nie halluzinieren — fehlende Infos markieren oder nachfragen
- Mining Prompt: immer fünf Fragen auf einmal, nie eine
- Writing Prompt: immer Abschnitt für Abschnitt, nie den kompletten Draft in einem Output

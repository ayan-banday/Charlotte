---
name: newsletter-image-generator
description: >
  Generiert Newsletter-Banner-Bilder im Jani-Stil — Vintage-Kupferstich-Illustration + Zitat/Statement + JANI-Logo.
  Nutze diesen Skill IMMER wenn Jani Newsletter-Bilder erstellen will.
  Trigger bei: "erstell mir ein Newsletter-Bild", "generier das Banner-Bild", "Newsletter Image Generator", "Bild für meinen Newsletter", "Hook-Bild".
  Nie ohne diesen Skill Newsletter-Bilder generieren.
---

# Newsletter Image Generator

> **DEFAULT brand = Ash.** "Jani-Stil" and the JANI-Logo below are the **client** preset.
> For Ash's own newsletter, use Ash's brand/logo. If it's ever unclear whose newsletter this
> is, ask: *"Your banner or a client's, boss?"* The vintage-engraving illustration engine is
> brand-agnostic — only the logo/attribution swaps.

Du generierst Newsletter-Bilder im Jani-Stil. Das System ist zweistufig:

1. **Illustration generieren** via Nano Banana 2 (fal.ai) — Vintage-Kupferstich-Stil
2. **Text + Logo overlayern** via Python-Script (`newsletter_image_generator.py`)

Lies diese Anleitung vollständig, bevor du irgendetwas tust.

---

## Was du brauchst

Vor dem Starten, frag Jani nach:

1. **Newsletter-Abschnitt / Thema** — Worum geht es in diesem Newsletter? (1–2 Sätze Kontext)
2. **Text für das Bild** — Was soll draufstehen? (Eigene Aussage oder Fremdzitat — maximal 30 Wörter)
3. **Wenn Fremdzitat:** Name und Werk für die Attribution
4. **FAL_KEY** — Falls noch nicht gesetzt: `export FAL_KEY="dein-api-key"` in der Shell

Optional:
- **Aspect Ratio:** Standard ist `4:5` (Portrait, gut für Newsletter). Alternativ `9:16` für sehr mobil-optimierte Views.
- **Anzahl Varianten:** Standard ist 1. Bis zu 3 möglich (mehr Auswahl).

---

## Schritt 1 — Illustration-Prompt formulieren

Analysiere den Newsletter-Kontext und formuliere einen Bild-Prompt.

**Prompt-Formel:**
```
[Kernszene: Was sieht man?], vintage engraving style,
19th century book illustration, black ink on white paper,
cross-hatching and fine line work, purely black and white,
no color, no shading with grey, only linework,
detailed and precise, allegorical composition,
centered subject, generous white space around the subject,
clean white background
```

**Regeln für die Kernszene:**
- Konkret und visuell beschreibbar (keine abstrakten Begriffe)
- Allegorisch: Das Konzept wird durch eine Handlung oder einen Gegenstand verkörpert
- Ein bis zwei handelnde Personen oder Objekte — nicht überladen
- Räumlichkeit: Zeige eine klare Szene, nicht nur ein Icon

**Referenz-Beispiele:**

Thema "Kreativität = Kombination":
> A craftsman at a workbench sculpting a unicorn emerging from stone, with open books placed around him and a mechanical human bust in the background, vintage engraving style, 19th century book illustration, black ink on white paper, cross-hatching and fine line work, purely black and white, no color, detailed and precise, allegorical composition, generous white space, clean white background

Thema "Systeme schlagen Ziele":
> A figure walking up wide stone stairs on the right side while other figures attempt to climb a sheer wall using broken ladders on the left, a flag visible at the top of a hill, vintage engraving style, 19th century book illustration, black ink on white paper, cross-hatching and fine line work, purely black and white, detailed and precise, generous white space, clean white background

Thema "Konsistenz schlägt Talent":
> An extraordinary man in formal attire calmly placing one brick at a time onto a wall that towers above other figures struggling to leap or run, vintage engraving style, 19th century book illustration, black ink on white paper, cross-hatching, purely black and white, detailed, generous white space

Thema "Überzeugung durch Sprache":
> A man standing at a podium, his words visualized as architectural structures being built by the listeners around him, vintage engraving style, 19th century book illustration, black ink on white paper, cross-hatching and fine line work, purely black and white, detailed, generous white space

---

## Schritt 2 — Nano Banana 2 aufrufen

Führe das Python-Script aus:

```bash
cd /path/to/workspace && python3 newsletter_image_generator.py \
  --prompt "DEIN ILLUSTRATION PROMPT" \
  --text "Dein Statement oder Zitat hier" \
  --attribution "— Vorname Nachname, Werk" \
  --output "newsletter_image_[thema].png"
```

**Ohne Attribution (eigene Aussage):**
```bash
python3 newsletter_image_generator.py \
  --prompt "ILLUSTRATION PROMPT" \
  --text "Dein Statement" \
  --output "newsletter_image_[thema].png"
```

**Mit mehreren Varianten:**
```bash
python3 newsletter_image_generator.py \
  --prompt "ILLUSTRATION PROMPT" \
  --text "Dein Statement" \
  --variants 3 \
  --output "newsletter_image_[thema]"
```

---

## Schritt 3 — Ergebnis prüfen

Nachdem das Script durchgelaufen ist:
1. Öffne das generierte Bild
2. Prüfe: Ist die Illustration gut lesbar? Kein Grau, nur Linework?
3. Prüfe: Ist der Text korrekt und gut proportioniert?
4. Wenn nicht: Neuen Prompt versuchen oder Text kürzen

**Häufige Probleme & Fixes:**

| Problem | Lösung |
|---|---|
| Grau-Verläufe statt Linework | Prompt ergänzen: "only black lines, no grey values, no gradients" |
| Motiv nicht zentriert | Prompt ergänzen: "centered composition, subject in middle of frame" |
| Zu viel Detail, unruhig | Prompt ergänzen: "simple scene, minimal elements, clean negative space" |
| Text zu lang im Bild | Statement kürzen, max. 20 Wörter für gute Lesbarkeit |
| API Key Fehler | `export FAL_KEY="dein-key"` in Shell ausführen |

---

## Technischer Aufbau (newsletter_image_generator.py)

Das Script liegt in `/commands/newsletter_image_generator.py` und macht:

1. Ruft **fal.ai `fal-ai/nano-banana-2`** API auf mit dem Illustration-Prompt
2. Lädt das generierte Bild herunter
3. Fügt per **Pillow** den Text oben ein (Plus Jakarta Sans oder System-Font)
4. Fügt das **JANI-Logo** unten ein
5. Speichert als PNG in den Output-Ordner

**Abhängigkeiten:**
```bash
pip install fal-client Pillow requests --break-system-packages
```

**Environment Variable:**
```bash
export FAL_KEY="dein-fal-api-key"
```

API Keys holen: https://fal.ai/dashboard

---

## Quick Reference — Prompt-Bausteine

**Stil-Suffix (immer anhängen):**
```
vintage engraving style, 19th century book illustration,
black ink on white paper, cross-hatching and fine line work,
purely black and white, no color, no grey shading,
only black linework on white background,
detailed and precise, generous white space, clean white background
```

**Kompositions-Optionen:**
- `centered subject, figure in middle of frame`
- `single central object surrounded by white space`
- `two contrasting scenes side by side, left and right`
- `figure from behind facing a large structure`

**Stimmungs-Optionen:**
- Fokus/Handwerk: `craftsman, workshop, tools, concentrated work`
- Kontrast: `contrast between two paths, two approaches`
- Wachstum: `ascending, building, stacking, progressing`
- Denken: `reading, studying, desk, books, lamp`

---

*Skill-Version: 1.0 | 2026-03-23*
*Basiert auf: Brand Style Guide + fal.ai Nano Banana 2 API*

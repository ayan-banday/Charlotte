---
name: jani-insight-email
description: >
  Schreibt einen kompletten, fertigen Newsletter für Jani auf Basis eines Kerninsights — mit Entry Point, Story, Core Insight, Delivery-Mode und CTA. Nutze diesen Skill IMMER wenn Jani eine fertige Email oder Newsletter schreiben will und schon eine Idee, einen Angle oder einen Insight hat. Trigger bei: "schreib mir den Newsletter", "ich will eine Email schreiben über X", "schreib das als Newsletter aus", "lass uns die Email schreiben", "schreib den aus", oder wenn Jani nach dem jani-newsletter-ideas Skill eine Idee gewählt hat. Immer diesen Skill laden bevor du eine komplette Newsletter-Email für Jani schreibst. Nie aus dem Kopf schreiben — immer erst diesen Skill lesen.
---

# Jani Insight Newsletter Writer

> **DEFAULT = Ash.** This is the client (Jani) writer; its `…/Jarvis/…` context paths and the
> `jani-voice` skill live in Jani's vault, not here. For Ash's own newsletter, use the
> **`Write a Newsletter` workflow** instead — it writes in `ash-newsletter-voice` with local
> context (`/System/MEMORY.md`, `[C] RGS.md`). Use this skill only when writing *for Jani*.

Dieser Skill schreibt einen fertigen, vollständigen Newsletter für Jani — in seiner Stimme, mit seiner Struktur, ohne KI-Muster.

---

## Vor dem Schreiben

### Schritt 1 — Kontext laden

Lies diese Dateien zuerst:

- `/sessions/sharp-great-tesla/mnt/Jarvis/02 Projects/Writing Station/[C] Newsletter Writing Principles.md` — die Non-Negotiables für Janis Schreibstil
- `/sessions/sharp-great-tesla/mnt/Jarvis/CLAUDE.md` — aktueller Fokus, Produkte, Ziele
- `/sessions/sharp-great-tesla/mnt/Jarvis/Context/[C] Ziele 2026.md` — welcher Quartal, welcher CTA macht Sinn

Lies außerdem die `jani-voice` Skill (im System bereits geladen) für Rhythmus, Lexik und Verbote.

### Schritt 2 — Abstimmung mit Jani

Bevor du anfängst zu schreiben, bestätige Entry Point und Angle. Schreibe kurz:

- Den Angle in einem Satz: Was ist der eigentliche Drive dieser Email?
- Den Entry Point: Die konkrete Szene oder Situation, mit der die Email öffnet
- Das Schreibmodell: Lesson-Mode / Story-Mode / Resource-Mode

Dann frag: "Passt das so? Oder willst du den Einstieg anders setzen?" Warte auf grünes Licht. Kein Überraschungs-Draft am Ende.

---

## Die Struktur

### 1. Entry Point (2–4 Sätze)

Der Einstieg zieht den Leser in eine Welt — nicht in ein Thema. Der Leser soll nach zwei Sätzen wissen, wohin die Reise geht, aber noch nicht warum.

Was hier reingehört:
- Ein persönlicher Moment, eine Situation, ein Fehler, eine Beobachtung
- Ultra-konkret: Zeit, Ort, Situation — kein "eines Tages", sondern "letzten Dienstag um 23 Uhr"
- Der Leser soll sich in der Situation wiederfinden oder sich vorstellen können, dabei zu sein

Was hier nicht reingehört:
- Thesen oder Behauptungen
- Zusammenfassungen von dem, was gleich kommt
- Abstrakte Eröffnungen ("In einer Welt, in der...")

**Beispiel (Feeling, nicht kopieren):**
> "Letzte Woche saß ich um halb zwölf nachts vor meinem Laptop und hatte einen Text geöffnet, der nach niemandem klang. Nicht nach mir, nicht nach meinen Lesern, nicht nach irgendetwas Echtem. Ich hatte ChatGPT gefragt, mir einen Post zu schreiben — und bekommen, was ich verdient hatte."

---

### 2. Tension Through Story (5–12 Sätze)

Hier entsteht Energie. Die Geschichte verknüpft den Entry Point mit dem Insight — nicht direkt, sondern durch Spannung.

Was hier passiert:
- Die Situation entwickelt sich: Was hat Jani gedacht, gemacht, erlebt?
- Konkrete Details, die man sich vorstellen kann: Geräusche, Orte, Gespräche, Zahlen
- Janis eigener Kommentar dazu — kein neutrales Berichten, sondern echte Perspektive
- Ein oder zwei natürliche Übergänge, die von der Geschichte in Richtung Insight führen

Was hier nicht reingehört:
- Belehrungen schon in dieser Phase
- Abstrakte Schlussfolgerungen ("Das zeigte mir, wie wichtig X ist")
- Passivkonstruktionen oder distanzierte Sprache

**Wichtig:** Bleib in der Geschichte. Der Insight kommt noch nicht — erst die Story, dann der Schwenk.

---

### 3. Der Core Insight

Das ist die eigentliche Botschaft der Email. Ein Satz, der die Wahrheit nennt.

Dieser Satz muss:
- Konkret genug sein, dass man ihn nicht mit etwas anderem verwechselt
- Aus der Geschichte entstehen — nicht von oben eingefügt werden
- Den Leser kurz innehalten lassen

Dann: Den Insight mindestens dreimal in der Email reformulieren — nicht wiederholen, sondern aus verschiedenen Blickwinkeln zeigen. Einmal direkt nach dem Schwenk, einmal im Delivery-Teil, einmal am Ende (oder im CTA).

---

### 4. Delivery (nach Schreibmodell)

#### Lesson-Mode
Der Insight hat praktische Konsequenzen — der Leser will wissen, was er damit macht.

- 3–5 konkrete Schritte, klar nummeriert
- Kein Fluff, kein Allgemeinwissen — nur Dinge, die direkt aus dem Insight folgen
- Optional: ein Callout-Box für einen Begriff oder ein Framework, das Jani nutzt
- Jeder Schritt endet mit einem Bild, das zeigt, wie das in der Praxis aussieht

#### Story-Mode
Der Insight ist selbst die Revelation — der Leser braucht keinen Aktionsplan, sondern Zeit mit der Erkenntnis.

- Eine nahtlose Fortsetzung der Geschichte, die den Insight vertieft
- Kein Schritt-für-Schritt, stattdessen: Das Bild, das bleibt
- Am Ende eine Formulierung, die sich einbrennt — ein Satz, den der Leser sich merkt

#### Resource-Mode
Der Insight führt zu einer konkreten Empfehlung — ein Tool, Buch, System oder Workflow.

- Kurze Überleitung: Warum diese Resource?
- Die Resource konkret vorstellen: Was ist es, wie nutzt Jani es, was ändert sich dadurch?
- Conviction aufbauen, bevor der Link kommt — der Leser soll wollen, nicht nur klicken

---

### 5. CTA

Ein klarer Aufruf. Immer nur einer pro Email. Kein weicher Abschluss.

Je nach aktuellem Kontext (Q1 2026: Core Product Launch):

**Option A — Antwort auf die Email (Engagement)**
> "Schreib mir kurz: Was ist dein größter Struggle damit gerade? Ich lese jede Antwort."

**Option B — Produkt (Revenue)**
> Direkter Hinweis auf das 297€ Produkt, wenn der Insight direkt damit verbunden ist. Kein Druck-Verkauf, sondern natürliche Verlängerung des Insights: "Wenn du wissen willst, wie das konkret aussieht — [Link]."

**Option C — DM / Community**
> "Wenn dich das anspricht, schreib mir auf Instagram. Ich antworte jedem, der mir schreibt."

---

### 6. Close

Der Sign-Off. Kurz, persönlich, nach Jani.

Kein "Beste Grüße" — eher:
> "Bis nächste Woche,
> Jani"

Optional: ein letzter Satz, der die Kernaussage noch einmal anklingen lässt — nicht wiederholt, sondern schwingt aus.

---

## Nach dem Schreiben — Self-Check

Gehe durch diese Fragen, bevor du den Draft ablieferst:

**Stimme:**
- Klingt dieser Text nach Jani oder nach einem Newsletter-Template?
- Gibt es Staccato-Fragment-Listen? (Wenn ja: sofort umschreiben. "Mehr Lärm. Weniger Tiefe." ist verboten.)
- Gibt es AI-Diagnose-Sätze? ("Das ist kein X-Problem, das ist ein Y-Problem." ist verboten.)
- Gibt es Em-Dash Kontrast-Aphorismen? ("X war nicht Y — es war Z." ist verboten.)

**Struktur:**
- Öffnet der Entry Point mit einer konkreten Szene, nicht mit einem Thema?
- Kommt der Core Insight mindestens dreimal vor — in verschiedenen Formulierungen?
- Hat die Email genau einen CTA, klar und direkt?

**Inhalt:**
- Sind alle Aussagen greifbar genug, dass der Leser sie sich vorstellt?
- Werden Zahlen konkret genannt ("250 Stunden", "3 Templates", "23 Uhr") statt abstrakt ("viel Zeit", "einige Tools")?
- Hat jeder Beweis einen Mechanismus, nicht nur eine Metrik?

**Verboten in jedem Jani-Text:**
- Staccato-Fragmente als Stilelement
- AI-Diagnose-Sätze ("Das ist kein X, das ist Y")
- Em-Dash Kontrast-Aphorismen
- Corporate-Speak oder akademischer Duktus
- Einleitungen, die erklären, was gleich erklärt wird
- Abstrakte Aussagen ohne konkretes Bild dahinter

---

## Referenzen

- Jani's Schreibstil-DNA: `jani-voice` Skill (im System)
- Schreibstandards mit Vorher/Nachher: `/sessions/sharp-great-tesla/mnt/Jarvis/02 Projects/Writing Station/[C] Newsletter Writing Principles.md`
- Strategischer Kontext: `/sessions/sharp-great-tesla/mnt/Jarvis/Context/[C] Ziele 2026.md`

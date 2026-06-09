---
name: raw-cut
description: >
  Automatischer Raw Cut für Talking-Head-Videos und Vlogs. Nutze diesen Skill IMMER wenn Jani einen Raw Cut erstellen will, Stille schneiden will, Filler-Wörter entfernen will, Einatmer/Luftholen raushaben will, oder doppelt gesagte Sätze rausschneiden will. Trigger bei: "mach einen Raw Cut", "schneide das Video", "Stille raus", "Filler weg", "Einatmer raus", "nimm den letzten Take", "raw cut machen", "raw cut v2", "auto cut", "schneid das", oder wenn eine Videodatei erwähnt wird und ein Schnitt gewünscht ist. Immer diesen Skill laden bevor ein automatischer Videoschnitt gemacht wird, nie ohne diesen Skill.
---

# Raw Cut Skill

Automatischer Raw Cut für Talking-Head-Videos. Zwei Varianten:

- **v2 (Default, Recommended):** 4-Layer Architektur, deterministische Mikro-Wiederholungs-Erkennung, Einatmer-Entfernung, optionales Claude-Review. Für 14+ min Videos ohne manuelles Nacharbeiten.
- **v1 (Legacy):** einstufig, LLM-basiert mit Signalwörtern. Gut für kurze Clips, reicht nicht für lange Aufnahmen mit vielen Micro-Restarts.

---

## v2 Architektur (4 Layers)

Jede Layer liefert deterministische Schnittvorschläge. Claude kommt erst am Ende zum Review.

### Layer 1: Similarity Cuts (algorithmisch)
Splittet das Transcript an Sprechpausen > 0.4s in Phrasen. Vergleicht jede Phrase mit allen Phrasen im 45-Sekunden-Fenster nach ihr via:
- `difflib.SequenceMatcher` (char-level) mit Threshold 0.75
- Longest Common Substring (word-level) mit Threshold 0.60
- Prefix-Match mit Threshold 0.75

**Regel:** bei Match wird die frühere Phrase geschnitten, die spätere behalten. Parallelstrukturen wie "Ich bin brutal stolz. Ich bin brutal happy." werden über eine Prefix+Different-Ending Heuristik geschützt (beide bleiben).

**Fängt:**
- "entlang dieser Spirale und entlang dieser Spirale"
- "Die unterste Stufe... Die untersten drei Stufen"
- "Es geht darum zu optimieren, zu skalieren, zu gewinnen" (2x)

### Layer 1.5: Intra-Phrase Repeat Cuts (algorithmisch)
Findet nicht-adjazente Wiederholungen innerhalb einer einzigen Phrase (Wortgruppe ohne > 0.4s Pause). Layer 1 und Layer 2 übersehen diese Muster, weil Layer 1 nur Phrasen untereinander vergleicht und Layer 2 nur direkt aufeinanderfolgende n-Gramme prüft.

**Fängt:**
- "entlang dieser Spirale entwickeln und entlang dieser Spirale und entlang dieser Spirale"
- "ich nenne das ganze epistemische Feigheit, nämlich ich nenne das ganze epistemische Feigheit"
- "und damit kommen wir zu dem Punkt und damit kommen wir zu einem und damit kommen wir zu dem"

**Parallelstruktur-Schutz:** wenn zwischen zwei Occurrences <= 1 Wort liegt und dieses Wort kein Restart-Marker ist (nämlich, also, äh...), wird der Cut als Parallelstruktur eingestuft und nicht gemacht.

### Layer 2: Stutter Cuts (algorithmisch)
Direkte N-Gramm-Wiederholungen (2 bis 6 Wörter). Case-insensitive, Zeichensetzung gestrippt. Alle Vorkommen außer dem letzten werden geschnitten.

**Fängt:**
- "Und da, und da"
- "Das ist, das ist wichtig"

### Layer 3: Breath Cuts (Einatmer raus)

Zwei Modi:

**aggressive (Default):**
Findet Lücken > 0.3s vor Wortanfängen. Analysiert den Audio-Ausschnitt mit librosa STFT. Fingerprint Check: dominante Energie in 100-500 Hz vs 1-3 kHz. Ratio > 1.5 = Einatmer → entfernt. Behält 0.15s Padding vor dem ersten gesprochenen Laut.

**conservative:**
Blind Cut ohne Frequenz-Analyse. Schneidet alle Pausen > 0.3s vor Wörtern, behält 0.15s Padding. Schneller, risikoärmer, entfernt aber auch "saubere" Pausen.

**off:**
Keine Breath Cuts. Nur Standard-Stille wird entfernt.

### Layer 4: Claude Validator (optional)
Reviewt nur die Cut-Liste (nicht das ganze Transcript). Kann:
- Cuts ablehnen (False Positives wie Parallelstrukturen)
- Bis zu 5 weitere Wiederholungen nachmelden, die Layer 1 übersehen hat

**Backend Auswahl:**
- `auto` (Default): probiert `claude` CLI zuerst (Max Subscription, keine API-Kosten), fällt auf API zurück wenn CLI fehlt
- `cli`: erzwingt `claude` CLI
- `api`: erzwingt Anthropic API (nutzt `ANTHROPIC_API_KEY` aus `.env`)
- `off`: kein Validator, Skript ist rein deterministisch

---

## Ordnerstruktur

```
02 Projects/Writing Station/YouTube/
  ├── ready to edit/         ← Jani legt RAW-Footage hier rein
  │   └── processed/         ← nach dem Schnitt: Originals hierher
  └── edited/                ← fertige Raw Cuts landen hier
      └── _old/              ← Zwischenversionen
```

**Workflow für Jani:**
1. MP4 in `ready to edit/` ziehen
2. Jarvis sagen: "schneide das Video" / "raw cut v2"
3. Fertiges Video in `edited/`, Transcript daneben

**Output-Namensschema:**
- Video: `[Clipname] — Raw Cut.mp4`
- Transcript: `[Clipname] — Transcript.txt`

---

## Setup (einmalig)

```bash
# v2 Dependencies
pip install faster-whisper whisper-timestamped librosa python-dotenv --break-system-packages

# FFmpeg Check
ffmpeg -version

# Claude CLI (für kostenfreien Layer 4 via Max Subscription)
claude --version
```

**`.env` im Vault-Root:**
```
# Fallback nur wenn claude CLI fehlt
ANTHROPIC_API_KEY=sk-ant-...
```

**Wichtig:** `claude` CLI nutzt die Max Subscription → keine extra Kosten. Der API Key wird nur benutzt wenn die CLI nicht verfügbar ist.

---

## Script starten (v2)

Script liegt unter: `Skills/raw-cut/scripts/raw_cut_v2.py`

```bash
# Standard: MP4, aggressive Breath Removal, auto Validator
python3 Skills/raw-cut/scripts/raw_cut_v2.py --input "ready to edit/C0114.MP4"

# Konservative Breath Removal
python3 Skills/raw-cut/scripts/raw_cut_v2.py --input VIDEO.mp4 --breath-mode conservative

# Ohne Breath Removal
python3 Skills/raw-cut/scripts/raw_cut_v2.py --input VIDEO.mp4 --breath-mode off

# Ohne Claude Validator (rein deterministisch)
python3 Skills/raw-cut/scripts/raw_cut_v2.py --input VIDEO.mp4 --validator-backend off

# Export als FCPXML für DaVinci Resolve
python3 Skills/raw-cut/scripts/raw_cut_v2.py --input VIDEO.mp4 --output xml

# Transcript behalten
python3 Skills/raw-cut/scripts/raw_cut_v2.py --input VIDEO.mp4 --keep-transcript
```

---

## CLI Flags (v2)

| Flag | Default | Bedeutung |
|------|---------|-----------|
| `--input` | (required) | Pfad zur Videodatei |
| `--output` | `mp4` | `mp4` oder `xml` (FCPXML für Resolve) |
| `--output-path` | auto | eigener Output-Pfad |
| `--model` | `medium` | Whisper Modell (tiny/base/small/medium/large) |
| `--language` | `de` | Sprachcode |
| `--breath-mode` | `aggressive` | `aggressive` / `conservative` / `off` |
| `--validator-backend` | `auto` | `auto` / `cli` / `api` / `off` |
| `--no-preview` | false | überspringt Preview-Tabelle |
| `--keep-transcript` | false | speichert Transcript-TXT daneben |

---

## Konfiguration (Konstanten in raw_cut_v2.py)

| Konstante | Wert | Bedeutung |
|-----------|------|-----------|
| `PHRASE_SPLIT_GAP` | 0.4s | Pausenlänge um Phrasen zu splitten |
| `L1_LOOKAHEAD_WINDOW` | 45.0s | Suchfenster für Similarity |
| `L1_SM_RATIO_THRESHOLD` | 0.75 | SequenceMatcher Schwelle |
| `L1_LCS_RATIO_THRESHOLD` | 0.60 | LCS Schwelle |
| `L1_PREFIX_RATIO_THRESHOLD` | 0.75 | Prefix-Match Schwelle |
| `L1_MIN_WORDS` | 3 | Phrasen kürzer werden ignoriert |
| `L15_MIN_NGRAM` | 3 | kleinste N-Gramm-Länge für Intra-Phrase |
| `L15_MAX_NGRAM` | 8 | größte N-Gramm-Länge für Intra-Phrase |
| `L15_MIN_WORDS` | 8 | Phrasen kürzer werden nicht gescannt |
| `L2_MIN_NGRAM` | 2 | kleinste N-Gramm-Länge |
| `L2_MAX_NGRAM` | 6 | größte N-Gramm-Länge |
| `L3_MIN_SILENCE_BEFORE_WORD` | 0.3s | Mindest-Pause vor Wort für Breath-Check |
| `L3_BREATH_LOOKBACK` | 0.4s | wie weit zurück der Audio-Ausschnitt geht |
| `L3_KEEP_BEFORE_ONSET` | 0.15s | Padding vor erstem Laut |
| `L3_BREATH_FREQ_LOW` | (100, 500) Hz | Einatmer-Band |
| `L3_BREATH_FREQ_HIGH` | (1000, 3000) Hz | Speech-Band |
| `L3_BREATH_ENERGY_RATIO` | 1.5 | Low/High Ratio für Einatmer |

---

## Preview-Tabelle (v2)

Vor dem Schnitt zeigt das Skript eine gruppierte Übersicht:

```
📋 Schnittplan (v2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Layer 1 (Similarity):     12 Cuts
Layer 2 (Stutter):         4 Cuts
Layer 3 (Breath):         38 Cuts
Silence:                  17 Cuts
Filler:                    6 Cuts
Layer 4 (Claude Review):  +2 hinzugefügt, -1 abgelehnt
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Gesamt:                   78 Cuts
Original:                 14:32
Nach Cut:                  8:47 (40% kürzer)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Qualität und Grenzen (v2)

**Funktioniert sehr gut:**
- Mikro-Wiederholungen ohne Signalwörter (Layer 1, 90%+)
- Stutter / direkte Wortdopplungen (Layer 2, 95%+)
- Einatmer am Satzanfang (Layer 3 aggressive, 85%+)
- Stille & explizite Signalwörter (100%)

**Funktioniert ok:**
- Einatmer mitten im Satz ohne Pause (60%)
- Parallelstrukturen korrekt erhalten (Layer 4 fängt die meisten False Positives)

**Funktioniert nicht:**
- Zwei komplett getrennte Takes vergleichen (zu großer Zeitabstand)
- Emotionale Qualität eines Takes beurteilen
- Musik / reine B-Roll-Abschnitte bewerten

---

## v1 Workflow (Legacy, Fallback)

Falls v2 nicht verfügbar ist oder für kurze Clips:

```bash
python3 Skills/raw-cut/scripts/raw_cut.py --input VIDEO.mp4
```

v1 nutzt Whisper + Signalwort-basierte Logik. Siehe `raw_cut.py` für Details.

**Wann v1 reicht:**
- Clips unter 5 Minuten
- Jani sagt beim Drehen konsequent "nochmal" bei falschen Takes
- Keine Einatmer zu entfernen

---

## Tipps für bessere Ergebnisse

- Beim Drehen "nochmal" sagen bei falschen Takes, Layer 1 fängt das 100% zuverlässig
- Vor dem Mikro atmen, nicht direkt rein, Layer 3 aggressive fängt trotzdem die meisten
- Bei Parallelstrukturen ("Ich bin X. Ich bin Y.") den Validator nicht auf `off` stellen, der fängt False Positives

---

## Debug

**Kein Whisper gefunden:**
```bash
pip install whisper-timestamped faster-whisper --break-system-packages
```

**librosa fehlt:**
```bash
pip install librosa --break-system-packages
```

**Layer 4 schlägt fehl:**
- `claude --version` prüft CLI-Verfügbarkeit
- `ANTHROPIC_API_KEY` in `.env` prüfen
- Fallback: `--validator-backend off` nutzen, Skript läuft dann rein deterministisch

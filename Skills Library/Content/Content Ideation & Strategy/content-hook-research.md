# Hook Research Skill

Reverse-engineered viral hooks für Newsletter-Titel, Email-Subject-Lines und Content-Hooks.
Drei Quellen: YouTube (Apify), Reddit (WebSearch), Instagram/TikTok (WebSearch).
Keine erfundenen View-Zahlen — immer aus echten Daten.

## Wann triggern

Immer wenn ein Newsletter-Titel, Subject Line, Email-Hook oder Content-Hook gebraucht wird — VOR dem Schreiben. Nie Titel aus dem Kopf generieren.

## Plattform-Auswahl

**Für Email Subject Lines:** Reddit zuerst — Post-Titel sind pure Hooks, Upvotes zeigen was resoniert.
**Für Content-Hooks (Reel, YouTube, Karussell):** YouTube zuerst + Reddit.
**Vollständige Recherche:** Alle drei Plattformen parallel.

## Prozess (Schritt für Schritt)

### 1. Alle drei Plattformen gleichzeitig (parallel)

#### 1a. YouTube — Apify Scrape starten

Token liegt in: `/commands/.env` → `APIFY_TOKEN`

```bash
APIFY_TOKEN=$(grep APIFY_TOKEN /path/to/commands/.env | cut -d= -f2)

curl -s -X POST \
  "https://api.apify.com/v2/acts/streamers~youtube-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN&timeout=60" \
  -H "Content-Type: application/json" \
  -d '{
    "searchKeywords": "[THEMA] [Keyword-Variante]",
    "maxResults": 20,
    "type": "video"
  }'
```

Drei Suchen durchführen:
- `"[Kernthema] 2024 2025"` — direktes Thema
- `"I [tried/built/stopped] [Verhaltensänderung]"` — Experiment-Hooks
- `"[Zielgruppe] productivity system changed"` — Outcome-Hooks

#### 1b. Reddit — WebSearch

Suche in themenrelevanten Subreddits nach Posts mit hohen Upvotes und hoher Comment-Ratio.

Standard-Subreddits für Business/Creator-Themen:
- `r/Entrepreneur` — Business, Selbstständigkeit
- `r/productivity` — Systeme, Second Brain, Effizienz
- `r/socialmedia` — Content Creation, Wachstum
- `r/marketing` — Copywriting, Funnels
- `r/personalfinance` — Finanzen
- Topic-spezifische Subreddits je nach Thema

WebSearch-Befehl:
```
site:reddit.com/r/[Subreddit] "[Thema]" 2024 OR 2025
```
Oder direkt: `reddit [Thema] [Subreddit] viral post 2024 2025`

Outlier auf Reddit: Posts mit 1000+ Upvotes oder auffällig hoher Comment-Zahl im Verhältnis zu Upvotes (zeigt emotionale Reaktion). Post-Titel sind der Hook — Flair und Kommentare zeigen wie die Community reagiert hat.

Reddit-Spezifisch: Die präzisesten, unpoliertesten Hooks kommen oft aus Reddit. Kein Marketing-Bullshit, nur was wirklich resoniert. Auch Pain-Formulierungen aus Top-Kommentaren sind Gold für Email Copy.

#### 1c. Instagram / TikTok — WebSearch

Für Caption-Hooks und erste Sätze viraler Posts.

```
site:instagram.com "[Thema]" viral 2024 2025
```
oder WebSearch: `instagram tiktok viral "[Thema]" hook caption 2024`

Alternativ: Apify Instagram Hashtag Scraper (`apify/instagram-hashtag-scraper`) — gibt Caption, Likes, Comments zurück. Nur wenn Apify verfügbar und Scrape nötig.

Outlier auf Instagram/TikTok: Posts mit Saves >> Likes (zeigt Informationswert), hohe Comment-Ratio (zeigt emotionale Reaktion). Erste Zeile der Caption = Hook.

### 2. Ergebnisse filtern (alle Plattformen)

Aus allen Plattformen:
- YouTube: sortieren nach `viewCount`, Outlier = Videos mit deutlich mehr Views als Kanaldurchschnitt oder kleine Kanäle mit überproportionalen Views
- Reddit: sortieren nach Upvotes + Comment-Ratio, Outlier = Posts mit 1000+ Upvotes oder hoher emotionaler Reaktion
- Instagram/TikTok: Outlier = hohe Save-Rate oder hohe Comment-Ratio im Verhältnis zu Followern
- Top 10 gesamt auswählen (plattformübergreifend)

### 2b. Kopier-Strategie: Eng kopieren, nicht wischi-waschi adaptieren

**Zwei erlaubte Ansätze — kein dritter:**

**Ansatz A: Eng kopieren**
Titelstruktur 1:1 übernehmen, nur Inhalt tauschen.
- Original: "Does ChatGPT Make You Dumber?"
- Kopie: "Macht ChatGPT dich wirklich dümmer?"
Funktioniert weil: der Mechanismus ist identisch, nur lokalisiert.

**Ansatz B: Mechanismus verstehen, dann smart umbauen**
1. Warum funktioniert dieser Titel? (1 Satz: psychologischer Mechanismus)
2. Was macht er beim Leser? (Identitätsbedrohung / Neugier / Kontrast / ...)
3. Denselben Mechanismus auf Janis Thema anwenden
- Original: "ChatGPT makes you stupid" → Mechanismus: Identitätsbedrohung + "du machst das gerade"
- Rebuild: "ChatGPT macht dich dümmer — aber nicht warum du denkst" → gleiche Bedrohung + Twist der zur Auflösung zwingt

**Verboten:** Loose Adaptationen die den Mechanismus verlieren ("AI ersetzt deinen Copywriter. Nicht deinen Kopf." = eigene Idee, kein Viral-Mechanismus). Das ist kein Hook-Research, das ist Brainstorming.

---

### 3. Hook-Mechanismus extrahieren

Pro Video einen Satz: Was macht diesen Titel retention-stark?

| Mechanismus | Erkennungsmerkmal |
|---|---|
| Dream Outcome | "How I [allgemeines Wunschergebnis]" |
| Experiment | "I tried X for Y days" |
| Pattern Interrupt | "I stopped [common advice]" |
| Bold Claim | "The ONLY X you'll ever need" / "ULTIMATE" |
| Revelation | "X is a Lie" / "X killed Y" / "NOT what you think" |
| Spezifische Zahl | "$X" / "X Minuten" / "X Tools" |
| Konträr + Neugier | "[Sache] ist falsch" — Leser will Auflösung |
| Delegation Fantasy | "I built AI that does X for me" |

### 4. Output-Format (immer exakt so)

```
[Nr]. "[Originaltitel / Post-Titel / Caption]"
Quelle: [YouTube: Kanal / Reddit: r/Subreddit / Instagram: @Account] | Engagement: [Views/Upvotes/Saves] | Outlier weil: [1 Satz]
Mechanismus: "[abstrakte Hook-Formel]"
→ Jani-Adaptation: "[konkreter Vorschlag in Janis Stimme, mit seinen Details]"
```

### 5. Top 3 empfehlen

Die 3 stärksten Adaptationen fett markieren + 1-Satz-Begründung warum sie zum aktuellen Newsletter-Mining passen.

### 6. Writer entscheidet — dann Varianten

Nie selbst wählen. Richtung bestätigen lassen, dann 3 Titeloptionen in dieser Richtung ausarbeiten.

---

## Referenz-Tabelle: Bekannte Outlier (Stand: März 2026, via Apify)

| Titel | Kanal | Views | Mechanismus |
|---|---|---|---|
| "The ULTIMATE Second Brain Setup in Notion" | Thomas Frank | 1.3M | Bold Claim + ULTIMATE |
| "The most powerful AI Agent I've ever used" | Dan Martell | 670K | Superlativ + persönlich |
| "Success Is Hard Until You Build Systems Like This" | Ali Abdaal | 659K | Kontrast + Neugier |
| "7 Best AI Tools You NEED to Try" | Kevin Stratvert | 648K | Zahl + Urgency |
| "101 Ways To Use AI In Your Daily Life" | Tina Huang | 544K | Extreme Zahl |
| "I Tried AI as a Life Coach for 365 Days" | Ali Abdaal | 363K | Experiment + Zeitraum |
| "How to Build Systems (with AI) to ACTUALLY Achieve Your Goals" | Dan Martell | 253K | "ACTUALLY" + Outcome |
| "How To Use ChatGPT to Actually Change Your Life" | Jay Shetty | 224K | "Actually" + Dream |
| "Second Brains are a Lie" | Andrew Adriance | 77K | Revelation + Konträr |
| "Claude just killed ALL Note-Taking Apps" | ICOR with Tom | 65K | Extreme Behauptung + Tool-Kill |

---

## Integration

Dieser Skill wird aufgerufen in:
- `ash-newsletter-v2` → Block 2, Schritt 1 (Titel)
- Jedes Mal wenn Subject Lines, Hooks, oder Content-Titel gebraucht werden

Laut CLAUDE.md: Pflichtschritt vor jedem Titel. Niemals überspringen.

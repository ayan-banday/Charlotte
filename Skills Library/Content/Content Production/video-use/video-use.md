---
name: video-use
description: Edit any video by conversation. Transcribe, cut, color grade, generate overlay animations, burn subtitles — for talking heads, montages, tutorials, travel, interviews. No presets, no menus. Ask questions, confirm the plan, execute, iterate, persist. Production-correctness rules are hard; everything else is artistic freedom.
---

# Video Use

## Principle

1. **LLM reasons from raw transcript + on-demand visuals.** The only derived artifact that earns its keep is a packed phrase-level transcript (`takes_packed.md`). Everything else — filler tagging, retake detection, shot classification, emphasis scoring — you derive at decision time.
2. **Audio is primary, visuals follow.** Cut candidates come from speech boundaries and silence gaps. Drill into visuals only at decision points.
3. **Ask → confirm → execute → iterate → persist.** Never touch the cut until the user has confirmed the strategy in plain English.
4. **Generalize.** Do not assume what kind of video this is. Look at the material, ask the user, then edit.
5. **Artistic freedom is the default.** Every specific value, preset, font, color, duration, pitch structure, and technique in this document is a *worked example* from one proven video — not a mandate. Read them to understand what's possible and why each worked. Then make your own taste calls based on what the material actually is and what the user actually wants. **The only things you MUST do are in the Hard Rules section below.** Everything else is yours.
6. **Invent freely.** If the material calls for a technique not described here — split-screen, picture-in-picture, lower-third identity cards, reaction cuts, speed ramps, freeze frames, crossfades, match cuts, L-cuts, J-cuts, speed ramps over breath, whatever — build it. The helpers are ffmpeg and PIL. They can do anything the format supports. Do not wait for permission.
7. **Verify your own output before showing it to the user.** If you wouldn't ship it, don't present it.

## Hard Rules (production correctness — non-negotiable)

These are the things where deviation produces silent failures or broken output. They are not taste, they are correctness. Memorize them.

1. **Subtitles are applied LAST in the filter chain**, after every overlay. Otherwise overlays hide captions. Silent failure.
2. **Per-segment extract → lossless `-c copy` concat**, not single-pass filtergraph. Otherwise you double-encode every segment when overlays are added.
3. **30ms audio fades at every segment boundary** (`afade=t=in:st=0:d=0.03,afade=t=out:st={dur-0.03}:d=0.03`). Otherwise audible pops at every cut.
4. **Overlays use `setpts=PTS-STARTPTS+T/TB`** to shift the overlay's frame 0 to its window start. Otherwise you see the middle of the animation during the overlay window.
5. **Master SRT uses output-timeline offsets**: `output_time = word.start - segment_start + segment_offset`. Otherwise captions misalign after segment concat.
6. **Never cut inside a word.** Snap every cut edge to a word boundary from the Scribe transcript.
7. **Pad every cut edge.** Working window: 30–200ms. Scribe timestamps drift 50–100ms *mid-phrase* — padding absorbs that. Tighter for fast-paced, looser for cinematic.
8. **Audio-snap every segment END to actual silence.** Padding does NOT fix Scribe drift at sentence ends. When a word is followed by a pause/breath/silence, Scribe's `word.end` can overshoot the actual end-of-speech by **500–3000ms** — it packs the trailing silence into the word. Negative `POST_PAD` can't compensate (would clip mid-phrase cuts). The fix: for every segment end, probe the original audio with ffmpeg `silencedetect` in window `[word_start - 0.05, scribe_end + 0.3]` at `-42dB / duration=0.15` and snap to where audio actually drops. Never trust Scribe's `word.end` at segment boundaries. See *Audio-snap* section below for implementation.
9. **Word-level verbatim ASR only.** Never SRT/phrase mode (loses sub-second gap data). Never normalized fillers (loses editorial signal).

**9a. Phrase-sequence anchors are retake-safe and hard-fail.** When anchoring a cut to a word sequence (e.g., starting a segment at the phrase "wenn orange hört dass jobs wegfallen"), the search MUST:
  - Match in a *window* around the anchor time (e.g., `[anchor - 15s, anchor + 30s]`), not "search starting at anchor time". Retakes often begin 1–10s BEFORE the anchor (right after a "noch mal" marker).
  - Return the LAST match in the window, not the first. This auto-picks the retake when a phrase appears multiple times (abandoned take + retake).
  - Hard-fail if no match (`sys.exit(1)`), not warn-and-continue. A silently-dropped beat is invisible in the preview until the user listens and notices the missing idea. Refuse to write the EDL when any beat fails to resolve.
  - Print `Beats: N produced / M defined` so N == M is visually obvious on every run.
10. **Cache transcripts per source.** Never re-transcribe unless the source file itself changed.
11. **Parallel sub-agents for multiple animations.** Never sequential. Spawn N at once via the `Agent` tool; total wall time ≈ slowest one.
12. **Strategy confirmation before execution.** Never touch the cut until the user has approved the plain-English plan.
13. **All session outputs in `<videos_dir>/edit/`.** Never write inside the `video-use/` project directory.

Everything else in this document is a worked example. Deviate whenever the material calls for it.

## Directory layout

The skill lives in `video-use/`. User footage lives wherever they put it. All session outputs go into `<videos_dir>/edit/`.

```
<videos_dir>/
├── <source files, untouched>
└── edit/
    ├── project.md               ← memory; appended every session
    ├── takes_packed.md          ← phrase-level transcripts, the LLM's primary reading view
    ├── edl.json                 ← cut decisions
    ├── transcripts/<name>.json  ← cached raw Scribe JSON
    ├── animations/slot_<id>/    ← per-animation source + render + reasoning
    ├── clips_graded/            ← per-segment extracts with grade + fades
    ├── master.srt               ← output-timeline subtitles
    ├── downloads/               ← yt-dlp outputs
    ├── verify/                  ← debug frames / timeline PNGs
    ├── preview.mp4
    └── final.mp4
```

## Setup

- `ELEVENLABS_API_KEY` in `.env` at project root or env. Ask and write `.env` if missing.
- `ffmpeg` + `ffprobe` on PATH.
- Python deps: `pip install -e .`.
- `yt-dlp`, `manim`, Remotion installed only on first use.
- This skill vendors `skills/manim-video/`. Read its SKILL.md when building a Manim slot.

## Helpers

- **`transcribe.py <video>`** — single-file Scribe call. `--num-speakers N` optional. Cached.
- **`transcribe_batch.py <videos_dir>`** — 4-worker parallel transcription. Use for multi-take.
- **`pack_transcripts.py --edit-dir <dir>`** — `transcripts/*.json` → `takes_packed.md` (phrase-level, break on silence ≥ 0.5s).
- **`timeline_view.py <video> <start> <end>`** — filmstrip + waveform PNG. On-demand visual drill-down. **Not a scan tool** — use it at decision points, not constantly.
- **`render.py <edl.json> -o <out>`** — per-segment extract → concat → overlays (PTS-shifted) → subtitles LAST. `--preview` for 720p fast. `--build-subtitles` to generate master.srt inline.
- **`grade.py <in> -o <out>`** — ffmpeg filter chain grade. Presets + `--filter '<raw>'` for custom.

For animations, create `<edit>/animations/slot_<id>/` with `Bash` and spawn a sub-agent via the `Agent` tool.

## The process

1. **Inventory.** `ffprobe` every source. `transcribe_batch.py` on the directory. `pack_transcripts.py` to produce `takes_packed.md`. Sample one or two `timeline_view`s for a visual first impression.
2. **Pre-scan for problems.** One pass over `takes_packed.md` to note verbal slips, obvious mis-speaks, or phrasings to avoid. Plain list, feed into the editor brief.
3. **Converse.** Describe what you see in plain English. Ask questions *shaped by the material*. Collect: content type, target length/aspect, aesthetic/brand direction, pacing feel, must-preserve moments, must-cut moments, animation and grade preferences, subtitle needs. Do not use a fixed checklist — the right questions are different every time.
4. **Propose strategy.** 4–8 sentences: shape, take choices, cut direction, animation plan, grade direction, subtitle style, length estimate. **Wait for confirmation.**
5. **Execute.** Produce `edl.json` via the editor sub-agent brief. Drill into `timeline_view` at ambiguous moments. Build animations in parallel sub-agents. Apply grade per-segment. Compose via `render.py`.
6. **Preview.** `render.py --preview`.
7. **Self-eval (before showing the user).** Run `timeline_view` on the **rendered output** (not the sources) at every cut boundary (±1.5s window). Check each image for:
   - Visual discontinuity / flash / jump at the cut
   - Waveform spike at the boundary (audio pop that slipped past the 30ms fade)
   - Subtitle hidden behind an overlay (Rule 1 violation)
   - Overlay misaligned or showing wrong frames (Rule 4 violation)

   Also sample: first 2s, last 2s, and 2–3 mid-points — check grade consistency, subtitle readability, overall coherence. Run `ffprobe` on the output to verify duration matches the EDL expectation.

   If anything fails: fix → re-render → re-eval. **Cap at 3 self-eval passes** — if issues remain after 3, flag them to the user rather than looping forever. Only present the preview once the self-eval passes.
8. **Iterate + persist.** Natural-language feedback, re-plan, re-render. Never re-transcribe. Final render on confirmation. Append to `project.md`.

## Cut craft (techniques)

- **Audio-first.** Candidate cuts from word boundaries and silence gaps.
- **Preserve peaks.** Laughs, punchlines, emphasis beats. Extend past punchlines to include reactions — the laugh IS the beat.
- **Speaker handoffs** benefit from air between utterances. Common values: 400–600ms. Less for fast-paced, more for cinematic. Taste call.
- **Audio events as signals.** `(laughs)`, `(sighs)`, `(applause)` mark beats. Extend past them.
- **Silence gaps are cut candidates.** Silences ≥400ms are usually the cleanest. 150–400ms phrase boundaries are usable with a visual check. <150ms is unsafe (mid-phrase).
- **Example cut padding** (the launch video shipped with this): 50ms before the first kept word, 80ms after the last. Tighter for montage energy, looser for documentary. Stay in the 30–200ms working window (Hard Rule 7).
- **At sentence ends**, padding alone is insufficient — see *Audio-snap* section. Apply `snap_to_silence` before `POST_PAD`, then `POST_PAD` becomes a clean 0–20ms micro-buffer on top of actual speech-end, not a drift-compensator.
- **Never reason audio and video independently.** Every cut must work on both tracks.

## Audio-snap at segment ends (Hard Rule 8 implementation)

**The problem.** ElevenLabs Scribe reports `word.end` based on when it stops being confident the word is ongoing, not when speech actually stops. When a word is followed by silence or breath, Scribe packs the trailing quiet into the word's duration. Typical overshoot:

- Mid-sentence word (next word starts soon): 50–100ms. Padding absorbs it.
- Sentence-end word before a pause: 500–1500ms. Common.
- Word before a long beat/breath/thinking pause: 2000–4000ms. Happens on hooks and transitions.

Negative `POST_PAD` can't fix this — the overshoot is variable, and any value large enough to catch the 2-second cases clips the mid-sentence cases mid-word.

**The fix.** For every segment end, ignore Scribe's `word.end` and re-derive it from the audio. Probe the original source with ffmpeg `silencedetect` in a tight window around Scribe's claim. The first silence within the window is the real end-of-speech.

**Reference implementation** (drop into `build_edl.py`):

```python
import re, subprocess

_silence_re = re.compile(r"silence_start:\s*([\d.]+)")
_snap_cache: dict[tuple[float, float], float] = {}

def snap_to_silence(word_start: float, scribe_end: float,
                    source_path: str, threshold_db: int = -42) -> float:
    """Return actual end-of-speech for a segment ending at scribe_end.

    Probes audio in [word_start - 0.05, max(scribe_end + 0.3, word_start + 0.8)]
    and returns the first silence_start found. Falls back to scribe_end if none.
    """
    key = (round(word_start, 3), round(scribe_end, 3))
    if key in _snap_cache:
        return _snap_cache[key]

    probe_start = max(0.0, word_start - 0.05)
    probe_end = max(scribe_end + 0.3, word_start + 0.8)
    duration = probe_end - probe_start

    cmd = [
        "ffmpeg", "-nostdin", "-hide_banner", "-loglevel", "info",
        "-ss", f"{probe_start:.3f}", "-i", source_path, "-t", f"{duration:.3f}",
        "-af", f"silencedetect=noise={threshold_db}dB:duration=0.15",
        "-f", "null", "-",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)

    snapped = scribe_end
    for line in result.stderr.splitlines():
        m = _silence_re.search(line)
        if not m:
            continue
        abs_t = probe_start + float(m.group(1))
        if abs_t < word_start + 0.1:
            continue  # ignore silence that starts before the word speaks
        snapped = abs_t
        break

    _snap_cache[key] = snapped
    return snapped
```

**Tuning knobs.**
- `threshold_db=-42`: sensitive enough to catch quiet tails, tolerant enough to let word decays complete. Raise to `-38` if cuts feel too tight; lower to `-46` if cuts hang.
- `duration=0.15`: 150ms minimum silence. Shorter values (`0.05`) catch micro-pauses between syllables → cuts mid-word. Longer values (`0.3`) miss short pauses and fall back to Scribe.
- The `abs_t < word_start + 0.1` guard prevents snapping to silence that exists *before* the word (edge case when `word_start` is slightly pessimistic).

**When to use this.** Every segment end in a talking-head cut. It adds ~0.5s per probe, so 135 segments ≈ 60–90s per EDL build. Cache the results per `(word_start, scribe_end)` pair — re-runs are instant.

**When NOT to use this.** Fast-paced montage where segments butt-join mid-phrase (next segment starts talking before silence). For those, Scribe's `word.end` + small post-pad is fine; silence never comes.

**Verification.** Log `drift = scribe_end - snapped_end` during the build. Drifts > 150ms are normal at sentence ends. Drifts > 1000ms are common at hooks/transitions. If drifts are all < 50ms, the threshold is too strict (falling back to Scribe); if drifts are clipping words, threshold is too loose.

## Retake-safe phrase search (Hard Rule 9a implementation)

**The problem.** When a speaker does multiple takes of the same sentence (e.g., abandoned take → "noch mal" → final take), the transcript contains both. The EDL needs to anchor segment starts/ends to word sequences in the transcript. Two things go wrong with a naive "find first match at or after anchor time" approach:

1. **Retakes start before the anchor.** If you set the anchor at your intended cut point (just after "noch mal"), the retake's first word is usually within 100–500ms of the anchor — and often *before* it. A forward-only search returns -1, beat drops silently.
2. **First match may be the abandoned take.** If the anchor is loose and both takes fall within the search range, returning the first gives you the abandoned version.

**The fix.** Search in a *window* around the anchor, return the LAST match. For typical retake structures (`abandoned → noch mal → final`, within 5–10s), window `[anchor - 15s, anchor + 30s]` + `prefer="last"` always picks the final take. For phrases with one occurrence, same result. No special-casing needed at the KEEPS level.

**Reference implementation:**

```python
def find_phrase_sequence(seq, search_start=0, search_end=None, prefer="last"):
    """Return index of first word of a matched phrase sequence.

    prefer="last":  return LAST match in window — retake-safe.
    prefer="first": return first match (legacy; rarely what you want).
    Returns -1 if no match.
    """
    if search_end is None:
        search_end = len(words)
    seq_len = len(seq)
    matches = []
    for i in range(search_start, search_end - seq_len + 1):
        if all(
            (words[i + j].get("text") or "").strip().lower().strip(".,!?:;\"„""'") == t
            for j, t in enumerate(seq)
        ):
            matches.append(i)
            if prefer == "first":
                return i
    if not matches:
        return -1
    return matches[-1] if prefer == "last" else matches[0]


SEQ_PRE_WINDOW = 15.0   # retakes often precede the anchor
SEQ_POST_WINDOW = 30.0  # anchor may estimate before phrase actually starts

def _windowed_bounds(anchor_time):
    s = find_word_after_time(anchor_time - SEQ_PRE_WINDOW) or 0
    e = find_word_after_time(anchor_time + SEQ_POST_WINDOW) or len(words)
    return s, e
```

**Hard-fail on missing beats.** After resolving all KEEPS entries, check if any failed:

```python
if failed_beats:
    print(f"BUILD FAILED — {len(failed_beats)} unresolved:")
    for beat, err in failed_beats:
        print(f"    {beat}: {err}")
    sys.exit(1)  # do NOT write partial EDL
print(f"Beats: {len(ranges)} produced / {len(KEEPS)} defined")
```

Silent beat-drops are the worst failure mode — they're invisible until the viewer notices a missing idea in the preview. Refuse to write the EDL on any failure; print the `N/M` counter on every run so mismatches are visually unmissable.

## Internal-silence splitting (Scribe mega-word collapse)

**The problem.** Scribe occasionally collapses a long pause between two spoken parts into a single "word" token spanning many seconds — e.g., a speaker says "habe" then pauses 12 seconds to think, then says "Und". Scribe transcribes this as `habeUnd` with `start=1100.3, end=1112.1`. No spacing, no audio_event, no second token — one word with a 12s duration.

Your segment spec spans this whole region as a single range. `snap_to_silence` only runs at the segment END, so the 12 seconds of internal silence stays in the output. Viewers hear: first sentence → dead air for 12s → second sentence. Catastrophic.

**The fix.** After resolving each KEEPS entry to `[s_pad, e_pad]`, probe the segment's internal audio with `silencedetect` at `-42dB / duration=1.5s`. Each silence found = an implicit cut: segment ends at `silence_start`, resumes at `silence_end`. Produces N+1 sub-ranges per KEEP (label them `BEAT_A`, `BEAT_B`, etc.). The 12s of dead air is gone.

**Discard noise-only sub-segments.** Between two nearby silences, there may be a short region of below-speech audio (breath, lip smack, throat clear) — loud enough to not be "silent" but not speech. If a sub-segment contains *zero* Scribe `word` tokens, drop it entirely. This prevents a 2-second breath fragment from becoming a sub-segment.

**Reference implementation:**

```python
def detect_internal_silences(src_start, src_end, min_silence_s=1.5, threshold_db=-42):
    """Return [(abs_silence_start, abs_silence_end), ...] inside [src_start, src_end]."""
    duration = src_end - src_start
    if duration < min_silence_s + 0.5:
        return []
    cmd = [
        "ffmpeg", "-nostdin", "-hide_banner", "-loglevel", "info",
        "-ss", f"{src_start:.3f}", "-i", str(SOURCE), "-t", f"{duration:.3f}",
        "-af", f"silencedetect=noise={threshold_db}dB:duration={min_silence_s}",
        "-f", "null", "-",
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    silences, cur = [], None
    for line in r.stderr.splitlines():
        m = re.search(r"silence_start:\s*([\d.]+)", line)
        if m:
            cur = src_start + float(m.group(1))
            continue
        m = re.search(r"silence_end:\s*([\d.]+)", line)
        if m and cur is not None:
            end_t = src_start + float(m.group(1))
            # Ignore silences at the very start/end (handled elsewhere).
            if cur > src_start + 0.3 and end_t < src_end - 0.3:
                silences.append((cur, end_t))
            cur = None
    return silences

# In the main loop, after resolving [s_pad, e_pad]:
pauses = detect_internal_silences(s_pad, e_pad)
sub_starts = [s_pad] + [e for _, e in pauses]
sub_ends = [s for s, _ in pauses] + [e_pad]
for i, (ss, se) in enumerate(zip(sub_starts, sub_ends)):
    if se - ss <= 0.2:
        continue
    if not any(w.get("type") == "word" and ss <= w.get("start", 0) < se
               for w in words):
        continue  # noise-only sub-segment, drop
    label = beat if len(sub_starts) == 1 else f"{beat}_{chr(ord('A') + i)}"
    ranges.append({"source": ..., "start": ss, "end": se, "beat": label, ...})
```

**Limitation.** This fix catches mega-words caused by *actual silence* (breath, thinking pauses, dead air). It does NOT catch mega-words caused by *continuous non-speech audio* — e.g., a clip insert (a TV show playing), music, or ambient sound. Scribe tags those as a single stretched word too, but silencedetect finds no silence so there's nothing to split.

**Mega-word safety check (mandatory before writing EDL).** After building ranges, scan every kept segment for single Scribe `word` tokens with duration > 3s. For each, check if `detect_internal_silences` finds anything inside. If not — clip insert, music, or Scribe miss — print a loud warning naming the beat, source time, and word text. Auto-split can't handle these; the user must listen and decide per case. Example output:

```
⚠️  MEGA-WORD CHECK — 2 region(s) with >3s Scribe word and NO detectable silence.
    Likely clip insert, music, or missed speech. Auto-split cannot handle these.
    Listen to each region and decide:
    • Keep as-is (intentional insert) → no action
    • Cut out → override the KEEP entry with tighter ('time', X.XX) bounds
    ZWEI_WOCHEN                  source 1042.00-1051.44 ( 9.4s)  text='Lanz'
    BLAU_ORANGE                  source 1570.36-1573.66 ( 3.3s)  text='orangene'
```

```python
mega_word_warnings = []
for r in ranges:
    for w in words:
        if w.get("type") != "word":
            continue
        w_start, w_end = w.get("start", 0), w.get("end", 0)
        if (w_end - w_start) > 3.0 and r["start"] <= w_start and w_end <= r["end"]:
            if not detect_internal_silences(w_start, w_end, min_silence_s=0.5):
                mega_word_warnings.append((r["beat"], w.get("text", ""), w_start, w_end))

if mega_word_warnings:
    print("⚠️  MEGA-WORD CHECK — ...")
    for beat, text, s, e in mega_word_warnings:
        print(f"    {beat}  source {s:.2f}-{e:.2f}  text={text!r}")
```

Never skip this check. It's cheap (one silencedetect pass per mega-word) and catches the last class of silent failures: audio that passes all automated rules but sounds wrong.

## The packed transcript (primary reading view)

`pack_transcripts.py` reads all `transcripts/*.json` and produces one markdown file where each take is a list of phrase-level lines, each prefixed with its `[start-end]` time range. Phrases break on any silence ≥ 0.5s OR speaker change. This is the artifact the editor sub-agent reads to pick cuts — it gives word-boundary precision from text alone at 1/10 the tokens of raw JSON.

Example line:
```
## C0103  (duration: 43.0s, 8 phrases)
  [002.52-005.36] S0 Ninety percent of what a web agent does is completely wasted.
  [006.08-006.74] S0 We fixed this.
```

## Editor sub-agent brief (for multi-take selection)

When the task is "pick the best take of each beat across many clips," spawn a dedicated sub-agent with a brief shaped like this. The structure is load-bearing; the pitch-shape example is not.

```
You are editing a <type> video. Pick the best take of each beat and 
assemble them chronologically by beat, not by source clip order.

INPUTS:
  - takes_packed.md (time-annotated phrase-level transcripts of all takes)
  - Product/narrative context: <2 sentences from the user>
  - Speaker(s): <name, role, delivery style note>
  - Expected structure: <pick an archetype or invent one>
  - Verbal slips to avoid: <list from the pre-scan pass>
  - Target runtime: <seconds>

Common structural archetypes (pick, adapt, or invent):
  - Tech launch / demo:   HOOK → PROBLEM → SOLUTION → BENEFIT → EXAMPLE → CTA
  - Tutorial:             INTRO → SETUP → STEPS → GOTCHAS → RECAP
  - Interview:            (QUESTION → ANSWER → FOLLOWUP) repeat
  - Travel / event:       ARRIVAL → HIGHLIGHTS → QUIET MOMENTS → DEPARTURE
  - Documentary:          THESIS → EVIDENCE → COUNTERPOINT → CONCLUSION
  - Music / performance:  INTRO → VERSE → CHORUS → BRIDGE → OUTRO
  - Or invent your own.

RULES:
  - Start/end times must fall on word boundaries from the transcript.
  - Pad cut boundaries (working window 30–200ms).
  - Prefer silences ≥ 400ms as cut targets.
  - Unavoidable slips are kept if no better take exists. Note them in "reason".
  - If over budget, revise: drop a beat or trim tails. Report total and self-correct.

OUTPUT (JSON array, no prose):
  [{"source": "C0103", "start": 2.42, "end": 6.85, "beat": "HOOK",
    "quote": "...", "reason": "..."}, ...]

Return the final EDL and a one-line total runtime check.
```

## Color grade (when requested)

Your job is to **reason about the image**, not apply a preset. Look at a frame (via `timeline_view`), decide what's wrong, adjust one thing, look again.

Mental model is ASC CDL. Per channel: `out = (in * slope + offset) ** power`, then global saturation. `slope` → highlights, `offset` → shadows, `power` → midtones.

**Example filter chains** (`grade.py` has `--list-presets`; use them as starting points or mix your own):

- **`warm_cinematic`** — retro/technical, subtle teal/orange split, desaturated. Shipped in a real launch video. Safe for talking heads.
- **`neutral_punch`** — minimal corrective: contrast bump + gentle S-curve. No hue shifts.
- **`none`** — straight copy. Default when the user hasn't asked.

For anything else — portraiture, nature, product, music video, documentary — invent your own chain. `grade.py --filter '<raw ffmpeg>'` accepts any filter string.

Hard rules: apply **per-segment during extraction** (not post-concat, which re-encodes twice). Never go aggressive without testing skin tones.

## Subtitles (when requested)

Subtitles have three dimensions worth reasoning about: **chunking** (1/2/3/sentence per line), **case** (UPPER/Title/Natural), and **placement** (margin from bottom). The right combo depends on content.

**Worked styles** — pick, adapt, or invent:

**`bold-overlay`** — short-form tech launch, fast-paced social. 2-word chunks, UPPERCASE, break on punctuation, Helvetica 18 Bold, white-on-outline, `MarginV=35`. `render.py` ships with this as `SUB_FORCE_STYLE`.

```
FontName=Helvetica,FontSize=18,Bold=1,
PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BackColour=&H00000000,
BorderStyle=1,Outline=2,Shadow=0,
Alignment=2,MarginV=35
```

**`natural-sentence`** (if you invent this mode) — narrative, documentary, education. 4–7 word chunks, sentence case, break on natural pauses, `MarginV=60–80`, larger font for readability, slightly wider max-width. No shipped force_style — design one if you need it.

Invent a third style if neither fits. Hard rules: subtitles LAST (Rule 1), output-timeline offsets (Rule 5).

## Animations (when requested)

Animations match the content and the brand. **Get the palette, font, and visual language from the conversation** — never assume a default. If the user hasn't told you, propose a palette in the strategy phase and wait for confirmation before building anything.

**Tool options:**

- **PIL + PNG sequence + ffmpeg** — simple overlay cards: counters, typewriter text, single bar reveals, progressive draws. Fast to iterate, any aesthetic you want. The launch video used this.
- **Manim** — formal diagrams, state machines, equation derivations, graph morphs. Read `skills/manim-video/SKILL.md` and its references for depth.
- **Remotion** — typography-heavy, brand-aligned, web-adjacent layouts. React/CSS-based.

None is mandatory. Invent hybrids if useful (e.g., PIL background with a Remotion layer on top).

**Duration rules of thumb, context-dependent:**

- **Sync-to-narration explanations.** A viewer needs to parse the content at 1×. Rough floor 3s, typical 5–7s for simple cards, 8–14s for complex diagrams. The launch video shipped at 5–7s per simple card.
- **Beat-synced accents** (music video, fast montage). 0.5–2s is fine — they're visual accents, not information. The "readable at 1×" rule becomes *"recognizable at 1×"*, not *"fully parseable."*
- **Hold the final frame ≥ 1s** before the cut (universal).
- **Over voiceover:** total duration ≥ `narration_length + 1s` (universal).
- **Never parallel-reveal independent elements** — the eye can't track two new things at once. One thing, pause, next thing.

**Animation payoff timing (rule for sync-to-narration):** get the payoff word's timestamp. Start the overlay `reveal_duration` seconds earlier so the landing frame coincides with the spoken payoff word. Without this sync the animation feels disconnected.

**Easing** (universal — never `linear`, it looks robotic):

```python
def ease_out_cubic(t):    return 1 - (1 - t) ** 3
def ease_in_out_cubic(t):
    if t < 0.5: return 4 * t ** 3
    return 1 - (-2 * t + 2) ** 3 / 2
```

`ease_out_cubic` for single reveals (slow landing). `ease_in_out_cubic` for continuous draws.

**Typing text anchor trick:** center on the FULL string's width, not the partial-string width — otherwise text slides left during reveal.

**Example palette** (the launch video — one aesthetic among infinite):
- Background `(10, 10, 10)` near-black
- Accent `#FF5A00` / `(255, 90, 0)` orange
- Labels `(110, 110, 110)` dim gray
- Font: Menlo Bold at `/System/Library/Fonts/Menlo.ttc` (index 1)
- ≤ 2 accent colors, ~40% empty space, minimal chrome
- Result: terminal / retro tech feel

This is one style. If the brand is warm and serif, use that. If it's colorful and playful, use that. If the user handed you a style guide, follow it. If they didn't, propose one and confirm.

**Parallel sub-agent brief** — each animation is one sub-agent spawned via the `Agent` tool. Each prompt is self-contained (sub-agents have no parent context). Include:

1. One-sentence goal: *"Build ONE animation: [spec]. Nothing else."*
2. Absolute output path (`<edit>/animations/slot_<id>/render.mp4`)
3. Exact technical spec: resolution, fps, codec, pix_fmt, CRF, duration
4. Style palette as concrete values (RGB tuples, hex, or reference to a design system)
5. Font path with index
6. Frame-by-frame timeline (what happens when, with easing)
7. Anti-list ("no chrome, no extras, no titles unless specified")
8. Code pattern reference (copy helpers inline, don't import across slots)
9. Deliverable checklist (script, render, verify duration via ffprobe, report)
10. **"Do not ask questions. If anything is ambiguous, pick the most obvious interpretation and proceed."**

One sub-agent = one file (unique filenames, parallel agents don't overwrite each other).

## Output spec

Match the source unless the user asked for something specific. Common targets: `1920×1080@24` cinematic, `1920×1080@30` screen content, `1080×1920@30` vertical social, `3840×2160@24` 4K cinema, `1080×1080@30` square. `render.py` defaults the scale to 1080p from any source; pass `--filter` or edit the extract command for other targets. Worth asking the user which delivery format matters.

## EDL format

```json
{
  "version": 1,
  "sources": {"C0103": "/abs/path/C0103.MP4", "C0108": "/abs/path/C0108.MP4"},
  "ranges": [
    {"source": "C0103", "start": 2.42, "end": 6.85,
     "beat": "HOOK", "quote": "...", "reason": "Cleanest delivery, stops before slip at 38.46."},
    {"source": "C0108", "start": 14.30, "end": 28.90,
     "beat": "SOLUTION", "quote": "...", "reason": "Only take without the false start."}
  ],
  "grade": "warm_cinematic",
  "overlays": [
    {"file": "edit/animations/slot_1/render.mp4", "start_in_output": 0.0, "duration": 5.0}
  ],
  "subtitles": "edit/master.srt",
  "total_duration_s": 87.4
}
```

`grade` is a preset name or raw ffmpeg filter. `overlays` are rendered animation clips. `subtitles` is optional and applied LAST.

## Memory — `project.md`

Append one section per session at `<edit>/project.md`:

```markdown
## Session N — YYYY-MM-DD

**Strategy:** one paragraph describing the approach
**Decisions:** take choices, cuts, grades, animations + why
**Reasoning log:** one-line rationale for non-obvious decisions
**Outstanding:** deferred items
```

On startup, read `project.md` if it exists and summarize the last session in one sentence before asking whether to continue.

## Anti-patterns

Things that consistently fail regardless of style:

- **Hierarchical pre-computed codec formats** with USABILITY / tone tags / shot layers. Over-engineering. Derive from the transcript at decision time.
- **Hand-tuned moment-scoring functions.** The LLM picks better than any heuristic you'll write.
- **Whisper SRT / phrase-level output.** Loses sub-second gap data. Always word-level verbatim.
- **Running Whisper locally on CPU.** Slow and it normalizes fillers. Use hosted Scribe.
- **Burning subtitles into base before compositing overlays.** Overlays hide them. (Hard Rule 1.)
- **Single-pass filtergraph when you have overlays.** Double re-encodes. Use per-segment extract → concat.
- **Linear animation easing.** Looks robotic. Always cubic.
- **Hard audio cuts at segment boundaries.** Audible pops. (Hard Rule 3.)
- **Typing text centered on the partial string.** Text slides left as it grows.
- **Sequential sub-agents for multiple animations.** Always parallel.
- **Editing before confirming the strategy.** Never.
- **Re-transcribing cached sources.** Immutable outputs of immutable inputs.
- **Assuming what kind of video it is.** Look first, ask second, edit last.
- **Trusting Scribe's `word.end` at segment boundaries.** Overshoot is 500–3000ms when followed by silence. Audio-snap every segment end (Hard Rule 8).
- **Fixing late cuts with negative `POST_PAD`.** Works for mid-phrase drift (50–100ms), fails for sentence-end drift (500–3000ms). Use audio-snap instead — a global pad can't distinguish the two.
- **Narrow `from_time`-anchored phrase searches ("start at time X, find next match").** Use a *window* around a rough anchor time instead (±15s pre, +30s post) and return the LAST match. Reasons: (a) retakes often start BEFORE the anchor when the anchor estimates the intended cut point after a "noch mal" marker — a forward-only search misses them; (b) anchor estimates drift as the KEEPS list evolves. Window + last-match is retake-safe by construction.
- **Warn-and-continue on sequence lookup failure.** `!!!` / "sequence not found" must be `sys.exit(1)`, not a printed warning with a saved EDL. Silently-dropped beats are invisible in the preview until the user listens and catches a conceptual gap — a bad failure mode. Always print `Beats: N produced / M defined` at the end of the build so mismatches are unmissable.
- **Trusting that a single Scribe word token = a single spoken word.** When a speaker pauses 5+ seconds mid-sentence, Scribe often glues the pre-pause word and post-pause word into one token (e.g., `habeUnd`) with a duration spanning the pause. The segment stays correct on paper (word boundaries exist) but contains dead air in the output. Always run `detect_internal_silences` on every segment.
- **Skipping the mega-word safety check.** `detect_internal_silences` only fixes pauses with actual silence. When Scribe glues a word to 9s of continuous non-speech audio (clip insert, music, missed speech), silencedetect finds nothing and the garbage stays in. Always scan ranges for Scribe tokens >3s with no internal silence and flag them loudly before rendering — the user must listen and decide per case.

#!/usr/bin/env python3
"""
Raw Cut Script v2 — Jarvis
- Word-level timestamps für präzises Schneiden
- Räuspern/Luftholen zwischen Wörtern raus
- Wiederholungen/Neustarts erkennen
- Stille schneiden
"""

import subprocess
import json
import re
from pathlib import Path
from difflib import SequenceMatcher

# === CONFIG ===
INPUT_FILES = [
    "/sessions/confident-loving-fermi/mnt/Jarvis/02 Projects/Writing Station/YouTube/02 ready to edit/Spiral Dynamics YouTube Video/C0114.MP4"
]  # leer = auto-scan von READY_TO_EDIT_DIR
READY_TO_EDIT_DIR = Path("/sessions/confident-loving-fermi/mnt/Jarvis/02 Projects/Writing Station/YouTube/02 ready to edit")
OUTPUT_DIR = Path("/sessions/confident-loving-fermi/mnt/Jarvis/02 Projects/Writing Station/YouTube/03 edited")
WORK_DIR = Path("/sessions/confident-loving-fermi/raw_cut_work")

SILENCE_DB = -38          # dB threshold für Stille
MIN_SILENCE = 0.5         # Sekunden Mindeststille — höher = weniger mini-cuts
SPEECH_PAD_START = 0.08   # Padding vor erstem Wort
SPEECH_PAD_END = 0.2      # Padding nach letztem Wort — etwas mehr für natürlichere Übergänge
MAX_INTER_WORD_GAP = 1.0  # Lücken zwischen Wörtern > 1s = Räuspern/Luftholen
                           # (0.4s war zu aggressiv — schnitt normale Satzpausen)
MIN_SEGMENT_DURATION = 1.5 # Segmente kürzer als X Sekunden werden verworfen (kein Mini-Clip)
INTRO_MIN_DURATION = 2.0  # Erstes Segment unter X Sekunden = Fragment am Anfang → raus
WHISPER_MODEL = "small"
LANGUAGE = "de"
REPEAT_SIMILARITY = 0.60  # Ähnlichkeits-Schwelle — niedriger = auch Teilwiederholungen erwischen

WORK_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)


def extract_audio(video_path, audio_path):
    print(f"\n🎵 Audio extrahieren...")
    subprocess.run([
        "ffmpeg", "-y", "-i", str(video_path),
        "-ac", "1", "-ar", "16000", "-vn", str(audio_path)
    ], capture_output=True)


def transcribe_with_words(audio_path):
    """Transkription mit Word-Level Timestamps."""
    print(f"\n📝 Transkription mit Word-Level Timestamps...")
    from faster_whisper import WhisperModel
    model = WhisperModel(WHISPER_MODEL, device="cpu", compute_type="int8")
    segments, info = model.transcribe(
        str(audio_path),
        language=LANGUAGE,
        beam_size=5,
        word_timestamps=True
    )

    all_words = []
    all_segments = []

    for seg in segments:
        seg_words = []
        if seg.words:
            for word in seg.words:
                seg_words.append({
                    "word": word.word.strip(),
                    "start": word.start,
                    "end": word.end
                })
                all_words.append({
                    "word": word.word.strip(),
                    "start": word.start,
                    "end": word.end
                })
        all_segments.append({
            "start": seg.start,
            "end": seg.end,
            "text": seg.text.strip(),
            "words": seg_words
        })

    print(f"  → {len(all_words)} Wörter, {len(all_segments)} Segmente")
    return all_words, all_segments


def detect_repeats(segments):
    """Findet wiederholte Sätze/Takes — letzten behalten."""
    print(f"\n🔄 Wiederholungs-Erkennung...")
    cuts = []  # (start, end) die raus sollen

    texts = [s["text"] for s in segments]
    n = len(segments)

    i = 0
    while i < n:
        best_match_end = None
        best_match_similarity = 0

        # Suche ob Segment i nochmal vorkommt danach (innerhalb 5 Minuten)
        for j in range(i + 1, min(i + 20, n)):
            sim = SequenceMatcher(None, texts[i].lower(), texts[j].lower()).ratio()
            if sim >= REPEAT_SIMILARITY:
                # Prüfe ob die Folgesegmente auch ähnlich sind
                chain_sim = sim
                for k in range(1, 4):
                    if i + k < n and j + k < n:
                        s2 = SequenceMatcher(None, texts[i+k].lower(), texts[j+k].lower()).ratio()
                        chain_sim = (chain_sim + s2) / 2
                if chain_sim > best_match_similarity:
                    best_match_similarity = chain_sim
                    best_match_end = j

        if best_match_end is not None:
            # Cut: alles von Segment i bis Start von best_match_end raus
            cut_start = segments[i]["start"]
            cut_end = segments[best_match_end]["start"]
            cuts.append((cut_start, cut_end))
            print(f"  ✂️  Wiederholung: {cut_start:.1f}s–{cut_end:.1f}s ({cut_end-cut_start:.1f}s)")
            print(f"      '{texts[i][:60]}...'")
            i = best_match_end  # springe zum letzten Take
        else:
            i += 1

    return cuts


def words_to_speech_segments(words, duration):
    """
    Baut Keep-Segmente aus Word-Timestamps.
    Nur Lücken > MAX_INTER_WORD_GAP (1.0s) werden geschnitten —
    das sind echte Räuspern/Luftholen-Pausen, keine normalen Satzpausen.
    Kurze Segmente (< MIN_SEGMENT_DURATION) werden herausgefiltert.
    Das allererste Segment wird auf Fragment-am-Anfang geprüft.
    """
    if not words:
        return []

    raw_segments = []
    current_start = max(0, words[0]["start"] - SPEECH_PAD_START)
    current_end = words[0]["end"] + SPEECH_PAD_END

    for i in range(1, len(words)):
        prev_end = words[i-1]["end"]
        next_start = words[i]["start"]
        gap = next_start - prev_end

        if gap > MAX_INTER_WORD_GAP:
            raw_segments.append((current_start, current_end))
            current_start = next_start - SPEECH_PAD_START
            current_end = words[i]["end"] + SPEECH_PAD_END
        else:
            current_end = words[i]["end"] + SPEECH_PAD_END

    raw_segments.append((current_start, min(current_end, duration)))

    # Fragment am Anfang entfernen: erstes Segment zu kurz = unvollständiger Take
    if raw_segments and (raw_segments[0][1] - raw_segments[0][0]) < INTRO_MIN_DURATION:
        print(f"  ✂️  Anfangs-Fragment entfernt: {raw_segments[0][0]:.1f}s–{raw_segments[0][1]:.1f}s")
        raw_segments = raw_segments[1:]

    # Zu kurze Segmente herausfiltern (Mini-Clips vermeiden)
    segments = []
    for s, e in raw_segments:
        if e - s >= MIN_SEGMENT_DURATION:
            segments.append((s, e))
        else:
            print(f"  ⏭  Mini-Segment übersprungen: {s:.1f}s–{e:.1f}s ({e-s:.1f}s)")

    return segments


def apply_repeat_cuts(segments, repeat_cuts):
    """Schneidet Wiederholungs-Bereiche aus Keep-Segmenten raus."""
    result = []
    for seg_start, seg_end in segments:
        remaining = [(seg_start, seg_end)]
        for cut_start, cut_end in repeat_cuts:
            new_remaining = []
            for rs, re in remaining:
                if cut_end <= rs or cut_start >= re:
                    new_remaining.append((rs, re))
                elif cut_start <= rs and cut_end >= re:
                    pass  # komplett überlappend, raus
                elif cut_start > rs and cut_end < re:
                    new_remaining.append((rs, cut_start))
                    new_remaining.append((cut_end, re))
                elif cut_start <= rs:
                    new_remaining.append((cut_end, re))
                else:
                    new_remaining.append((rs, cut_start))
            remaining = new_remaining
        result.extend(remaining)
    # Kleine Reste filtern
    return [(s, e) for s, e in result if e - s > 0.1]


def get_duration(video_path):
    result = subprocess.run([
        "ffprobe", "-v", "quiet", "-print_format", "json",
        "-show_format", str(video_path)
    ], capture_output=True, text=True)
    return float(json.loads(result.stdout)['format']['duration'])


def merge_close_segments(segments, max_gap=0.3):
    """Benachbarte Segmente zusammenführen wenn Lücke < max_gap — weniger Cuts."""
    if not segments:
        return segments
    merged = [segments[0]]
    for s, e in segments[1:]:
        prev_s, prev_e = merged[-1]
        if s - prev_e <= max_gap:
            merged[-1] = (prev_s, e)
        else:
            merged.append((s, e))
    return merged


def cut_video(video_path, segments, output_path):
    """
    filter_complex Ansatz mit ultrafast preset.
    Nahe Segmente werden erst zusammengeführt um Cuts zu reduzieren.
    Timeout: 2 Stunden (reicht für 26 min Sony XAVC-S).
    """
    # Erst benachbarte Segmente zusammenführen
    segments = merge_close_segments(segments, max_gap=0.3)

    print(f"\n✂️  Schneide: {len(segments)} Segmente → {output_path.name}")
    total_keep = sum(e - s for s, e in segments)
    print(f"  Gesamtlänge nach Cut: {total_keep/60:.1f} min")

    filter_parts = []
    for i, (start, end) in enumerate(segments):
        s = max(0, start)
        e = max(s + 0.05, end)
        filter_parts.append(
            f"[0:v]trim=start={s:.3f}:end={e:.3f},setpts=PTS-STARTPTS[v{i}];"
            f"[0:a]atrim=start={s:.3f}:end={e:.3f},asetpts=PTS-STARTPTS[a{i}]"
        )

    n = len(segments)
    concat_in = "".join([f"[v{i}][a{i}]" for i in range(n)])
    filter_complex = ";".join(filter_parts) + f";{concat_in}concat=n={n}:v=1:a=1[outv][outa]"

    print(f"  → Encoding läuft (ultrafast, kann 30-60 min dauern)...")
    result = subprocess.run([
        "ffmpeg", "-y", "-i", str(video_path),
        "-filter_complex", filter_complex,
        "-map", "[outv]", "-map", "[outa]",
        "-c:v", "libx264", "-crf", "23", "-preset", "ultrafast",
        "-c:a", "aac", "-b:a", "192k",
        str(output_path)
    ], capture_output=True, text=True, timeout=7200)  # 2 Stunden

    if result.returncode == 0 and output_path.exists():
        size_mb = output_path.stat().st_size / 1e6
        print(f"  ✅ Fertig! {size_mb:.0f} MB → {output_path.name}")
        return True
    else:
        print(f"  ❌ Fehler: {result.stderr[-400:]}")
        return False


def print_cut_summary(original_dur, segments, repeat_cuts):
    total_keep = sum(e - s for s, e in segments)
    saved = original_dur - total_keep
    print(f"\n{'='*55}")
    print(f"📋 Schnittplan-Zusammenfassung")
    print(f"{'='*55}")
    print(f"  Original:           {original_dur/60:.1f} min")
    print(f"  Nach Cut:           {total_keep/60:.1f} min")
    print(f"  Gespart:            {saved/60:.1f} min ({saved/original_dur*100:.0f}%)")
    print(f"  Keep-Segmente:      {len(segments)}")
    print(f"  Wiederholungen:     {len(repeat_cuts)} Stellen")
    print(f"{'='*55}")


def process_file(video_path_str):
    video_path = Path(video_path_str)
    name = video_path.stem

    print(f"\n{'='*55}")
    print(f"🎬 {video_path.name}")
    print(f"{'='*55}")

    duration = get_duration(video_path)
    print(f"  Dauer: {duration/60:.1f} min")

    audio_path = WORK_DIR / f"{name}_audio.wav"
    extract_audio(video_path, audio_path)

    words, segs = transcribe_with_words(audio_path)

    # Transcript speichern
    transcript_path = OUTPUT_DIR / f"{name}_transcript_v2.txt"
    lines = [f"[{s['start']:.2f} - {s['end']:.2f}] {s['text']}" for s in segs]
    transcript_path.write_text('\n'.join(lines))

    # Keep-Segmente aus Word-Timestamps (Räuspern/Luftholen raus)
    speech_segments = words_to_speech_segments(words, duration)
    print(f"\n  Word-basierte Segmente: {len(speech_segments)}")

    # Wiederholungen finden
    repeat_cuts = detect_repeats(segs)

    # Wiederholungen aus Segmenten rausschneiden
    final_segments = apply_repeat_cuts(speech_segments, repeat_cuts)

    print_cut_summary(duration, final_segments, repeat_cuts)

    # Video schneiden
    output_path = OUTPUT_DIR / f"{name} — Raw Cut.mp4"
    cut_video(video_path, final_segments, output_path)

    # Aufräumen
    if audio_path.exists():
        audio_path.unlink()


# === MAIN ===
print("\n🎬 Jarvis Raw Cut v2")
print(f"Word-Level Timestamps | Räuspern/Luftholen | Wiederholungs-Erkennung")

# Auto-scan: alle MP4s aus ready to edit (inkl. Unterordner, ignoriert processed/)
if not INPUT_FILES:
    found = []
    for mp4 in sorted(READY_TO_EDIT_DIR.rglob("*.MP4")) + sorted(READY_TO_EDIT_DIR.rglob("*.mp4")):
        if "processed" not in str(mp4).lower():
            found.append(str(mp4))
    if not found:
        print("⚠️ Keine MP4s in 02 ready to edit gefunden.")
    else:
        print(f"  {len(found)} Clip(s) gefunden:")
        for f in found:
            rel = Path(f).relative_to(READY_TO_EDIT_DIR)
            print(f"  → {rel}")
    INPUT_FILES.extend(found)

for f in INPUT_FILES:
    if not Path(f).exists():
        print(f"⚠️ Nicht gefunden: {f}")
        continue
    process_file(f)

print("\n✅ Fertig!")

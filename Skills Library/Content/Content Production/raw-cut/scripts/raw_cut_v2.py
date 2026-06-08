#!/usr/bin/env python3
"""
raw_cut_v2.py — Automatischer Raw Cut v2
Vier-Layer-Architektur: Similarity (L1) + Stotter (L2) + Einatmer (L3) + Claude Review (L4)

Pipeline:
    1. FFmpeg extrahiert Audio (16kHz mono WAV)
    2. whisper-timestamped transkribiert (Wort-Timestamps, Disfluencies)
    3. Phrasen-Splitter (Pause > 0.4s trennt)
    4. Layer 1 — Similarity: difflib.SequenceMatcher + LCS-Substring + Prefix-Match
    5. Layer 2 — Stotter: direkt aufeinanderfolgende n-gram-Wiederholungen (2-6 Wörter)
    6. Silence-Detection (Stille > 0.5s auf 0.15s kürzen)
    7. Filler-Detection (äh, ähm isoliert)
    8. Layer 3 — Einatmer: librosa Frequenzband-Check (100-500Hz vs 1-3kHz)
    9. Cut-Merge: alle Layer zusammen, Overlaps auflösen, nach Start sortieren
   10. Layer 4 — Claude Validator: CLI-first, API-Fallback, skip bei Fehlen
   11. Preview-Tabelle (gruppiert nach Quelle)
   12. User-Bestätigung
   13. FFmpeg filter_complex schneidet Video
   14. Output: MP4 oder FCPXML für DaVinci Resolve

Usage:
    python raw_cut_v2.py --input video.mp4
    python raw_cut_v2.py --input video.mp4 --breath-mode conservative
    python raw_cut_v2.py --input video.mp4 --no-preview --output xml
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field, asdict
from difflib import SequenceMatcher
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

# ─── Konfiguration ────────────────────────────────────────────────────────────

DEFAULT_WHISPER_MODEL = "medium"
DEFAULT_LANGUAGE = "de"

# Phrase-Splitter
PHRASE_SPLIT_GAP = 0.4  # Pause > X Sekunden trennt Phrasen

# Layer 1 — Similarity
L1_LOOKAHEAD_WINDOW = 45.0   # Sekunden vorwärts scannen
L1_SM_RATIO_THRESHOLD = 0.75
L1_LCS_RATIO_THRESHOLD = 0.60
L1_PREFIX_RATIO_THRESHOLD = 0.75
L1_MIN_WORDS = 3

# Layer 1.5 — Intra-Phrase Repeat (nicht-adjazente Wiederholungen innerhalb einer Phrase)
L15_MIN_NGRAM = 3        # kleinste n-Gramm-Länge die erkannt wird
L15_MAX_NGRAM = 8        # größte n-Gramm-Länge
L15_MIN_WORDS = 8        # Phrasen kürzer werden ignoriert
L15_MIN_CUT_DURATION = 0.1  # Mindest-Cut-Länge in Sekunden

# Layer 2 — Stotter
L2_MIN_NGRAM = 2
L2_MAX_NGRAM = 6

# Layer 3 — Einatmer
L3_MIN_SILENCE_BEFORE_WORD = 0.3   # nur Onsets mit mind. X Sek vorheriger Stille prüfen
L3_BREATH_LOOKBACK = 0.4           # wie weit vor dem Onset untersuchen
L3_KEEP_BEFORE_ONSET = 0.15        # so viel Pause unmittelbar vor dem Wort behalten
L3_BREATH_FREQ_LOW = (100, 500)    # Einatmer-Band (Hz)
L3_BREATH_FREQ_HIGH = (1000, 3000) # Sprach-Formanten-Band (Hz)
L3_BREATH_ENERGY_RATIO = 1.5       # RMS_low / RMS_high > X  => Einatmer
L3_BREATH_MIN_RMS = 0.002          # Mindest-Energie damit es kein reiner Raum-Noise ist

# Silence
SILENCE_THRESHOLD = 0.5   # Stille > X Sekunden wird gekürzt
SILENCE_PAD = 0.15        # Rest-Pause an Cut-Grenzen

# Filler
FILLER_WORDS_DE = {"äh", "ähm", "öh", "mhm", "hm", "ähhh", "ahm"}
FILLER_WORDS_EN = {"um", "uh", "eh", "hmm"}

# Parallelstruktur-Heuristik
PARALLEL_MAX_LEN_DIFF = 2

# Layer 4 — Claude
L4_CLI_COMMAND = "claude"
L4_API_MODEL = "claude-sonnet-4-5-20250929"
L4_MAX_TOKENS = 4096
L4_CONTEXT_WORDS = 8

# ─── Datenklassen ─────────────────────────────────────────────────────────────

@dataclass
class CutRegion:
    start: float
    end: float
    source: str        # "similarity" | "stutter" | "breath" | "silence" | "filler" | "validator_add" | "merged"
    reason: str
    rejected: bool = False

    def duration(self) -> float:
        return max(0.0, self.end - self.start)

    def as_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Phrase:
    start: float
    end: float
    text: str
    words: List[Dict[str, Any]]

    def clean_text(self) -> str:
        return clean_text(self.text)

    def clean_words(self) -> List[str]:
        return [clean_word(w["text"]) for w in self.words if clean_word(w["text"])]


# ─── Text-Hilfsfunktionen ─────────────────────────────────────────────────────

_PUNCT_RE = re.compile(r"[^\w\säöüÄÖÜß]+", re.UNICODE)


def clean_text(s: str) -> str:
    """Lowercase + Satzzeichen raus + Whitespace normalisiert."""
    s = _PUNCT_RE.sub(" ", s.lower())
    return " ".join(s.split())


def clean_word(s: str) -> str:
    s = _PUNCT_RE.sub("", s.lower())
    return s.strip()


def lcs_substring_words(a: List[str], b: List[str]) -> int:
    """Längster gemeinsamer contiguous Substring auf Wort-Ebene (Anzahl Wörter)."""
    if not a or not b:
        return 0
    m, n = len(a), len(b)
    # Zwei Zeilen statt voller Matrix (Speicher)
    prev = [0] * (n + 1)
    best = 0
    for i in range(1, m + 1):
        cur = [0] * (n + 1)
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                cur[j] = prev[j - 1] + 1
                if cur[j] > best:
                    best = cur[j]
        prev = cur
    return best


def common_prefix_count(a: List[str], b: List[str]) -> int:
    n = 0
    for x, y in zip(a, b):
        if x == y:
            n += 1
        else:
            break
    return n


# ─── Audio-Extraktion ─────────────────────────────────────────────────────────

def extract_audio(video_path: str, audio_path: str) -> None:
    cmd = [
        "ffmpeg", "-y",
        "-i", video_path,
        "-ac", "1",
        "-ar", "16000",
        "-vn",
        audio_path,
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"FFmpeg Fehler beim Audio-Extract:\n{res.stderr[-1200:]}")
        sys.exit(1)
    print(f"✓ Audio extrahiert → {audio_path}")


# ─── Transkription ────────────────────────────────────────────────────────────

def transcribe(audio_path: str, model_name: str, language: str) -> Dict[str, Any]:
    """Transkription mit Word-Timestamps. Nutzt faster-whisper (primär) oder whisper-timestamped (Fallback)."""

    # ── faster-whisper (primär, bereits installiert von v1) ──────────────────
    try:
        from faster_whisper import WhisperModel
        print(f"↻ Lade Whisper-Modell '{model_name}' (faster-whisper) …")
        model = WhisperModel(model_name, device="cpu", compute_type="int8")
        print("↻ Transkribiere (kann einige Minuten dauern) …")
        segments_iter, info = model.transcribe(
            audio_path,
            language=language,
            beam_size=5,
            word_timestamps=True,
        )
        words: List[Dict[str, Any]] = []
        full_text_parts: List[str] = []
        for seg in segments_iter:
            full_text_parts.append(seg.text.strip())
            if seg.words:
                for w in seg.words:
                    text = w.word.strip()
                    if not text:
                        continue
                    words.append({
                        "text": text,
                        "start": float(w.start),
                        "end": float(w.end),
                        "confidence": float(w.probability),
                        "is_filler": False,
                    })
        detected_lang = info.language if hasattr(info, "language") else language
        print(f"✓ {len(words)} Wörter, Sprache: {detected_lang}")
        return {"text": " ".join(full_text_parts), "words": words, "language": detected_lang}

    except ImportError:
        pass  # Fallback auf whisper-timestamped

    # ── whisper-timestamped (Fallback) ───────────────────────────────────────
    try:
        import whisper_timestamped as whisper
    except ImportError:
        print("Fehler: weder faster-whisper noch whisper-timestamped installiert.")
        print("Installieren: pip3 install faster-whisper")
        sys.exit(1)

    print(f"↻ Lade Whisper-Modell '{model_name}' (whisper-timestamped) …")
    model_wt = whisper.load_model(model_name)
    print("↻ Transkribiere …")
    result = whisper.transcribe(model_wt, audio_path, language=language, detect_disfluencies=True, vad=True)

    words = []
    for segment in result["segments"]:
        for w in segment.get("words", []):
            text = w["text"].strip()
            words.append({
                "text": text,
                "start": float(w["start"]),
                "end": float(w["end"]),
                "confidence": float(w.get("confidence", 1.0)),
                "is_filler": text in ("[*]",),
            })
    print(f"✓ {len(words)} Wörter, Sprache: {result.get('language', language)}")
    return {"text": result["text"], "words": words, "language": result.get("language", language)}


# ─── Phrase-Splitter ──────────────────────────────────────────────────────────

def split_into_phrases(words: List[Dict[str, Any]]) -> List[Phrase]:
    """Splittet Wörter in Phrasen bei Pausen > PHRASE_SPLIT_GAP. Filler werden ignoriert."""
    phrases: List[Phrase] = []
    buffer: List[Dict[str, Any]] = []
    prev_end = 0.0

    for w in words:
        if w.get("is_filler"):
            continue
        gap = w["start"] - prev_end
        if buffer and gap > PHRASE_SPLIT_GAP:
            phrases.append(_make_phrase(buffer))
            buffer = []
        buffer.append(w)
        prev_end = w["end"]

    if buffer:
        phrases.append(_make_phrase(buffer))

    return phrases


def _make_phrase(words: List[Dict[str, Any]]) -> Phrase:
    return Phrase(
        start=words[0]["start"],
        end=words[-1]["end"],
        text=" ".join(w["text"] for w in words),
        words=words,
    )


# ─── Layer 1: Similarity-based duplicate detection ────────────────────────────

def _is_parallel_structure(words_a: List[str], words_b: List[str]) -> bool:
    """'Ich bin brutal stolz' / 'Ich bin brutal happy' → gleicher Anfang, anderes Ende → Parallelstruktur."""
    if not words_a or not words_b:
        return False
    if abs(len(words_a) - len(words_b)) > PARALLEL_MAX_LEN_DIFF:
        return False
    min_len = min(len(words_a), len(words_b))
    if min_len < 3:
        return False
    cp = common_prefix_count(words_a, words_b)
    if cp >= min_len - 2 and cp < min_len:
        return True
    return False


def _should_cut_earlier(a: Phrase, b: Phrase) -> Tuple[bool, str]:
    """a ist früher, b ist später. Gibt (should_cut_a, reason) zurück."""
    text_a = a.clean_text()
    text_b = b.clean_text()
    words_a = a.clean_words()
    words_b = b.clean_words()

    if not text_a or not text_b:
        return (False, "")
    if len(words_a) < L1_MIN_WORDS:
        return (False, "")

    if _is_parallel_structure(words_a, words_b):
        return (False, "parallel")

    # Regel 1: SequenceMatcher char-level
    r_sm = SequenceMatcher(None, text_a, text_b, autojunk=False).ratio()
    if r_sm >= L1_SM_RATIO_THRESHOLD:
        return (True, f"SM {r_sm:.2f}")

    # Regel 2: LCS-Substring word-level
    lcs_len = lcs_substring_words(words_a, words_b)
    min_words = min(len(words_a), len(words_b))
    lcs_ratio = lcs_len / min_words if min_words else 0
    if lcs_ratio >= L1_LCS_RATIO_THRESHOLD and lcs_len >= L1_MIN_WORDS:
        return (True, f"LCS {lcs_ratio:.2f} ({lcs_len}W)")

    # Regel 3: Prefix-Match (A ist abgebrochene Version von B)
    if len(text_a) <= len(text_b) and len(text_a) >= 6:
        prefix_b = text_b[: len(text_a)]
        r_prefix = SequenceMatcher(None, text_a, prefix_b, autojunk=False).ratio()
        if r_prefix >= L1_PREFIX_RATIO_THRESHOLD:
            return (True, f"Prefix {r_prefix:.2f} (abgebrochen)")

    return (False, "")


def layer1_similarity_cuts(phrases: List[Phrase]) -> List[CutRegion]:
    cuts: List[CutRegion] = []
    marked: set = set()

    for i, a in enumerate(phrases):
        if i in marked:
            continue
        if len(a.clean_words()) < L1_MIN_WORDS:
            continue

        similar: List[Tuple[int, str]] = []
        for j in range(i + 1, len(phrases)):
            b = phrases[j]
            if b.start - a.end > L1_LOOKAHEAD_WINDOW:
                break
            cut, reason = _should_cut_earlier(a, b)
            if cut:
                similar.append((j, reason))

        if not similar:
            continue

        last_idx = similar[-1][0]
        to_cut_idx = [i] + [idx for idx, _ in similar[:-1]]
        for idx in to_cut_idx:
            if idx in marked:
                continue
            marked.add(idx)
            p = phrases[idx]
            _, rtext = _should_cut_earlier(p, phrases[last_idx])
            snippet = (p.text[:60] + "…") if len(p.text) > 60 else p.text
            cuts.append(CutRegion(
                start=p.start,
                end=p.end,
                source="similarity",
                reason=f"L1 {rtext} → letzte @ {phrases[last_idx].start:.1f}s | \"{snippet}\"",
            ))

    return cuts


# ─── Layer 1.5: Intra-Phrase Repeat detection ────────────────────────────────

def layer15_intra_phrase_cuts(phrases: List[Phrase]) -> List[CutRegion]:
    """
    Findet nicht-adjazente Wiederholungen von n-Grammen INNERHALB einer einzelnen Phrase.

    Fängt Muster wie:
      'entlang dieser Spirale entwickeln und entlang dieser Spirale und entlang dieser Spirale'
      'und damit kommen wir zu dem Punkt und damit kommen wir zu einem und damit kommen wir zu'
      'ich nenne das ganze epistemische Feigheit nämlich ich nenne das ganze epistemische Feigheit'

    Strategie: für jede Phrase mit >= L15_MIN_WORDS Wörtern,
    suche von groß nach klein (n=L15_MAX_NGRAM..L15_MIN_NGRAM) nach dem ersten n-Gramm
    das an 2+ nicht-direkt-benachbarten Positionen vorkommt (mindestens 1 Wort Abstand).
    Schneidet von der ERSTEN Occurrence bis zum Start der LETZTEN Occurrence.
    Die letzte Version des Satzes bleibt erhalten.

    Parallelstruktur-Schutz:
    Wenn zwischen zwei Occurrences insgesamt <= 1 Trennwort liegt UND dieses Wort kein
    Restart-Marker ist (nämlich, also, äh, ...), wird es als rhetorische Parallelstruktur
    gewertet und NICHT geschnitten.
    Beispiel: 'Ich bin brutal stolz. Ich bin brutal happy.' bleibt erhalten.

    Abgrenzung zu Layer 2:
    - Layer 2: direkt aufeinanderfolgende Wiederholungen (A B C A B C)
    - Layer 1.5: Wiederholungen mit Lücken dazwischen (A B C D E A B C)
    """
    # Wörter die einen Neustart markieren (kein Inhalt, nur Überleitung)
    RESTART_MARKERS: set = {
        "nämlich", "also", "äh", "ähm", "öh", "hm", "mhm",
        "oder", "beziehungsweise", "bzw", "sprich",
        "ich", "wir", "ihr", "du", "das",
    }

    cuts: List[CutRegion] = []

    for phrase in phrases:
        wc = phrase.clean_words()
        wo = phrase.words  # Wörter mit Timestamps

        if len(wc) < L15_MIN_WORDS:
            continue

        found = False
        for n in range(min(L15_MAX_NGRAM, len(wc) // 2), L15_MIN_NGRAM - 1, -1):
            if found:
                break
            for i in range(len(wc) - n - 1):
                unit = tuple(wc[i: i + n])
                if not all(unit):
                    continue

                # Suche alle Vorkommen ab i+n+1 (mind. 1 Wort Abstand = nicht-adjazent)
                occurrences = [i]
                j = i + n + 1
                while j <= len(wc) - n:
                    if tuple(wc[j: j + n]) == unit:
                        occurrences.append(j)
                        j += n
                    else:
                        j += 1

                if len(occurrences) < 2:
                    continue

                # Gesamtzahl der Wörter zwischen allen Occurrence-Paaren sammeln
                total_middle = 0
                middle_words: List[str] = []
                for k in range(len(occurrences) - 1):
                    gap_start = occurrences[k] + n
                    gap_end = occurrences[k + 1]
                    total_middle += gap_end - gap_start
                    middle_words.extend(wc[gap_start:gap_end])

                # Parallelstruktur-Schutz:
                # <= 1 Trennwort ohne Restart-Marker → rhetorische Parallelstruktur → skip.
                if total_middle <= 1:
                    if not middle_words or middle_words[0] not in RESTART_MARKERS:
                        continue

                first_idx = occurrences[0]
                last_idx = occurrences[-1]

                if first_idx >= len(wo) or last_idx >= len(wo):
                    continue

                cut_start = wo[first_idx]["start"]
                cut_end = wo[last_idx]["start"]

                if cut_end - cut_start < L15_MIN_CUT_DURATION:
                    continue

                snippet = " ".join(unit)[:40]
                cuts.append(CutRegion(
                    start=cut_start,
                    end=cut_end,
                    source="intra_phrase",
                    reason=(
                        f"L1.5 {len(occurrences)}x {n}-gram '{snippet}' "
                        f"(Lücken @ {', '.join(str(o) for o in occurrences)})"
                    ),
                ))
                found = True
                break

    return cuts


# ─── Layer 2: Stutter n-gram detection ────────────────────────────────────────

def layer2_stutter_cuts(words: List[Dict[str, Any]]) -> List[CutRegion]:
    """Direkt aufeinanderfolgende n-gram-Wiederholungen (2-6 Wörter), cuttet alle ausser die letzte."""
    speech_words = [w for w in words if not w.get("is_filler")]
    clean = [clean_word(w["text"]) for w in speech_words]

    cuts: List[CutRegion] = []
    i = 0
    while i < len(clean) - 1:
        best_n = 0
        best_reps = 0
        for n in range(L2_MAX_NGRAM, L2_MIN_NGRAM - 1, -1):
            if i + 2 * n > len(clean):
                continue
            unit = clean[i: i + n]
            if any(not w for w in unit):
                continue
            reps = 1
            while (i + (reps + 1) * n <= len(clean)
                   and clean[i + reps * n: i + (reps + 1) * n] == unit):
                reps += 1
            if reps >= 2 and (reps - 1) * n > (best_reps - 1) * best_n:
                best_n = n
                best_reps = reps
        if best_reps >= 2:
            cut_word_start = i
            cut_word_end_exclusive = i + (best_reps - 1) * best_n
            start_t = speech_words[cut_word_start]["start"]
            end_t = speech_words[cut_word_end_exclusive - 1]["end"]
            unit_text = " ".join(clean[i: i + best_n])
            cuts.append(CutRegion(
                start=start_t,
                end=end_t,
                source="stutter",
                reason=f"L2 Stotter {best_reps}x '{unit_text}' ({best_n}-gram)",
            ))
            i = cut_word_end_exclusive + best_n
        else:
            i += 1
    return cuts


# ─── Layer 3: Einatmer-Removal via librosa ────────────────────────────────────

def layer3_breath_cuts(words: List[Dict[str, Any]],
                       audio_path: str,
                       mode: str) -> List[CutRegion]:
    """mode: 'aggressive' (Frequenzband-Check) | 'conservative' (blind cut) | 'off'."""
    if mode == "off":
        return []

    if mode == "aggressive":
        try:
            import numpy as np  # noqa
            import librosa       # noqa
        except ImportError:
            print("⚠️  librosa nicht installiert — Layer 3 kann 'aggressive' nicht laufen.")
            print("   Installieren: pip install librosa")
            print("   Falle zurück auf 'conservative' für diesen Run.")
            mode = "conservative"

    speech_words = [w for w in words if not w.get("is_filler")]
    if not speech_words:
        return []

    cuts: List[CutRegion] = []

    # Conservative: keine Audio-Analyse, blind cutten
    if mode == "conservative":
        prev_end = 0.0
        for w in speech_words:
            gap = w["start"] - prev_end
            if gap >= L3_MIN_SILENCE_BEFORE_WORD:
                cut_start = prev_end + SILENCE_PAD
                cut_end = w["start"] - L3_KEEP_BEFORE_ONSET
                if cut_end - cut_start >= 0.05:
                    cuts.append(CutRegion(
                        start=cut_start,
                        end=cut_end,
                        source="breath",
                        reason=f"L3 konservativ: Pre-Onset-Pause {gap:.2f}s",
                    ))
            prev_end = w["end"]
        return cuts

    # Aggressive: Frequenzband-Check
    import numpy as np
    import librosa

    print("↻ Lade Audio für Einatmer-Analyse …")
    y, sr = librosa.load(audio_path, sr=16000, mono=True)

    prev_end = 0.0
    for w in speech_words:
        gap = w["start"] - prev_end
        if gap < L3_MIN_SILENCE_BEFORE_WORD:
            prev_end = w["end"]
            continue

        lookback_start = max(prev_end, w["start"] - L3_BREATH_LOOKBACK)
        lookback_end = w["start"]
        if lookback_end - lookback_start < 0.1:
            prev_end = w["end"]
            continue

        seg = y[int(lookback_start * sr): int(lookback_end * sr)]
        if len(seg) < 256:
            prev_end = w["end"]
            continue

        n_fft = 512
        hop = 128
        S = np.abs(librosa.stft(seg, n_fft=n_fft, hop_length=hop))
        freqs = librosa.fft_frequencies(sr=sr, n_fft=n_fft)

        low_mask = (freqs >= L3_BREATH_FREQ_LOW[0]) & (freqs <= L3_BREATH_FREQ_LOW[1])
        high_mask = (freqs >= L3_BREATH_FREQ_HIGH[0]) & (freqs <= L3_BREATH_FREQ_HIGH[1])

        if not low_mask.any() or not high_mask.any():
            prev_end = w["end"]
            continue

        rms_low = float(np.sqrt(np.mean(S[low_mask] ** 2)))
        rms_high = float(np.sqrt(np.mean(S[high_mask] ** 2)))
        rms_overall = float(np.sqrt(np.mean(seg ** 2)))

        is_breath = (
            rms_overall >= L3_BREATH_MIN_RMS
            and rms_high > 1e-9
            and (rms_low / rms_high) >= L3_BREATH_ENERGY_RATIO
        )

        if is_breath:
            cut_start = lookback_start
            cut_end = w["start"] - L3_KEEP_BEFORE_ONSET
            if cut_end - cut_start >= 0.05:
                cuts.append(CutRegion(
                    start=cut_start,
                    end=cut_end,
                    source="breath",
                    reason=f"L3 Einatmer (low/high RMS {rms_low / max(rms_high, 1e-9):.2f})",
                ))

        prev_end = w["end"]

    return cuts


# ─── Silence-Detection ────────────────────────────────────────────────────────

def silence_cuts(words: List[Dict[str, Any]], total_duration: float) -> List[CutRegion]:
    speech = [w for w in words if not w.get("is_filler")]
    cuts: List[CutRegion] = []
    prev_end = 0.0

    for w in speech:
        gap = w["start"] - prev_end
        if gap > SILENCE_THRESHOLD:
            cut_start = prev_end + SILENCE_PAD
            cut_end = w["start"] - SILENCE_PAD
            if cut_end - cut_start >= 0.05:
                cuts.append(CutRegion(
                    start=cut_start,
                    end=cut_end,
                    source="silence",
                    reason=f"Stille {gap:.2f}s → kürzen auf {2 * SILENCE_PAD:.2f}s",
                ))
        prev_end = w["end"]

    if total_duration - prev_end > SILENCE_THRESHOLD:
        cuts.append(CutRegion(
            start=prev_end + SILENCE_PAD,
            end=total_duration,
            source="silence",
            reason=f"Stille am Ende {total_duration - prev_end:.2f}s",
        ))

    return cuts


# ─── Filler-Detection ─────────────────────────────────────────────────────────

def filler_cuts(words: List[Dict[str, Any]]) -> List[CutRegion]:
    cuts: List[CutRegion] = []
    fillers = FILLER_WORDS_DE | FILLER_WORDS_EN

    for i, w in enumerate(words):
        is_filler_marker = w.get("is_filler")
        is_filler_word = clean_word(w["text"]) in fillers
        if not (is_filler_marker or is_filler_word):
            continue

        prev_end = words[i - 1]["end"] if i > 0 else 0.0
        next_start = words[i + 1]["start"] if i + 1 < len(words) else w["end"]

        gap_before = w["start"] - prev_end
        gap_after = next_start - w["end"]

        if gap_before >= 0.15 or gap_after >= 0.15:
            cuts.append(CutRegion(
                start=max(0.0, w["start"] - 0.05),
                end=w["end"] + 0.05,
                source="filler",
                reason=f"Filler '{w['text']}' isoliert",
            ))

    return cuts


# ─── Cut-Merge & Overlap-Resolution ───────────────────────────────────────────

def merge_cut_regions(cuts: List[CutRegion], total_duration: float) -> List[CutRegion]:
    active = [c for c in cuts if not c.rejected and c.duration() > 0]
    active.sort(key=lambda c: c.start)

    merged: List[CutRegion] = []
    for c in active:
        start = max(0.0, c.start)
        end = min(total_duration, c.end)
        if end - start <= 0:
            continue

        if merged and start <= merged[-1].end + 0.01:
            prev = merged[-1]
            if c.source != prev.source and prev.source != "merged":
                prev.source = "merged"
                prev.reason = f"{prev.reason} + {c.reason}"
            elif c.source != prev.source:
                prev.reason = f"{prev.reason} + {c.reason}"
            prev.end = max(prev.end, end)
        else:
            merged.append(CutRegion(
                start=start, end=end,
                source=c.source, reason=c.reason,
            ))
    return merged


def invert_cuts_to_keeps(cuts: List[CutRegion], total_duration: float) -> List[Dict[str, Any]]:
    keeps: List[Dict[str, Any]] = []
    cursor = 0.0
    for c in cuts:
        if c.start > cursor:
            keeps.append({"start": cursor, "end": c.start})
        cursor = max(cursor, c.end)
    if cursor < total_duration:
        keeps.append({"start": cursor, "end": total_duration})
    return [k for k in keeps if k["end"] - k["start"] >= 0.05]


# ─── Layer 4: Claude Validator ────────────────────────────────────────────────

def _build_validator_prompt(cuts: List[CutRegion], words: List[Dict[str, Any]]) -> str:
    lines = [
        "Du bist ein Video-Editor-Reviewer. Ich habe algorithmisch eine Cut-Liste generiert.",
        "Deine Aufgabe: nur algorithmus-bedingte Fehler korrigieren.",
        "",
        "Du darfst:",
        "  (a) einen Cut ABLEHNEN wenn es absichtliche Parallelstruktur oder rhetorische Wiederholung ist.",
        "      Beispiel: 'Ich bin brutal stolz. Ich bin brutal happy.' → nicht cutten",
        "      Beispiel: 'Langsam. Ganz langsam. Noch langsamer.' → nicht cutten",
        "  (b) einen ZUSÄTZLICHEN Cut vorschlagen wenn der Algorithmus eine echte Wiederholung übersehen hat.",
        "",
        "Regeln:",
        "  - Bei Wiederholungen IMMER den LETZTEN Take behalten",
        "  - Nie die Aussage des Creators verändern",
        "  - Keine inhaltlichen Kürzungen (nur Sprech-Fehler und Dopplungen)",
        "",
        "Antworte AUSSCHLIESSLICH mit einem JSON-Objekt ohne Text drumherum:",
        '{"reject": [<cut_id>, ...], "add": [{"start": <float>, "end": <float>, "reason": "..."}, ...]}',
        "",
        f"Cut-Liste (je {L4_CONTEXT_WORDS} Wörter Kontext vor und nach dem Cut):",
        "",
    ]

    for idx, c in enumerate(cuts):
        context_before = [w["text"] for w in words
                          if not w.get("is_filler") and w["end"] <= c.start][-L4_CONTEXT_WORDS:]
        inside = [w["text"] for w in words
                  if not w.get("is_filler") and w["start"] >= c.start and w["end"] <= c.end]
        context_after = [w["text"] for w in words
                         if not w.get("is_filler") and w["start"] >= c.end][:L4_CONTEXT_WORDS]

        before = " ".join(context_before)
        inside_text = " ".join(inside)
        after = " ".join(context_after)

        lines.append(f"[{idx}] {c.source} | {c.reason}")
        lines.append(f"    Zeit: {c.start:.2f}-{c.end:.2f}s")
        lines.append(f"    VOR CUT:    …{before}")
        lines.append(f"    INNEN (wird gecuttet): «{inside_text}»")
        lines.append(f"    NACH CUT:   {after}…")
        lines.append("")

    lines.append("Wenn alles OK: {\"reject\": [], \"add\": []}")
    return "\n".join(lines)


def _try_claude_cli(prompt: str) -> Optional[str]:
    cli = shutil.which(L4_CLI_COMMAND)
    if not cli:
        return None
    try:
        # stdin-Variante ist die robustere: viele claude-CLI-Versionen mögen
        # -p mit sehr großem String in argv nicht.
        res = subprocess.run(
            [cli, "-p", "--output-format", "text"],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=180,
        )
        if res.returncode == 0 and res.stdout.strip():
            return res.stdout.strip()
        # Fallback ohne --output-format
        res2 = subprocess.run(
            [cli, "-p"],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=180,
        )
        if res2.returncode == 0 and res2.stdout.strip():
            return res2.stdout.strip()
        print(f"⚠️  claude CLI exit {res.returncode}: {res.stderr[-400:]}")
        return None
    except subprocess.TimeoutExpired:
        print("⚠️  claude CLI Timeout (>180s)")
        return None
    except Exception as e:
        print(f"⚠️  claude CLI Fehler: {e}")
        return None


def _try_claude_api(prompt: str) -> Optional[str]:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return None
    try:
        import anthropic
    except ImportError:
        print("⚠️  anthropic SDK nicht installiert — API-Fallback nicht möglich.")
        print("   Installieren: pip install anthropic")
        return None
    try:
        client = anthropic.Anthropic()
        response = client.messages.create(
            model=L4_API_MODEL,
            max_tokens=L4_MAX_TOKENS,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text.strip()
    except Exception as e:
        print(f"⚠️  Anthropic API Fehler: {e}")
        return None


def _parse_validator_response(raw: str) -> Dict[str, Any]:
    raw = raw.strip()
    if raw.startswith("```"):
        first_nl = raw.find("\n")
        if first_nl > 0:
            raw = raw[first_nl + 1:]
        if raw.endswith("```"):
            raw = raw[:-3]
    m_start = raw.find("{")
    m_end = raw.rfind("}")
    if m_start == -1 or m_end == -1:
        return {"reject": [], "add": []}
    try:
        data = json.loads(raw[m_start: m_end + 1])
    except json.JSONDecodeError:
        return {"reject": [], "add": []}
    reject = []
    for x in data.get("reject", []):
        try:
            reject.append(int(x))
        except (TypeError, ValueError):
            continue
    adds = [a for a in data.get("add", []) if isinstance(a, dict) and "start" in a and "end" in a]
    return {"reject": reject, "add": adds}


def layer4_validator(cuts: List[CutRegion],
                     words: List[Dict[str, Any]],
                     backend: str) -> Tuple[List[CutRegion], Dict[str, Any]]:
    stats = {"backend": None, "rejected": 0, "added": 0, "skipped_reason": None}

    if backend == "off":
        stats["skipped_reason"] = "Flag --validator-backend off"
        return cuts, stats
    if not cuts:
        stats["skipped_reason"] = "keine Cuts zum Reviewen"
        return cuts, stats

    prompt = _build_validator_prompt(cuts, words)

    raw: Optional[str] = None
    chosen: Optional[str] = None

    if backend in ("auto", "cli"):
        print("↻ Layer 4 — Claude Validator via CLI …")
        raw = _try_claude_cli(prompt)
        if raw is not None:
            chosen = "cli"

    if raw is None and backend in ("auto", "api"):
        print("↻ Layer 4 — Claude Validator via API …")
        raw = _try_claude_api(prompt)
        if raw is not None:
            chosen = "api"

    if raw is None:
        stats["skipped_reason"] = "weder claude CLI noch ANTHROPIC_API_KEY verfügbar"
        print("⚠️  Layer 4 übersprungen — weder claude CLI noch API-Key verfügbar.")
        return cuts, stats

    stats["backend"] = chosen
    decision = _parse_validator_response(raw)

    for idx in decision["reject"]:
        if 0 <= idx < len(cuts):
            cuts[idx].rejected = True
            cuts[idx].reason += " [VALIDATOR REJECT]"
            stats["rejected"] += 1

    for add in decision["add"]:
        try:
            start = float(add["start"])
            end = float(add["end"])
        except (TypeError, ValueError):
            continue
        if end - start <= 0:
            continue
        cuts.append(CutRegion(
            start=start, end=end,
            source="validator_add",
            reason=f"L4 Validator: {add.get('reason', 'übersehene Dopplung')}",
        ))
        stats["added"] += 1

    return cuts, stats


# ─── Preview-Tabelle ──────────────────────────────────────────────────────────

def fmt_time(t: float) -> str:
    m = int(t // 60)
    s = t - m * 60
    return f"{m:02d}:{s:05.2f}"


SOURCE_ICONS = {
    "similarity":    "🔁",
    "intra_phrase":  "🔂",
    "stutter":       "🌀",
    "breath":        "💨",
    "silence":       "🤫",
    "filler":        "🗑️ ",
    "validator_add": "✅",
    "merged":        "🔀",
}


def print_cut_preview(cuts: List[CutRegion],
                      keeps: List[Dict[str, Any]],
                      total_duration: float,
                      stats: Dict[str, Any]) -> None:
    print("\n" + "═" * 78)
    print("📋  RAW CUT v2 — SCHNITTPLAN")
    print("═" * 78)

    by_source: Dict[str, List[CutRegion]] = {}
    for c in cuts:
        if c.rejected:
            continue
        by_source.setdefault(c.source, []).append(c)

    order = ["similarity", "intra_phrase", "stutter", "breath", "silence", "filler", "validator_add", "merged"]
    for src in order:
        items = by_source.get(src, [])
        if not items:
            continue
        total_dur = sum(c.duration() for c in items)
        icon = SOURCE_ICONS.get(src, "•")
        print(f"\n{icon}  {src.upper()} — {len(items)} Cuts, {total_dur:.1f}s")
        print("─" * 78)
        for c in items[:40]:
            reason = c.reason
            if len(reason) > 72:
                reason = reason[:69] + "…"
            print(f"   {fmt_time(c.start)} → {fmt_time(c.end)}  ({c.duration():5.2f}s)  {reason}")
        if len(items) > 40:
            print(f"   … und {len(items) - 40} weitere")

    rejected = [c for c in cuts if c.rejected]
    if rejected:
        print(f"\n🚫  ABGELEHNT durch Validator — {len(rejected)} Cuts")
        print("─" * 78)
        for c in rejected[:15]:
            print(f"   {fmt_time(c.start)} → {fmt_time(c.end)}  {c.reason}")

    kept_duration = sum(k["end"] - k["start"] for k in keeps)
    cut_duration = total_duration - kept_duration
    reduction = (1 - kept_duration / total_duration) * 100 if total_duration > 0 else 0

    print("\n" + "═" * 78)
    print(f"Original:      {fmt_time(total_duration)}")
    print(f"Nach Cut:      {fmt_time(kept_duration)}  ({reduction:.1f}% kürzer, -{fmt_time(cut_duration)})")
    active_cuts = sum(1 for c in cuts if not c.rejected)
    print(f"Cuts aktiv:    {active_cuts}")
    print(f"Keep-Segmente: {len(keeps)}")
    if stats.get("backend"):
        print(f"Layer 4:       {stats['backend']} (+{stats['added']} Cuts, -{stats['rejected']} abgelehnt)")
    elif stats.get("skipped_reason"):
        print(f"Layer 4:       skipped ({stats['skipped_reason']})")
    print("═" * 78 + "\n")


# ─── FFmpeg-Schnitt ───────────────────────────────────────────────────────────

def cut_with_ffmpeg(input_video: str, keeps: List[Dict[str, Any]], output_path: str) -> None:
    if not keeps:
        print("Fehler: Keine Keep-Segmente.")
        sys.exit(1)

    filter_parts = []
    for i, k in enumerate(keeps):
        filter_parts.append(
            f"[0:v]trim=start={k['start']:.4f}:end={k['end']:.4f},"
            f"setpts=PTS-STARTPTS[v{i}];"
            f"[0:a]atrim=start={k['start']:.4f}:end={k['end']:.4f},"
            f"asetpts=PTS-STARTPTS[a{i}]"
        )
    concat_inputs = "".join(f"[v{i}][a{i}]" for i in range(len(keeps)))
    concat = f"{concat_inputs}concat=n={len(keeps)}:v=1:a=1[outv][outa]"
    full_filter = ";\n".join(filter_parts) + ";\n" + concat

    cmd = [
        "ffmpeg", "-y",
        "-i", input_video,
        "-filter_complex", full_filter,
        "-map", "[outv]",
        "-map", "[outa]",
        "-c:v", "libx264",
        "-crf", "18",
        "-preset", "fast",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        "-c:a", "aac",
        "-b:a", "192k",
        output_path,
    ]
    print(f"↻ Schneide Video mit FFmpeg ({len(keeps)} Segmente) …")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"FFmpeg Fehler:\n{res.stderr[-1200:]}")
        sys.exit(1)
    print(f"✓ Fertig: {output_path}")


# ─── FCPXML Export ────────────────────────────────────────────────────────────

def export_fcpxml(keeps: List[Dict[str, Any]], input_video: str, output_path: str) -> None:
    video_name = Path(input_video).stem
    clips_xml = ""
    offset = 0.0
    for k in keeps:
        dur = k["end"] - k["start"]
        clips_xml += f"""
        <clip name="{video_name}" offset="{offset:.4f}s" duration="{dur:.4f}s" start="{k['start']:.4f}s">
            <video ref="r1" offset="{k['start']:.4f}s" duration="{dur:.4f}s" start="{k['start']:.4f}s"/>
            <audio ref="r1" offset="{k['start']:.4f}s" duration="{dur:.4f}s" start="{k['start']:.4f}s"/>
        </clip>"""
        offset += dur

    fcpxml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE fcpxml>
<fcpxml version="1.9">
    <resources>
        <format id="r0" name="FFVideoFormat1080p2997" frameDuration="1001/30000s" width="1920" height="1080"/>
        <asset id="r1" name="{video_name}" src="file://{os.path.abspath(input_video)}"
               hasVideo="1" hasAudio="1" format="r0"/>
    </resources>
    <library>
        <event name="Raw Cut v2">
            <project name="{video_name}_raw_cut_v2">
                <sequence format="r0" duration="{offset:.4f}s">
                    <spine>{clips_xml}
                    </spine>
                </sequence>
            </project>
        </event>
    </library>
</fcpxml>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(fcpxml)
    print(f"✓ FCPXML: {output_path}")


# ─── Cuts-Log ─────────────────────────────────────────────────────────────────

def write_cuts_log(cuts: List[CutRegion], log_path: str) -> None:
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump([c.as_dict() for c in cuts], f, indent=2, ensure_ascii=False)


# ─── .env Loader ──────────────────────────────────────────────────────────────

def load_env_file() -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        return
    # Absteigend im Dateibaum nach .env suchen (Vault-Root + Parent + CWD)
    candidates = []
    here = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
    for p in [Path.cwd(), here, here.parent, here.parent.parent, here.parent.parent.parent]:
        candidates.append(p / ".env")
    # Vault-Root (für den Fall dass hardcoded Pfad existiert)
    candidates.append(Path.home() / "Documents" / "Claude" / "Jarvis" / ".env")
    for env in candidates:
        if env.is_file():
            load_dotenv(env, override=False)
            return


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Raw Cut v2 — 4-Layer-Pipeline für Talking-Head-Videos",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--input", required=True, help="Pfad zur Eingabe-Videodatei")
    parser.add_argument("--output", choices=["mp4", "xml"], default="mp4")
    parser.add_argument("--model", default=DEFAULT_WHISPER_MODEL,
                        choices=["tiny", "base", "small", "medium", "large"])
    parser.add_argument("--language", default=DEFAULT_LANGUAGE)
    parser.add_argument("--breath-mode", choices=["aggressive", "conservative", "off"],
                        default="aggressive",
                        help="Einatmer-Removal: aggressive=Frequenzband-Check, conservative=blind cut, off=aus")
    parser.add_argument("--validator-backend", choices=["auto", "cli", "api", "off"],
                        default="auto",
                        help="Layer 4 Backend: auto=CLI zuerst dann API, cli=nur CLI, api=nur API, off=aus")
    parser.add_argument("--output-path", default=None,
                        help="Optional expliziter Output-Pfad (default: neben Input)")
    parser.add_argument("--no-preview", action="store_true",
                        help="Kein interaktiver Preview, direkt schneiden")
    parser.add_argument("--keep-transcript", action="store_true",
                        help="Transcript als JSON neben dem Output speichern")
    args = parser.parse_args()

    load_env_file()

    input_video = args.input
    if not os.path.exists(input_video):
        print(f"Fehler: Datei nicht gefunden: {input_video}")
        sys.exit(1)

    stem = Path(input_video).stem
    out_dir = Path(input_video).parent
    if args.output_path:
        output_path = args.output_path
    elif args.output == "mp4":
        output_path = str(out_dir / f"{stem} — Raw Cut v2.mp4")
    else:
        output_path = str(out_dir / f"{stem}_raw_cut_v2.fcpxml")

    cuts_log_path = str(out_dir / f"{stem}_cuts_v2.json")
    transcript_path = str(out_dir / f"{stem}_transcript_v2.json")

    with tempfile.TemporaryDirectory() as tmp:
        audio_path = os.path.join(tmp, "audio.wav")

        extract_audio(input_video, audio_path)

        t = transcribe(audio_path, args.model, args.language)
        words = t["words"]
        if not words:
            print("Fehler: Keine Wörter erkannt.")
            sys.exit(1)

        total_duration = max(words[-1]["end"], 0.0)
        print(f"   Dauer (Transkript): {fmt_time(total_duration)}")

        if args.keep_transcript:
            with open(transcript_path, "w", encoding="utf-8") as f:
                json.dump(t, f, indent=2, ensure_ascii=False)
            print(f"   Transcript gespeichert: {transcript_path}")

        phrases = split_into_phrases(words)
        print(f"   Phrasen (Pause > {PHRASE_SPLIT_GAP}s): {len(phrases)}")

        print("\n↻ Layer 1 — Similarity (SequenceMatcher + LCS + Prefix) …")
        cuts = layer1_similarity_cuts(phrases)
        print(f"   → {len(cuts)} Cuts")

        print("↻ Layer 1.5 — Intra-Phrase Repeat (nicht-adjazente Wiederholungen) …")
        l15 = layer15_intra_phrase_cuts(phrases)
        cuts += l15
        print(f"   → {len(l15)} Cuts")

        print("↻ Layer 2 — Stotter n-gram …")
        l2 = layer2_stutter_cuts(words)
        cuts += l2
        print(f"   → {len(l2)} Cuts")

        print("↻ Silence-Cuts …")
        l_silence = silence_cuts(words, total_duration)
        cuts += l_silence
        print(f"   → {len(l_silence)} Cuts")

        print("↻ Filler-Cuts …")
        l_filler = filler_cuts(words)
        cuts += l_filler
        print(f"   → {len(l_filler)} Cuts")

        print(f"↻ Layer 3 — Einatmer ({args.breath_mode}) …")
        l3 = layer3_breath_cuts(words, audio_path, args.breath_mode)
        cuts += l3
        print(f"   → {len(l3)} Cuts")

        cuts, l4_stats = layer4_validator(cuts, words, args.validator_backend)

        merged = merge_cut_regions(cuts, total_duration)
        keeps = invert_cuts_to_keeps(merged, total_duration)

        write_cuts_log(cuts, cuts_log_path)
        print(f"\n📄 Cut-Log: {cuts_log_path}")

        print_cut_preview(cuts, keeps, total_duration, l4_stats)

        if not args.no_preview:
            confirm = input("Schnittplan OK? Weiter schneiden? [J/n]: ").strip().lower()
            if confirm not in ("", "j", "ja", "y", "yes"):
                print("Abgebrochen.")
                sys.exit(0)

        if args.output == "mp4":
            cut_with_ffmpeg(input_video, keeps, output_path)
        else:
            export_fcpxml(keeps, input_video, output_path)

    print(f"\n✅  Raw Cut v2 fertig: {output_path}")


if __name__ == "__main__":
    main()

"""Wav loading, trimming and simple DSP helpers (stdlib only)."""

import struct
import wave
from pathlib import Path


class AudioError(Exception):
    pass


def load_wav(path):
    """Return (sample_rate, channels, frames_as_list_of_ints)."""
    p = Path(path)
    if not p.exists():
        raise AudioError(f"no such file: {p}")
    with wave.open(str(p), "rb") as w:
        rate = w.getframerate()
        channels = w.getnchannels()
        width = w.getsampwidth()
        if width != 2:
            raise AudioError("only 16-bit pcm supported")
        raw = w.readframes(w.getnframes())
    fmt = {1: "b", 2: "h", 4: "i"}[width]
    frames = list(struct.unpack(f"<{len(raw) // width}{fmt}", raw))
    return rate, channels, frames


def duration_seconds(path):
    rate, channels, frames = load_wav(path)
    return len(frames) / channels / rate


def trim(path, out_path, start_s, end_s):
    """Write frames between start_s and end_s to out_path."""
    rate, channels, frames = load_wav(path)
    i0 = int(start_s * rate * channels)
    i1 = min(len(frames), int(end_s * rate * channels))
    with wave.open(str(out_path), "wb") as w:
        w.setnchannels(channels)
        w.setsampwidth(2)
        w.setframerate(rate)
        w.writeframes(struct.pack(f"<{i1 - i0}h", *frames[i0:i1]))
    return out_path


def rms_levels(path, window_s=0.5):
    """Coarse loudness map used by the deck view."""
    rate, channels, frames = load_wav(path)
    step = int(rate * channels * window_s)
    levels = []
    for i in range(0, len(frames) - step, step):
        chunk = frames[i:i + step]
        acc = sum(x * x for x in chunk) / len(chunk)
        levels.append(acc ** 0.5 / 32768.0)
    return levels

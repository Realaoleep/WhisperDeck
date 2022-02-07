"""Wav loading and trimming (stdlib only)."""

import struct
import wave


def load_wav(path):
    with wave.open(path, "rb") as w:
        rate = w.getframerate()
        channels = w.getnchannels()
        raw = w.readframes(w.getnframes())
    frames = list(struct.unpack(f"<{len(raw) // 2}h", raw))
    return rate, channels, frames


def trim(path, out_path, start_s, end_s):
    rate, channels, frames = load_wav(path)
    i0 = int(start_s * rate * channels)
    i1 = min(len(frames), int(end_s * rate * channels))
    with wave.open(out_path, "wb") as w:
        w.setnchannels(channels); w.setsampwidth(2); w.setframerate(rate)
        w.writeframes(struct.pack(f"<{i1 - i0}h", *frames[i0:i1]))
    return out_path

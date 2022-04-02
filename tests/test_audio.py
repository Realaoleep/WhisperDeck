"""Basic wav helper tests (synthetic file, no assets needed)."""

import struct, wave

from whisperdeck.audio import load_wav, trim, rms_levels


def _mk(path, rate=8000, secs=1.0):
    n = int(rate * secs)
    frames = [int(8000 * ((i % 40) / 40 - 0.5)) for i in range(n)]
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate)
        w.writeframes(struct.pack(f"<{n}h", *frames))
    return path


def test_load(tmp_path):
    p = _mk(tmp_path / "a.wav")
    rate, ch, frames = load_wav(p)
    assert rate == 8000 and ch == 1 and len(frames) == 8000

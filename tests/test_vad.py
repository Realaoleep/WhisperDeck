"""VAD window sanity on a synthetic clip."""

import struct, wave

from whisperdeck.vad import speech_windows, total_speech_seconds


def _mk(path, rate=8000, secs=2.0, loud_until=1.0):
    n = int(rate * secs)
    frames = []
    for i in range(n):
        amp = 30000 if i < rate * loud_until else 200
        frames.append(amp * ((i % 20) / 20 - 0.5))
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate)
        w.writeframes(struct.pack(f"<{n}h", *frames))
    return path


def test_windows(tmp_path):
    p = _mk(tmp_path / "v.wav")
    wins = speech_windows(p)
    assert wins and wins[0][0] < 0.5
    assert total_speech_seconds(p) > 0

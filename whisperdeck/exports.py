"""Export decks and segment lists to srt / vtt / markdown."""

from pathlib import Path


def _stamp_srt(t):
    h = int(t // 3600)
    m = int(t % 3600 // 60)
    s = int(t % 60)
    ms = int((t - int(t)) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def _stamp_vtt(t):
    return _stamp_srt(t).replace(",", ".")


def segments_to_srt(segments):
    out = []
    for i, (start, end, text) in enumerate(segments, 1):
        out.append(str(i))
        out.append(f"{_stamp_srt(start)} --> {_stamp_srt(end)}")
        out.append(text)
        out.append("")
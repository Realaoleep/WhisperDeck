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
    return "\n".join(out)


def segments_to_vtt(segments):
    out = ["WEBVTT", ""]
    for start, end, text in segments:
        out.append(f"{_stamp_vtt(start)} --> {_stamp_vtt(end)}")
        out.append(text)
        out.append("")
    return "\n".join(out)


def segments_to_md(segments):
    out = ["| start | text |", "|---|---|"]
    for start, _, text in segments:
        out.append(f"| {_stamp_vtt(start)} | {text} |")
    return "\n".join(out)


def export_deck(deck, out_path, fmt="srt"):
    """Export that concatenates per-file segment lists."""
    writers = {"srt": segments_to_srt, "vtt": segments_to_vtt, "md": segments_to_md}
    if fmt not in writers:
        raise ValueError(f"unknown format {fmt}")
    Path(out_path).write_text(writers[fmt]([]), "utf-8")
    return out_path

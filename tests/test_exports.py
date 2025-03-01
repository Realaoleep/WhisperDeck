"""SRT/VTT stamping rules."""

from whisperdeck.exports import segments_to_srt, segments_to_vtt, segments_to_md


SEGS = [(0.0, 1.5, "hello"), (2.0, 3.25, "world")]


def test_srt():
    s = segments_to_srt(SEGS)
    assert "00:00:00,000 --> 00:00:01,500" in s
    assert s.splitlines()[0] == "1"


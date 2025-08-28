"""Tag sidecar round-trip."""

from whisperdeck.tags import read_tags, write_tags, add_tag, filter_by_tag


def test_roundtrip(tmp_path):
    p = tmp_path / "memo.wav"
    p.write_bytes(b"RIFF")
    write_tags(p, ["podcast", "draft"], notes="first pass")
    data = read_tags(p)
    assert data["tags"] == ["draft", "podcast"]
    add_tag(p, "podcast")
    assert read_tags(p)["tags"].count("podcast") == 1


def test_filter(tmp_path):
    a = tmp_path / "a.wav"; b = tmp_path / "b.wav"
    for x in (a, b):
        x.write_bytes(b"RIFF")
    write_tags(a, ["keep"]); write_tags(b, ["drop"])
    assert filter_by_tag([a, b], "keep") == [a]

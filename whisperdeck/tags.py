"""Free-form tag bookkeeping for deck items (stored sidecar json)."""

import json
from pathlib import Path


def sidecar_for(audio_path):
    p = Path(audio_path)
    return p.with_suffix(".wd.json")


def read_tags(audio_path):
    sc = sidecar_for(audio_path)
    if not sc.exists():
        return {"tags": [], "notes": ""}
    return json.loads(sc.read_text("utf-8"))


def write_tags(audio_path, tags, notes=""):
    sc = sidecar_for(audio_path)
    sc.write_text(json.dumps({"tags": sorted(set(tags)), "notes": notes},
                             indent=2), "utf-8")
    return sc


def add_tag(audio_path, tag):
    data = read_tags(audio_path)
    data["tags"].append(tag)
    write_tags(audio_path, data["tags"], data.get("notes", ""))


def filter_by_tag(paths, tag):
    return [p for p in paths if tag in read_tags(p).get("tags", [])]

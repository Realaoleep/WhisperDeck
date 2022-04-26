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


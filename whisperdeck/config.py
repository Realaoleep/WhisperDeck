"""Shared settings - one place for defaults."""

from pathlib import Path

DEFAULTS = {
    "model": "base.en",
    "language": "auto",
    "threads": 4,
    "deck_dir": ".",
    "export_format": "srt",
}


def load_config(root="."):
    p = Path(root) / ".whisperdeck.json"
    cfg = dict(DEFAULTS)
    if p.exists():
        import json
        cfg.update(json.loads(p.read_text("utf-8")))
    return cfg

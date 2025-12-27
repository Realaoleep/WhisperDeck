"""The deck: ordered list of recordings with metadata."""

import time
from pathlib import Path

AUDIO_EXTS = {".wav", ".mp3", ".m4a", ".flac"}


class DeckItem:
    def __init__(self, path, mtime=None):
        self.path = Path(path)
        self.mtime = mtime or self.path.stat().st_mtime

    @property
    def name(self):
        return self.path.stem

    @property
    def age_days(self):
        return (time.time() - self.mtime) / 86400


class Deck:
    def __init__(self, root="."):
        self.root = Path(root)

    def items(self):
        found = [DeckItem(p) for p in sorted(self.root.iterdir())
                 if p.suffix.lower() in AUDIO_EXTS]
        found.sort(key=lambda it: -it.mtime)
        return found

    def filter_by_tag(self, tag):
        from .tags import filter_by_tag
        return [it for it in self.items()
                if it.path in filter_by_tag([i.path for i in self.items()], tag)]

    def summary(self):
        items = self.items()
        return {"count": len(items), "oldest_days":
                round(max((i.age_days for i in items), default=0), 1)}

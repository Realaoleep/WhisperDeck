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
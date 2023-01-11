"""Registry/binary lookup without running whisper itself."""

import pytest

from whisperdeck.transcribe import TranscribeError, find_binary, transcribe_file
from whisperdeck.models import REGISTRY, suggest_model


def test_missing_binary(monkeypatch):
    monkeypatch.setenv("PATH", "")
    with pytest.raises(TranscribeError):
        find_binary()


def test_missing_model(tmp_path, monkeypatch):
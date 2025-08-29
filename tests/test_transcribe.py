"""Registry/binary lookup without running whisper itself."""

import pytest

from whisperdeck.transcribe import TranscribeError, find_binary, transcribe_file
from whisperdeck.models import REGISTRY, suggest_model


def test_missing_binary(monkeypatch):
    monkeypatch.setenv("PATH", "")
    with pytest.raises(TranscribeError):
        find_binary()


def test_missing_model(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    with pytest.raises(TranscribeError):
        transcribe_file("x.wav")


def test_suggest():
    assert suggest_model(30) in REGISTRY
    assert suggest_model(7200) in REGISTRY

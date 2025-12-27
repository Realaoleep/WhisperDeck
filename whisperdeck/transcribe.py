"""Thin, honest wrapper around a local whisper.cpp binary."""

import shutil
import subprocess
from pathlib import Path


class TranscribeError(Exception):
    pass


def find_binary():
    for name in ("whisper-cli", "main", "whisper"):
        path = shutil.which(name)
        if path:
            return path
    raise TranscribeError(
        "whisper.cpp binary not found on PATH "
        "(see docs/model-zoo.md for build instructions)")


def transcribe_file(wav_path, model="base.en", language="auto", threads=4):
    """Run whisper.cpp on a wav and return plain text."""
    binary = find_binary()
    model_path = Path("models") / f"ggml-{model}.bin"
    if not model_path.exists():
        raise TranscribeError(f"model not found: {model_path} - run "
                              "models/download.py first")
    cmd = [binary, "-m", str(model_path), "-t", str(threads),
           "-nt", "-np", str(wav_path)]
    if language != "auto":
        cmd += ["-l", language]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise TranscribeError(proc.stderr.strip()[:400])
    return proc.stdout.strip()


def transcribe_segments(wav_path, **kw):
    """Return [(start_s, end_s, text), ...] parsed from -oj output."""
    import json
    binary = find_binary()
    model_path = Path("models") / f"ggml-{kw.get('model', 'base.en')}.bin"
    proc = subprocess.run(
        [binary, "-m", str(model_path), "-oj", "-of", "-", str(wav_path)],
        capture_output=True, text=True)
    if proc.returncode != 0:
        raise TranscribeError(proc.stderr.strip()[:400])
    data = json.loads(proc.stdout)
    segs = []
    for s in data.get("transcription", []):
        ts = s.get("timestamps", {})
        segs.append((_parse_ts(ts.get("from")), _parse_ts(ts.get("to")),
                     s.get("text", "").strip()))
    return segs


def _parse_ts(stamp):
    if not stamp or "--" in stamp:
        return 0.0
    h, m, rest = stamp.split(":")
    sec, ms = rest.split(",")
    return int(h) * 3600 + int(m) * 60 + int(sec) + int(ms) / 1000.0

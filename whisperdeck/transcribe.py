"""Run a local whisper.cpp binary on one file."""

import subprocess


def transcribe_file(wav_path, model="base.en"):
    cmd = ["main", "-m", f"models/ggml-{model}.bin", "-nt", "-np", wav_path]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.stdout.strip()

#!/usr/bin/env python3
"""Fetch a ggml whisper model into models/."""

import argparse
import sys
import urllib.request
from pathlib import Path

BASE = "https://huggingface.co/ggerganov/whisper.cpp/resolve/main"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="base.en")
    args = ap.parse_args()

    out = Path("models") / f"ggml-{args.model}.bin"
    if out.exists():
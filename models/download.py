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
        print(f"already have {out}")
        return 0
    url = f"{BASE}/ggml-{args.model}.bin"
    print(f"fetching {url}")
    out.parent.mkdir(exist_ok=True)
    urllib.request.urlretrieve(url, out)
    print(f"saved {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

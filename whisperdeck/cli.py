"""wd - the WhisperDeck command line interface."""

import argparse
import sys

from .audio import duration_seconds
from .tags import read_tags
from .deck import Deck
from .exports import export_deck


def main(argv=None):
    ap = argparse.ArgumentParser(prog="wd")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_deck = sub.add_parser("deck", help="list recordings in a deck")
    p_deck.add_argument("--dir", default=".")
    p_deck.add_argument("--tag", default=None)

    p_tr = sub.add_parser("transcribe", help="transcribe one file")
    p_tr.add_argument("wav")
    p_tr.add_argument("--model", default="base.en")
    p_tr.add_argument("--language", default="auto")

    p_ex = sub.add_parser("export", help="export a deck to srt/vtt/md")
    p_ex.add_argument("out")
    p_ex.add_argument("--format", choices=["srt", "vtt", "md"], default="srt")

    args = ap.parse_args(argv)

    if args.cmd == "deck":
        deck = Deck(args.dir)
        for item in deck.items():
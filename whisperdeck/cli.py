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
            tags = read_tags(item.path).get("tags", [])
            label = f" [{','.join(tags)}]" if tags else ""
            print(f"{item.path.name}  {duration_seconds(item.path):7.1f}s{label}")
        return 0

    if args.cmd == "transcribe":
        from .transcribe import transcribe_file
        text = transcribe_file(args.wav, model=args.model, language=args.language)
        print(text)
        return 0

    if args.cmd == "export":
        deck = Deck(".")
        export_deck(deck, args.out, fmt=args.format)
        print(f"wrote {args.out}")
        return 0


if __name__ == "__main__":
    sys.exit(main())

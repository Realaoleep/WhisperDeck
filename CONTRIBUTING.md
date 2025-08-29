# Contributing

Small project, few rules:

- `make test` before every push - CI mirrors it.
- One topic per PR; keep diffs focused.
- Stdlib only in `whisperdeck/` (dev deps for tests are fine).
- Commit style: `area: change` prefixes, present tense.
- `pre-commit run --all-files` if you touch formatting hooks.

Bug reports: open an issue with the wav properties (rate/channels/width)
and the whisper.cpp build you use.

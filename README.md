# WhisperDeck

![ci-python](https://github.com/Realaoleep/WhisperDeck/actions/workflows/ci-python.yml/badge.svg)
![license](https://img.shields.io/badge/license-MIT-blue.svg)
![python](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![platform](https://img.shields.io/badge/platform-local-green.svg)

**On-device audio transcription toolkit** - a Python engine plus a small
Android demo app. Trim, tag, transcribe and export your recordings.
Everything runs locally: audio never leaves the machine.

## Why this exists

I record a lot of voice memos and wanted one tool that could trim them, tag
them, and turn them into searchable text without uploading anything to a
server. WhisperDeck is that tool: a *deck* of recordings, transcribed on
device with a local [whisper.cpp](https://github.com/ggerganov/whisper.cpp)
build.

## Features

| | |
|---|---|
| **Local-first** | one-time model download is the only network call, ever |
| **Trim + tag** | wav trimming, VAD-based speech windows, sidecar tags |
| **Transcribe** | whisper.cpp wrapper with segment timestamps |
| **Model zoo** | tiny → large-v3, picked per clip length |
| **Export** | SRT, WebVTT and markdown tables |
| **Android demo** | foreground recorder service + deck browser |

## Layout

```
whisperdeck/    the Python engine (CLI + library)
app/            minimal Android demo that records and lists a deck
models/         whisper model helpers and download script
docs/           guides (getting started, model zoo, shortcuts, exports)
examples/       end-to-end recipes (podcast notes, meeting minutes)
```

## Quick start

```console
$ pip install -e .
$ wd deck list
$ wd transcribe memo.wav --model base.en
$ wd export deck.srt --format srt
```

The Android demo lives in `app/` - open it in Android Studio, run it on a
device, and recordings land straight in a deck.

## Requirements

- Python 3.9+
- a `whisper.cpp` binary on PATH (see [docs/model-zoo.md](docs/model-zoo.md))
- Android Studio (only for the demo app)

## Contributing

PRs welcome - see [CONTRIBUTING.md](CONTRIBUTING.md). Keep `whisperdeck/`
stdlib-only; run `make test` before pushing.

## License

MIT - see [LICENSE](LICENSE).

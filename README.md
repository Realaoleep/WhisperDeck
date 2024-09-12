# WhisperDeck

**On-device audio transcription toolkit** - a Python engine plus a small
Android demo app. Trim, tag, transcribe and export your recordings.
Everything runs locally: audio never leaves the machine.

## Why this exists

I record a lot of voice memos and wanted one tool that could trim them, tag
them, and turn them into searchable text without uploading anything to a
server. WhisperDeck is that tool: a *deck* of recordings, transcribed on
device with a local whisper.cpp build.

## Layout

```
whisperdeck/    the Python engine (CLI + library)
app/            minimal Android demo that records and lists a deck
models/         whisper model helpers and download script
docs/           guides
```

## Quick start

```
pip install -e .
wd deck list
wd transcribe memo.wav --model base.en
```

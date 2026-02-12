# Getting started

1. Build or install a `whisper.cpp` binary (see [model-zoo.md](model-zoo.md)).
2. `pip install -e .` inside the repo.
3. Drop some wav files in a folder - that folder is your deck.
4. `wd deck list` shows recordings with durations and tags.
5. `wd transcribe memo.wav --model base.en` prints text.
6. `wd export deck.srt --format srt` writes subtitles.

Everything stays local: the only network call ever made is the one-time

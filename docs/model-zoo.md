# Model zoo

- Default is `base.en`; change per-call with `--model`.
- `suggest_model()` picks by clip length when you pass `quality=fast|balanced|max`.
- Multilingual clips: pass `--language auto` (default) or an ISO code.
- RAM guide: base ~500 MB, small ~1 GB, medium ~2.8 GB, large-v3 ~5.2 GB.

Build whisper.cpp with `-DWHISPER_BUILD_TESTS=OFF` if you only need the CLI.

# Export formats

| format | writer | use |
|---|---|---|
| `srt` | `segments_to_srt` | subtitles, video editing |
| `vtt` | `segments_to_vtt` | web players |
| `md` | `segments_to_md` | notes apps, plain-text archives |

Stamps are hour-anchored (`00:00:00,000` style); vtt swaps the comma for a
dot per spec.

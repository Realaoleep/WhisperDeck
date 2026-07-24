# Models

WhisperDeck does not bundle weights. Download ggml models with:

```
python models/download.py --model base.en
```

| model | size | params | notes |
|---|---|---|---|
| tiny.en | 75 MB | 39M | fast drafts, weak punctuation |
| base.en | 142 MB | 74M | **default** - good balance |
| small.en | 466 MB | 244M | noticeably better on accents |
| medium.en | 1.5 GB | 769M | slow on phones, fine on desktop |
| large-v3 | 2.9 GB | 1550M | multilingual, needs 5+ GB RAM |

Models land in `models/` and are git-ignored.

# Models

WhisperDeck does not bundle weights. Download ggml models with:

```
python models/download.py --model base.en
```

| model | size | params | notes |
|---|---|---|---|
| tiny.en | 75 MB | 39M | fast drafts, weak punctuation |
| base.en | 142 MB | 74M | **default** - good balance |
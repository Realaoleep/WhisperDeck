"""Model registry - what models exist and where they land."""

from pathlib import Path

REGISTRY = {
    "tiny.en":   {"size_mb": 75,   "params": "39M",   "vram_mb": 390},
    "base.en":   {"size_mb": 142,  "params": "74M",   "vram_mb": 500},
    "small.en":  {"size_mb": 466,  "params": "244M",  "vram_mb": 1000},
    "medium.en": {"size_mb": 1500, "params": "769M",  "vram_mb": 2800},
    "large-v3":  {"size_mb": 2900, "params": "1550M", "vram_mb": 5200},
}


def model_path(name):
    return Path("models") / f"ggml-{name}.bin"


def installed_models():
    found = []
    for name in REGISTRY:
        p = model_path(name)
        if p.exists() and p.stat().st_size > 1_000_000:
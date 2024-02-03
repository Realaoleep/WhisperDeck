"""Energy-based voice activity detection for pre-trim."""

from .audio import rms_levels


def speech_windows(path, threshold=0.04, pad_s=0.4):
    """Return [(start_s, end_s)] spans above the RMS threshold."""
    levels = rms_levels(path, window_s=0.25)
    windows = []
    open_at = None
    for i, level in enumerate(levels):
        t0, t1 = i * 0.25, (i + 1) * 0.25
        if level >= threshold and open_at is None:
            open_at = max(0.0, t0 - pad_s)
        elif level < threshold and open_at is not None:
            windows.append((open_at, t1 + pad_s))
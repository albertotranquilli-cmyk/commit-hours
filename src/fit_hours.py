#!/usr/bin/env python3
"""Fit a repository's event-hour histogram as a mixture of national work-hour profiles.

Templates (hour-of-week, UTC, 0=Mon 00:00 .. 167=Sun 23:00):
  US:  peak 13-21 UTC (9-17 ET) on weekdays
  CN:  peak 01-09 UTC (9-17 CST) on weekdays
  EU:  peak 07-15 UTC (9-17 CET) on weekdays
  JP:  peak 00-08 UTC (9-17 JST) on weekdays
  OTHER: flat

Fit: non-negative least squares. Output: weights per timezone.

This is a stub: implement after data is available.
"""
import numpy as np

HOURS = 24 * 7


def template(offset_utc, width=8):
    """Rectangular work-hour window starting at offset_utc (UTC hour), width hours, weekdays only."""
    t = np.zeros(HOURS)
    for day in range(5):  # Mon-Fri
        for h in range(width):
            t[day * 24 + (offset_utc + h) % 24] = 1.0
    return t / t.sum()


TEMPLATES = {
    "US": template(13),   # 9-17 ET
    "CN": template(1),    # 9-17 CST
    "EU": template(7),    # 9-17 CET
    "JP": template(0),    # 9-17 JST
    "OTHER": np.ones(HOURS) / HOURS,
}


def fit(hist):
    """hist: array of length 168 (hour-of-week counts). Return dict of weights."""
    A = np.column_stack([TEMPLATES[k] for k in TEMPLATES])
    # non-negative least squares
    try:
        from scipy.optimize import nnls
        w, _ = nnls(A, hist.astype(float))
    except ImportError:
        # fallback: normalized projection
        w = np.maximum(A.T @ hist.astype(float), 0)
    w = w / w.sum() if w.sum() > 0 else w
    return {k: round(float(v), 4) for k, v in zip(TEMPLATES, w)}


if __name__ == "__main__":
    # sanity: a pure-CN histogram should return CN ~ 1
    import numpy as np
    h = TEMPLATES["CN"] * 1000
    print(fit(h))
    h = TEMPLATES["US"] * 1000
    print(fit(h))

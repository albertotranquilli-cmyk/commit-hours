# PLAN.md — commit-hours roadmap

Status: 2026-10-05.

## Step 0 — scaffold (done)

## Step 1 — fit_hours.py

Non-negative least squares mixture fit of hour-of-week histograms against national work-hour templates. Templates: US (ET), CN (CST), EU (CET), JP (JST), plus a flat "other" component.

## Step 2 — data

Reuse GH Archive (same as tiaoxiu-signal) or the GitHub Events API. The 6 raw make-up days from tiaoxiu-signal's load_raw.py can also feed this: event hours on those days are pure CN-workday hours.

## Step 3 — validate

Known-CN repos (high tiaoxiu s) should show high CN weight. Known-US repos (AWS, Mozilla) should show high US weight. Japanese repos should show JP weight with zero CN.

## Step 4 — cross-correlate with tiaoxiu-signal

Spearman rank correlation between CN mixture weight and s. Target: strong positive correlation, which would mean two independent instruments agree.

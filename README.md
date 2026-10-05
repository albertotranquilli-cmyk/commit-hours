# commit-hours

**Git commit and event timestamps as a quantitative attribution signal.**

Status: scaffold 2026-10-05. No results yet.

## The idea

Every public GitHub event carries a UTC timestamp. Commit hours cluster around the author's local working hours. For repositories with known geography (e.g., a repo whose maintainers are all in one country), the hour-of-day distribution of events is a **fingerprint of that country's work schedule**.

Reverse the logic: for any repository, fit its event-hour distribution as a mixture of known national work-hour profiles (US 9-17 ET, China 9-17 CST, EU 9-17 CET, Japan 9-17 JST). The mixture weights are an estimate of the **share of activity attributable to each timezone's work pattern** — without geolocating a single person.

This is the same family as tiaoxiu-signal but goes further: it estimates a **full distribution** (multiple timezones simultaneously) rather than a single binary (China vs not-China). Applications: supply-chain risk (which timezones touch a dependency), incident response (when did the attacker likely work), and open-source diversity measurement that needs no personal data.

## Method

1. Fetch public events for a repo via the GitHub Events API (no key for low volume; with a token for scale) or GH Archive.
2. Build hour-of-week histograms per repo.
3. Fit a mixture model: weights for {US, CN, EU, JP, other} work-hour profiles. Use non-negative least squares or EM.
4. Validate on repos with known geography (Apache projects with known CN contributor bases, AWS/Mozilla as US controls).
5. Compare mixture weights with tiaoxiu-signal s values: repos with high s should have high CN weight.

## Ethics

Aggregate event timestamps only. No commit messages, no author names, no emails. Timestamps are public by design (git is content-addressed and public).

## Next steps

1. Implement the mixture fit (src/fit_hours.py).
2. Run on the tiaoxiu-signal eligible set (~3,600 repos) using GH Archive.
3. Cross-validate against tiaoxiu-signal s.
4. Paper: "Work-hour mixture models from public event timestamps".

# develop → test diff package — TSR 1632 (frontend)

- **when**: 2026-07-15T16:13:09Z
- **stream**: frontend
- **develop**: `e837185` CLEAN
- **test (before)**: `5843845`
- **test (after FF)**: `e837185`
- **pending**: 1 → 0
- **range**: `5843845..e837185`
- **subject**: fix(v1.2.1/G-RFID): harden dispatch candidate payload parsing

## Commits
e837185 fix(v1.2.1/G-RFID): harden dispatch candidate payload parsing

## Files
 .../visits/VisitRfidDiffComparePanel.jsx           | 25 ++++++++++++++++++++--
 .../visits/VisitRfidDiffComparePanel.test.jsx      | 25 ++++++++++++++++++++++
 2 files changed, 48 insertions(+), 2 deletions(-)

## Summary
Accept snake_case and serialized dispatch candidate payloads so VisitRfidDiffComparePanel exposes care-provision SMS batch targets across BE response shapes. +related tests in VisitRfidDiffComparePanel.test.jsx.

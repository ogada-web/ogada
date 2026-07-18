# develop→test diff · TSR1606 · QA-B445

- range: `9b65529..33f59a9`
- commit: `33f59a9 fix(v1.2.1/QA-B95): harden live readiness boolean parsing`
- files: `liveBackendProbe.js` · `liveE2eHarness.test.js`
- related: **129/129 PASS** (1.43s)
commit 33f59a9a2a61e6440f4e8ee472a53f5054d5258d
Author: jwj3400 <rlwlsdnr@naver.com>
Date:   Wed Jul 15 08:18:21 2026 +0000

    fix(v1.2.1/QA-B95): harden live readiness boolean parsing
    
    Parse trimmed and case-insensitive boolean strings in live health readiness fields so QA-B95 gating remains stable across backend payload format variations.
    
    Co-authored-by: Cursor <cursoragent@cursor.com>

 src/e2e/liveBackendProbe.js     | 14 +++++++++++++-
 src/test/liveE2eHarness.test.js | 24 ++++++++++++++++++++++++
 2 files changed, 37 insertions(+), 1 deletion(-)

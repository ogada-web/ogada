# develop→test diff · TSR1610 · QA-B447

- range: `33f59a9..9dbdfc5`
- commit: `9dbdfc5 fix(v1.2.1/QA-B95): unwrap bracketed operation blocker tokens`
- files: `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` · `liveE2eHarness.test.js`
- related: **131/131 PASS** (1.45s)
commit 9dbdfc5bc3f4029fe7490e2a79d32143716ebed6
Author: jwj3400 <rlwlsdnr@naver.com>
Date:   Wed Jul 15 09:05:00 2026 +0000

    fix(v1.2.1/QA-B95): unwrap bracketed operation blocker tokens
    
    Normalize bracketed and quoted composite operation blocker tokens in live-e2e probe/config/setup so QA-B95 diagnostics stay fail-closed across backend payload shape variations (BE parity @e7efe02).
    
    Co-authored-by: Cursor <cursoragent@cursor.com>

 src/e2e/liveBackendProbe.js     | 111 ++++++++++++++++++++++++++++++----------
 src/e2e/liveConfig.js           |  48 ++++++++++++++---
 src/e2e/liveGlobalSetup.js      |  40 +++++++++++++--
 src/test/liveE2eHarness.test.js |  44 ++++++++++++++++
 4 files changed, 206 insertions(+), 37 deletions(-)

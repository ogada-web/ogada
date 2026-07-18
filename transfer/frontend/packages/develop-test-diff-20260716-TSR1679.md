commit 83e6296a0fb376a01491b2c691078c9bc4329368
Author: jwj3400 <rlwlsdnr@naver.com>
Date:   Thu Jul 16 04:26:49 2026 +0000

    fix(v1.2.1/QA-B95): decode soft-hyphen and whitespace HTML entities
    
    Align frontend blocker parsing with backend @c67c7ed so mid-token soft hyphens and nbsp/ensp/emsp/thinsp whitespace entities stay fail-closed across readiness and live harness flows.
    
    Co-authored-by: Cursor <cursoragent@cursor.com>

 src/config/notificationChannelStatus.js      | 21 ++++++++++++---
 src/config/notificationChannelStatus.test.js | 23 ++++++++++++++++
 src/e2e/liveBackendProbe.js                  | 21 ++++++++++++---
 src/e2e/liveConfig.js                        | 18 +++++++++++--
 src/e2e/liveGlobalSetup.js                   | 18 +++++++++++--
 src/test/liveE2eHarness.test.js              | 40 ++++++++++++++++++++++++++++
 6 files changed, 131 insertions(+), 10 deletions(-)

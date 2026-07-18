<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-14T15:43:55+00:00 -->
# develop→test diff TSR 1557 — `5805d68`..`3bd50ac`

> **1557차 PASS(FE)** — FF merge `5805d68`→`3bd50ac` · related **64/64** · npm **2459/2459** · build **1217** · live **116/33/0** · origin/test **PUSHED** · Open **0** · cross-stream **SYNCED(BE `@5d6c007`)** · operation **BLOCK**(634 BE)

## Commits

```
3bd50ac feat(v1.2.1/G2): wire home newsletter authoring compose preview
```

## Diffstat

```
 src/api/billingGuardianPlatformServices.test.js |  52 +++++
 src/api/services.js                             |  19 ++
 src/pages/HomeNewsletterLaunchPage.jsx          | 248 +++++++++++++++++++++++-
 src/pages/HomeNewsletterLaunchPage.test.jsx     |  96 ++++++++-
 src/utils/homeNewsletter.js                     |  83 +++++++-
 src/utils/homeNewsletter.test.js                |  50 +++++
 6 files changed, 543 insertions(+), 5 deletions(-)
```

## 검증 요약

| 항목 | 결과 |
|---|---|
| test/develop/origin/test HEAD | **ALL SYNCED `@3bd50ac`** |
| ahead (`test..develop`) | **0** (FF EXECUTED) |
| develop working tree | **CLEAN** |
| related pre-merge | **64/64 PASS** (6.04s, 3 files · reconfirm) |
| post-merge `npm test` | **2459/2459 PASS** (834.87s, 465 files) |
| `npm run build` | **1217 modules PASS** (10.38s) |
| `npm audit` (high+, omit=dev) | **0** |
| live E2E | **116 PASS / 33 SKIP / 0 FAIL** (37.63s · bootstrap-disabled · reconfirm) |
| Open QA BLOCK | **0** (QA-B400 Fixed) |
| transfer verdict | **PASS** (FE) |
| cross-stream | **SYNCED** (BE `@5d6c007` · FE `@3bd50ac`) |
| operation | **BLOCK** (QA-B116 origin/test **634 BE** + QA-B95) |

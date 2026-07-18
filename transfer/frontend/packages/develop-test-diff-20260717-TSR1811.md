<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-17T22:58:24Z -->
# frontend develop→test diff meta — TSR 1811

- updated: 2026-07-17T22:58:24Z
- merge: FF+PUSH `4691856`→`3042a53` (1 commit · ALL SYNCED+PUSHED · pending **1→0**)
- absorbed: `3042a53` — QA-B601 SEC-D34 NHIS excel pre-upload magic-byte (visit/billing/caregiver/RFID)
- files (+10 / create 2): `excelImportFiles.js`+`.test.js`, Visit/Staff/RFID/NHISImport panels+pages+tests
- develop pre-merge related: **39/39 PASS** (16.59s)
- post-merge `npm test`: **2733/2735 PASS (2 FAIL)** (897.04s, 487 files)
- FAIL:
  1. `StaffPage.test.jsx` — caregiver import preview API call count **0** (`File(["data"], caregivers.xlsx)`)
  2. `pilotPageFlows.test.jsx` — US-V04 visit NHIS import POST never fired (`File(["data"], visits.xlsx)`)
- root cause: page/pilot fixtures lack OOXML `PK\x03\x04` magic → SEC-D34 `validate*ExcelImportFile` reject (same residual pattern as QA-B597)
- expected COD fix: sync fixtures to `Uint8Array([0x50,0x4b,0x03,0x04,0x14,0x00,0x06,0x00])` like panel/config tests; optional MIME spoof lock
- build: **1234** modules (9.35s) PASS
- audit: **0** high PASS
- live E2E: SKIP (suite FAIL)
- transfer verdict: **BLOCK** (Open QA-20260717-B602)
- cross-stream: BE pending 1 `@a788e6d` (Open QA-B600) · origin/test..develop **743**

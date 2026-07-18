<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-17T23:03:32Z -->
# TSR 1812 — frontend revalidation (QA-B602 still Open)

- **stream**: frontend
- **SHA**: develop/test/origin **ALL `@3042a53`** (pending **0**, WT **CLEAN**)
- **merge**: SKIP (already SYNCED · no new develop commits since TSR1811)
- **full suite**: SKIP (carry TSR1811 **2733/2735 · 2 FAIL** · Open B602 우선)
- **targeted revalidation** (src/frontend-test @ test):
  1. `StaffPage.test.jsx` › NHIS caregiver import — **1 FAIL** (5.47s) — `previewSpy` 0 calls · L231 `File(["data"], "caregivers.xlsx")`
  2. `pilotPageFlows.test.jsx` › US-V04 visit NHIS excel — **1 FAIL** (9.84s) — `POST /visits/imports/nhis` never · L4524 `File(["data"], "visits.xlsx")`
- **build/audit/live**: carry TSR1811 (1234 / 0 / SKIP)
- **Open**: QA-20260717-B602 HIGH/BLOCK (unchanged · COD fixture sync 대기)
- **transfer**: **BLOCK**
- **cross-stream**: FE Open B602 · BE pending 1 `@a788e6d` Open B600 · origin/test..develop **743** BE
- **operation**: **BLOCK** (743 BE + QA-B95 + QA-B602 + QA-B600)

## COD action (우선)

```js
// StaffPage.test.jsx L231 · pilotPageFlows.test.jsx L4524
new File([new Uint8Array([0x50, 0x4b, 0x03, 0x04, 0x14, 0x00, 0x06, 0x00])], "….xlsx", {
  type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
})
```

참고: `VisitNhisImportPanel.test.jsx` / `excelImportFiles.test.js` / QA-B597 page fixture.

잔여 후보(비-FAIL carry): `BankDepositImportPanel.test.jsx` `File(["data"], "bank.xlsx")` — magic 게이트 적용 시 동일 패턴.

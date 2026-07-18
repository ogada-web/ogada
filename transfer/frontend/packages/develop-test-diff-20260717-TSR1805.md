<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-17T21:01:28Z -->
# frontend develop→test diff meta — TSR 1805

- updated: 2026-07-17T21:01:28Z
- merge: FF `e16f432`→`cf28a2e` (1 commit · ALL SYNCED+PUSHED · pending **1→0**)
- commits:
  - `cf28a2e` fix(v1.2.1/v3): verify benefit-contract and staff-HR magic bytes before upload (SEC-D25 · QA-B594)
- files: 9 (+419/−35)
- related: 22/22 PASS (benefitContractAttachments+staffHrFiles+StaffHrFilePanel+ClientBenefitContractPanel · 6.10s · +9 vs TSR1803)
- post-merge npm: 2723/2723 PASS (886.76s, 485 files · +8 vs TSR1803 2715)
- build: 1233 modules PASS (9.32s · Δ0 modules)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (34.16s · bootstrap-disabled)
- origin/test: ALL SYNCED+PUSHED `@cf28a2e`
- QA: QA-20260717-B594 Fixed · Open 0(FE) · cross-stream SYNCED(BE `@324da07` · FE `@cf28a2e`) · origin/test BE **740** unpushed

## Diffstat
```
 .../ClientBenefitContractAttachmentPanel.jsx       |   2 +-
 .../staff/StaffDocumentRepositoryPanel.jsx         |   2 +-
 .../staff/StaffDocumentRepositoryPanel.test.jsx    |   3 +-
 src/components/staff/StaffHrFilePanel.jsx          |   2 +-
 src/components/staff/StaffHrFilePanel.test.jsx     |   3 +-
 src/config/benefitContractAttachments.js           | 139 ++++++++++++++++++---
 src/config/benefitContractAttachments.test.js      |  85 +++++++++++++
 src/config/staffHrFiles.js                         | 136 +++++++++++++++++---
 src/config/staffHrFiles.test.js                    |  82 ++++++++++++
 9 files changed, 419 insertions(+), 35 deletions(-)
```

## Notes
- QA-B594: FE SEC-D25 benefit-contract PDF/PNG + staff-HR PDF/PNG/JPEG FileReader 8-byte magic + Content-Type `;param` normalize · `ClientBenefitContractAttachmentPanel`·`StaffHrFilePanel`·`StaffDocumentRepositoryPanel` await validate (BE QA-B593 `@324da07` lockstep).
- Verification SHA identical on develop / test / origin/test / origin/develop · tests measured at `@cf28a2e`.
- operation BLOCK: origin/test push **740 BE** + QA-B95.

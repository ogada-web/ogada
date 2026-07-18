# develop→test diff meta — TSR1595 frontend
generated: 2026-07-15T05:05:41Z
range: 7d9dd70..2da7ead
merge: FF EXECUTED + origin/test PUSHED (ALL SYNCED)
---
2da7ead feat(v1.2.1/US-V06): wire monthly visit batch-unconfirm panel
---
 src/api/services.js                                |  13 +
 src/api/visitServices.test.js                      |  37 ++
 src/components/visits/VisitBatchUnconfirmPanel.jsx | 384 +++++++++++++++++++++
 .../visits/VisitBatchUnconfirmPanel.test.jsx       | 255 ++++++++++++++
 src/pages/VisitsPage.jsx                           |  18 +
 src/pages/VisitsPage.test.jsx                      |  67 ++++
 6 files changed, 774 insertions(+)

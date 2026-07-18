commit b42174aaea4b1e5e61684eb962df29832eef46a5
Author:     jwj3400 <rlwlsdnr@naver.com>
AuthorDate: Thu Jul 16 03:55:08 2026 +0000
Commit:     jwj3400 <rlwlsdnr@naver.com>
CommitDate: Thu Jul 16 03:55:08 2026 +0000

    fix(v1.2.1/M12): demote SSO launch when blockers remain
    
    Keep accounting BPO SSO in planned mode when readiness blockers exist and prevent showing the SSO launch action until blockers clear. This closes QA-B490 and locks the behavior with utility and page regressions.
    
    Co-authored-by: Cursor <cursoragent@cursor.com>

 src/pages/AccountingBpoPage.test.jsx | 36 ++++++++++++++++++++++++++++++++++++
 src/utils/accountingBpo.js           | 22 ++++++++++++----------
 src/utils/accountingBpo.test.js      | 21 +++++++++++++++++++++
 3 files changed, 69 insertions(+), 10 deletions(-)

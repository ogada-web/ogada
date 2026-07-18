483dfe1 fix(v1.2.1/G2): recover notice board page after mutations

commit 483dfe1094570b4658b1baddc63a0898ebcd0d72
Author: jwj3400 <rlwlsdnr@naver.com>
Date:   Thu Jul 16 02:58:39 2026 +0000

    fix(v1.2.1/G2): recover notice board page after mutations
    
    Prevent facility-notices board from staying on a stale empty page after publish/delete by reconciling to the last valid page, and add regression coverage for page fallback after deleting the final row.
    
    Co-authored-by: Cursor <cursoragent@cursor.com>

 src/pages/HomeNewsletterLaunchPage.jsx      | 26 +++++++--
 src/pages/HomeNewsletterLaunchPage.test.jsx | 82 +++++++++++++++++++++++++++++
 2 files changed, 103 insertions(+), 5 deletions(-)

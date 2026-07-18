diff --git a/src/e2e/liveConfig.js b/src/e2e/liveConfig.js
index 0a584eb..84a674c 100644
--- a/src/e2e/liveConfig.js
+++ b/src/e2e/liveConfig.js
@@ -54,6 +54,13 @@ export function isLiveE2eEnabled() {
   return process.env.LIVE_E2E === "1" || process.env.LIVE_E2E === "true";
 }
 
+function isLiveBootstrapSuppressionAllowed() {
+  return (
+    process.env.LIVE_E2E_ALLOW_BOOTSTRAP_SUPPRESSION === "1" ||
+    process.env.LIVE_E2E_ALLOW_BOOTSTRAP_SUPPRESSION === "true"
+  );
+}
+
 function readLiveBackendProbeState() {
   try {
     if (!existsSync(LIVE_BACKEND_STATE_FILE)) {
@@ -990,6 +997,8 @@ export function getLiveE2eSkipReasons({
     : buildEffectiveOperationReadinessReason(state, operationScope);
   const bootstrapEnableHintReason =
     !operationReady && hasFreshState ? buildBootstrapEnableHintReason(state) : "";
+  const operationSuppressedByBootstrap =
+    operationReady && hasFreshState && isLiveEffectiveOperationSuppressedByBootstrap();
 
   if (requireOperationReady && !operationReady) {
     reasons.push(operationReadinessReason);
@@ -997,6 +1006,15 @@ export function getLiveE2eSkipReasons({
       reasons.push(bootstrapEnableHintReason);
     }
   }
+  if (
+    requireOperationReady &&
+    operationSuppressedByBootstrap &&
+    !isLiveBootstrapSuppressionAllowed()
+  ) {
+    reasons.push(
+      "operation readiness suppressed by bootstrap blockers (set LIVE_E2E_ALLOW_BOOTSTRAP_SUPPRESSION=1 to allow)"
+    );
+  }
 
   if (requireSafetyCheckReady && !isLiveSafetyCheckSchemaReady()) {
     reasons.push("V185 safety check schema not ready");
diff --git a/src/test/liveE2eHarness.test.js b/src/test/liveE2eHarness.test.js
index 6bda967..2da3bb0 100644
--- a/src/test/liveE2eHarness.test.js
+++ b/src/test/liveE2eHarness.test.js
@@ -45,6 +45,7 @@ function clearLiveBackendStateFile() {
 /** Shell / prior live-e2e runs may leave tokens in process.env — stub all credential keys (QA-B119). */
 const LIVE_E2E_CREDENTIAL_ENV_KEYS = [
   "LIVE_E2E",
+  "LIVE_E2E_ALLOW_BOOTSTRAP_SUPPRESSION",
   "LIVE_E2E_ACCESS_TOKEN",
   "LIVE_E2E_REFRESH_TOKEN",
   "LIVE_E2E_EMAIL",
@@ -1455,7 +1456,7 @@ describe("liveConfig skip diagnostics", () => {
     expect(reasons.some((reason) => reason.includes("guardian-bootstrap-not-ready"))).toBe(false);
   });
 
-  it("ignores bootstrap-disabled blocker when staff auth is already recovered", () => {
+  it("blocks strict operation gate when readiness is bootstrap-suppressed", () => {
     mkdirSync(dirname(LIVE_BACKEND_STATE_FILE), { recursive: true });
     writeFileSync(
       LIVE_BACKEND_STATE_FILE,
@@ -1466,7 +1467,9 @@ describe("liveConfig skip diagnostics", () => {
         checkedAt: new Date().toISOString(),
         staffAuthReady: true,
         liveE2eOperationReady: false,
-        liveE2eOperationBlockers: ["bootstrap-disabled"]
+        liveE2eOperationBlockers: ["bootstrap-disabled"],
+        liveE2eSuppressedBootstrapOperationBlockers: ["bootstrap-disabled"],
+        liveE2eEffectiveOperationSuppressedByBootstrap: true
       })
     );
     vi.stubEnv("LIVE_E2E_ACCESS_TOKEN", "staff-token");
@@ -1476,7 +1479,42 @@ describe("liveConfig skip diagnostics", () => {
       requireOperationReady: true
     });
 
-    expect(reasons.some((reason) => reason.includes("bootstrap-disabled"))).toBe(false);
+    expect(
+      reasons.some((reason) =>
+        reason.includes("operation readiness suppressed by bootstrap blockers")
+      )
+    ).toBe(true);
+  });
+
+  it("allows bootstrap-suppressed readiness when explicit override is enabled", () => {
+    mkdirSync(dirname(LIVE_BACKEND_STATE_FILE), { recursive: true });
+    writeFileSync(
+      LIVE_BACKEND_STATE_FILE,
+      JSON.stringify({
+        reachable: true,
+        ready: true,
+        skipped: false,
+        checkedAt: new Date().toISOString(),
+        staffAuthReady: true,
+        liveE2eOperationReady: false,
+        liveE2eOperationBlockers: ["bootstrap-disabled"],
+        liveE2eSuppressedBootstrapOperationBlockers: ["bootstrap-disabled"],
+        liveE2eEffectiveOperationSuppressedByBootstrap: true
+      })
+    );
+    vi.stubEnv("LIVE_E2E_ACCESS_TOKEN", "staff-token");
+    vi.stubEnv("LIVE_E2E_ALLOW_BOOTSTRAP_SUPPRESSION", "1");
+
+    const reasons = getLiveE2eSkipReasons({
+      requireStaffAuth: true,
+      requireOperationReady: true
+    });
+
+    expect(
+      reasons.some((reason) =>
+        reason.includes("operation readiness suppressed by bootstrap blockers")
+      )
+    ).toBe(false);
   });
 
   it("ignores bootstrap-unavailable blocker when staff auth is already recovered", () => {

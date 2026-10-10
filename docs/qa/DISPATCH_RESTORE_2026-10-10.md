# Dispatch authoring and menu role scope — 2026-10-10

## Result

Branch managers can open the existing manual writer, automatic pickup suggestion, saved drafts, previous-run picker and draft detail within their authorized branch. Staff still see only confirmed runs. HQ-only draft deletion and existing address/contact masking remain restricted.

- Added a visible **배차 작성** navigation item and top-of-page action. Shuttle-sheet creation and optimization links use the same manager rule.
- Restored branch-manager create/update/confirm/unconfirm and scoped optimization settings on both the frontend and backend. Existing tenant, branch, client and vehicle checks remain in place; branch responses retain masking.
- Fixed the create-request validator to accept both pickup and dropoff, matching the existing UI/service behavior.
- Made transport and shuttle date/direction filters follow the URL so same-page links and browser navigation cannot silently retain another day/direction.
- The preview now forwards only explicit authenticated dispatch operations to Spring. Dispatch deletion and unrelated writes stay blocked.
- Menu badges distinguish **공용** (staff can view), **본사·지점** (HQ and branch managers) and **본사** (HQ-only). Full labels and explanations appear at the top of each page. Menu-declared roles and route guards determine the badge; actual action permissions remain enforced by the server.

## Verification

- Backend: 58 tests pass across transport service, suggestion service and authenticated controller security. This includes branch creation, masked responses, rejection outside branch write scope, staff/retired/platform-role rejection and HQ-only deletion.
- Frontend: transport authoring, draft restoration, previous-run loading, navigation and date/direction synchronization tests pass; 62 menu/audience/mobile-shell/protected-route tests pass.
- Preview proxy: 2 tests verify exact supported paths and block unrelated writes, deletion and invalid run IDs.
- Real local preview browser: branch-manager account created and confirmed a pickup, created a dropoff draft, reopened saved runs on mobile/desktop, and verified the original two draft runs with five passengers each remained intact. Staff POST creation and draft GET return 403.
- Real browser: HQ/branch badges, restricted HQ menu visibility, one active menu and no horizontal overflow verified at 390/1440 px.
- Builds pass; compiled assets do not contain the server REST key. The private pre-change database dump is retained under `.venv/phone-preview`.

The existing HTTPS preview is updated. Local commits only; Grok automation remains stopped.

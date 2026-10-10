# Employee personal attendance and manager HR access — 2026-10-10

## Behavior

- Employees see **내 근무 → 내 출퇴근**. The personal attendance screen contains only their status/timestamps and own check-in/out controls; it does not show a coworker roster, branch attendance totals, method overrides or HR management links.
- HQ/branch managers retain the branch-wide staff attendance screen. Its badge is **범위 분리**, and the page explains that staff use their own personal screen. Employee attendance has a **본인 전용** badge.
- Full staff schedules, annual leave/leave ledger, payroll previews/settings, employee health checks, employment records/HR files, staff reports and related HR management screens are restricted to managers. Route guards, sidebar items, context navigation, dashboard links and backend controller authorization agree.
- Attendance list queries for employees load only the authenticated user and that user's attendance. Check-in/out reject a different target user before looking up or changing employee data. Self check-in uses server time and the MOBILE method.
- Existing manager read/edit distinctions, tenant/branch validation and clinical client attendance/record workflows are retained. Preview forwarding adds only the two attendance action paths; other HR writes remain blocked by the demo proxy.

## Verification

- Backend: 16 tests pass across existing attendance behavior, ownership regression and real controller security. Managers can read HR management APIs; staff, normalized legacy employee roles and platform operators cannot. Own attendance query avoids loading coworker rosters; spoofed targets and unauthorized branches are rejected.
- Frontend: 85 related tests pass; final menu/personal attendance rerun (35 tests) passes. Coverage includes malicious extra rows in a mocked response, own action payloads, removal of management links, route protection, scope labels and dashboard behavior.
- Preview path restriction tests (2) pass; frontend build/backend packaging pass; compiled assets do not include the server REST key.
- Real local preview browser: staff reads only their row, checks in/out, cannot spoof a coworker, and receives 403 from annual leave, leave ledger, health, HR files, reports, payroll catalog and manager work-log APIs. Branch manager retains full roster and management reads at 390/1440 px with no horizontal overflow.

Changes are local commits. Existing transport authoring/restored drafts and the HTTPS preview are preserved; Grok automation remains stopped.

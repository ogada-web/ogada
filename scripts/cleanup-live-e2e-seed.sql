-- Remove Live E2E bootstrap pollution from the shared dev tenant (QA-B95 / dev-backend LIVE_E2E=true).
-- Safe to re-run. Does NOT delete demo transport clients (김영희 등) or dev fixture branches.
--
-- Usage:
--   PGPASSWORD=ogada psql -h localhost -U ogada -d ogada -f scripts/cleanup-live-e2e-seed.sql

BEGIN;

UPDATE visit_schedules
   SET paired_schedule_id = NULL
 WHERE id IN (
     '00000006-0006-4000-8000-000000000001',
     '00000009-0009-4000-8000-000000000001'
 );

DELETE FROM visit_schedules
 WHERE id IN (
     '00000006-0006-4000-8000-000000000001',
     '00000009-0009-4000-8000-000000000001'
 )
    OR client_id = '00000005-0005-4000-8000-000000000001';

DELETE FROM nhis_import_rows
 WHERE id = '00000008-0008-4000-8000-000000000001'
    OR client_id = '00000005-0005-4000-8000-000000000001';

DELETE FROM nhis_import_batches
 WHERE id = '00000007-0007-4000-8000-000000000001';

DELETE FROM guardian_clients
 WHERE client_id = '00000005-0005-4000-8000-000000000001'
    OR guardian_user_id = '00000004-0004-4000-8000-000000000001';

DELETE FROM transport_run_stops
 WHERE client_id = '00000005-0005-4000-8000-000000000001';

DELETE FROM clients
 WHERE id = '00000005-0005-4000-8000-000000000001'
    OR (organization_id = '00000001-0001-4000-8000-000000000001' AND name = 'Live E2E Client');

DELETE FROM user_branches
 WHERE user_id = '00000004-0004-4000-8000-000000000001';

DELETE FROM refresh_tokens
 WHERE user_id = '00000004-0004-4000-8000-000000000001';

DELETE FROM users
 WHERE id = '00000004-0004-4000-8000-000000000001';

UPDATE organizations
   SET name = '테스트요양기관'
 WHERE id = '00000001-0001-4000-8000-000000000001'
   AND name = 'Live E2E Organization';

UPDATE users
   SET display_name = 'HQ Admin'
 WHERE id = '00000002-0002-4000-8000-000000000001'
   AND email = 'test@test.com'
   AND display_name = 'Live E2E Admin';

COMMIT;

-- Dev fixture IDs for local/demo PostgreSQL (ogada database).
--
-- UUID layout (hex only, RFC4122 variant 4):
--   Organization : 00000001-0001-4000-8000-000000000001
--   Branch       : bbbbRRCC-000x-4000-8000-000000000001
--     bbbb = branch sequence (0001, 0002, ...)
--     RR   = region: 01=서울, 02=부산, 03=대구, 04=인천
--     CC   = service: 01=주간보호, 02=방문요양, 03=복지용구
--   Dev users    : 0000000n-000n-4000-8000-000000000001  (n=2 hq_admin, 3 branch_admin)
--
-- Branches:
--   00010101-0001-4000-8000-000000000001  서울 강남 주간보호센터
--   00010202-0002-4000-8000-000000000001  부산 해운대 방문요양센터
--
-- Run as postgres superuser (FK updates):
--   sudo -u postgres psql -d ogada -f scripts/seed-dev-fixtures.sql

BEGIN;

SET session_replication_role = replica;

-- Legacy placeholder IDs from early dev seeding
--   org     11111111-1111-1111-1111-111111111111
--   branch  22222222-2222-2222-2222-222222222222  (was "Branch A")
--   branch  33333333-3333-3333-3333-333333333333  (was "Branch B")
--   user    55555555-5555-5555-5555-555555555555  (test@test.com)
--   user    66666666-6666-6666-6666-666666666666  (badmin@test.com)

-- Target IDs
--   org     00000001-0001-4000-8000-000000000001
--   branch  00010101-0001-4000-8000-000000000001  서울 주간보호
--   branch  00010202-0002-4000-8000-000000000001  부산 방문요양
--   user    00000002-0002-4000-8000-000000000001  test@test.com
--   user    00000003-0003-4000-8000-000000000001  badmin@test.com

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM organizations WHERE id = '11111111-1111-1111-1111-111111111111') THEN
        RAISE NOTICE 'Legacy org not found — skipping ID remap (may already be applied).';
    END IF;
END $$;

-- Organization
UPDATE organizations
   SET id = '00000001-0001-4000-8000-000000000001',
       name = '테스트요양기관'
 WHERE id = '11111111-1111-1111-1111-111111111111';

-- Branches (rename + remap IDs with region/service encoding)
UPDATE branches
   SET id = '00010101-0001-4000-8000-000000000001',
       organization_id = '00000001-0001-4000-8000-000000000001',
       name = '서울 강남 주간보호센터',
       address_line1 = '서울특별시 강남구 테헤란로 152'
 WHERE id = '22222222-2222-2222-2222-222222222222';

UPDATE branches
   SET id = '00010202-0002-4000-8000-000000000001',
       organization_id = '00000001-0001-4000-8000-000000000001',
       name = '부산 해운대 방문요양센터',
       address_line1 = '부산광역시 해운대구 해운대해변로 264'
 WHERE id = '33333333-3333-3333-3333-333333333333';

-- Ensure dev branches always have a routable center address (transport depot / Kakao route loop)
UPDATE branches
   SET address_line1 = '서울특별시 강남구 테헤란로 152'
 WHERE id = '00010101-0001-4000-8000-000000000001'
   AND (address_line1 IS NULL OR btrim(address_line1) = '');

UPDATE branches
   SET address_line1 = '부산광역시 해운대구 해운대해변로 264'
 WHERE id = '00010202-0002-4000-8000-000000000001'
   AND (address_line1 IS NULL OR btrim(address_line1) = '');

UPDATE branches
   SET address_line1 = '서울특별시 강남구 테헤란로 152'
 WHERE service_type = 'DAY_CARE'
   AND (address_line1 IS NULL OR btrim(address_line1) = '');

-- Users (shorter dev IDs; keep passwords unchanged)
UPDATE users
   SET id = '00000002-0002-4000-8000-000000000001',
       organization_id = '00000001-0001-4000-8000-000000000001',
       active_branch_id = '00010101-0001-4000-8000-000000000001'
 WHERE id = '55555555-5555-5555-5555-555555555555';

UPDATE users
   SET id = '00000003-0003-4000-8000-000000000001',
       organization_id = '00000001-0001-4000-8000-000000000001',
       active_branch_id = '00010101-0001-4000-8000-000000000001'
 WHERE id = '66666666-6666-6666-6666-666666666666';

UPDATE users
   SET organization_id = '00000001-0001-4000-8000-000000000001'
 WHERE organization_id = '11111111-1111-1111-1111-111111111111';

-- organization_id on tenant-scoped tables
UPDATE attendance           SET organization_id = '00000001-0001-4000-8000-000000000001' WHERE organization_id = '11111111-1111-1111-1111-111111111111';
UPDATE audit_logs           SET organization_id = '00000001-0001-4000-8000-000000000001' WHERE organization_id = '11111111-1111-1111-1111-111111111111';
UPDATE backup_runs          SET organization_id = '00000001-0001-4000-8000-000000000001' WHERE organization_id = '11111111-1111-1111-1111-111111111111';
UPDATE billing_claims       SET organization_id = '00000001-0001-4000-8000-000000000001' WHERE organization_id = '11111111-1111-1111-1111-111111111111';
UPDATE billing_claim_items  SET organization_id = '00000001-0001-4000-8000-000000000001' WHERE organization_id = '11111111-1111-1111-1111-111111111111';
UPDATE billing_claim_status_history SET organization_id = '00000001-0001-4000-8000-000000000001' WHERE organization_id = '11111111-1111-1111-1111-111111111111';
UPDATE branch_qr_tokens     SET organization_id = '00000001-0001-4000-8000-000000000001' WHERE organization_id = '11111111-1111-1111-1111-111111111111';
UPDATE clients              SET organization_id = '00000001-0001-4000-8000-000000000001' WHERE organization_id = '11111111-1111-1111-1111-111111111111';
UPDATE copay_rates          SET organization_id = '00000001-0001-4000-8000-000000000001' WHERE organization_id = '11111111-1111-1111-1111-111111111111';
UPDATE fee_schedules        SET organization_id = '00000001-0001-4000-8000-000000000001' WHERE organization_id = '11111111-1111-1111-1111-111111111111';
UPDATE guardian_clients       SET organization_id = '00000001-0001-4000-8000-000000000001' WHERE organization_id = '11111111-1111-1111-1111-111111111111';
UPDATE guardian_invitations   SET organization_id = '00000001-0001-4000-8000-000000000001' WHERE organization_id = '11111111-1111-1111-1111-111111111111';
UPDATE guardian_notification_preferences SET organization_id = '00000001-0001-4000-8000-000000000001' WHERE organization_id = '11111111-1111-1111-1111-111111111111';
UPDATE health_records         SET organization_id = '00000001-0001-4000-8000-000000000001' WHERE organization_id = '11111111-1111-1111-1111-111111111111';
UPDATE login_history          SET organization_id = '00000001-0001-4000-8000-000000000001' WHERE organization_id = '11111111-1111-1111-1111-111111111111';
UPDATE nhis_import_batches    SET organization_id = '00000001-0001-4000-8000-000000000001' WHERE organization_id = '11111111-1111-1111-1111-111111111111';
UPDATE nhis_import_rows       SET organization_id = '00000001-0001-4000-8000-000000000001' WHERE organization_id = '11111111-1111-1111-1111-111111111111';
UPDATE notifications          SET organization_id = '00000001-0001-4000-8000-000000000001' WHERE organization_id = '11111111-1111-1111-1111-111111111111';
UPDATE user_branches          SET organization_id = '00000001-0001-4000-8000-000000000001' WHERE organization_id = '11111111-1111-1111-1111-111111111111';

-- branch_id remap (2222 → 서울 주간보호, 3333 → 부산 방문요양)
UPDATE attendance           SET branch_id = '00010101-0001-4000-8000-000000000001' WHERE branch_id = '22222222-2222-2222-2222-222222222222';
UPDATE attendance           SET branch_id = '00010202-0002-4000-8000-000000000001' WHERE branch_id = '33333333-3333-3333-3333-333333333333';
UPDATE audit_logs           SET branch_id = '00010101-0001-4000-8000-000000000001' WHERE branch_id = '22222222-2222-2222-2222-222222222222';
UPDATE audit_logs           SET branch_id = '00010202-0002-4000-8000-000000000001' WHERE branch_id = '33333333-3333-3333-3333-333333333333';
UPDATE billing_claims       SET branch_id = '00010101-0001-4000-8000-000000000001' WHERE branch_id = '22222222-2222-2222-2222-222222222222';
UPDATE billing_claims       SET branch_id = '00010202-0002-4000-8000-000000000001' WHERE branch_id = '33333333-3333-3333-3333-333333333333';
UPDATE branch_qr_tokens     SET branch_id = '00010101-0001-4000-8000-000000000001' WHERE branch_id = '22222222-2222-2222-2222-222222222222';
UPDATE branch_qr_tokens     SET branch_id = '00010202-0002-4000-8000-000000000001' WHERE branch_id = '33333333-3333-3333-3333-333333333333';
UPDATE clients              SET branch_id = '00010101-0001-4000-8000-000000000001' WHERE branch_id = '22222222-2222-2222-2222-222222222222';
UPDATE clients              SET branch_id = '00010202-0002-4000-8000-000000000001' WHERE branch_id = '33333333-3333-3333-3333-333333333333';
UPDATE guardian_invitations SET branch_id = '00010101-0001-4000-8000-000000000001' WHERE branch_id = '22222222-2222-2222-2222-222222222222';
UPDATE guardian_invitations SET branch_id = '00010202-0002-4000-8000-000000000001' WHERE branch_id = '33333333-3333-3333-3333-333333333333';
UPDATE health_records       SET branch_id = '00010101-0001-4000-8000-000000000001' WHERE branch_id = '22222222-2222-2222-2222-222222222222';
UPDATE health_records       SET branch_id = '00010202-0002-4000-8000-000000000001' WHERE branch_id = '33333333-3333-3333-3333-333333333333';
UPDATE login_history        SET branch_id = '00010101-0001-4000-8000-000000000001' WHERE branch_id = '22222222-2222-2222-2222-222222222222';
UPDATE login_history        SET branch_id = '00010202-0002-4000-8000-000000000001' WHERE branch_id = '33333333-3333-3333-3333-333333333333';
UPDATE nhis_import_batches  SET branch_id = '00010101-0001-4000-8000-000000000001' WHERE branch_id = '22222222-2222-2222-2222-222222222222';
UPDATE nhis_import_batches  SET branch_id = '00010202-0002-4000-8000-000000000001' WHERE branch_id = '33333333-3333-3333-3333-333333333333';
UPDATE notifications        SET branch_id = '00010101-0001-4000-8000-000000000001' WHERE branch_id = '22222222-2222-2222-2222-222222222222';
UPDATE notifications        SET branch_id = '00010202-0002-4000-8000-000000000001' WHERE branch_id = '33333333-3333-3333-3333-333333333333';
UPDATE user_branches        SET branch_id = '00010101-0001-4000-8000-000000000001' WHERE branch_id = '22222222-2222-2222-2222-222222222222';
UPDATE user_branches        SET branch_id = '00010202-0002-4000-8000-000000000001' WHERE branch_id = '33333333-3333-3333-3333-333333333333';

UPDATE users SET active_branch_id = '00010101-0001-4000-8000-000000000001'
 WHERE active_branch_id = '22222222-2222-2222-2222-222222222222';
UPDATE users SET active_branch_id = '00010202-0002-4000-8000-000000000001'
 WHERE active_branch_id = '33333333-3333-3333-3333-333333333333';

-- user_id remap for dev accounts
UPDATE user_branches    SET user_id = '00000002-0002-4000-8000-000000000001' WHERE user_id = '55555555-5555-5555-5555-555555555555';
UPDATE user_branches    SET user_id = '00000003-0003-4000-8000-000000000001' WHERE user_id = '66666666-6666-6666-6666-666666666666';
UPDATE refresh_tokens   SET user_id = '00000002-0002-4000-8000-000000000001' WHERE user_id = '55555555-5555-5555-5555-555555555555';
UPDATE refresh_tokens   SET user_id = '00000003-0003-4000-8000-000000000001' WHERE user_id = '66666666-6666-6666-6666-666666666666';
UPDATE login_history    SET user_id = '00000002-0002-4000-8000-000000000001' WHERE user_id = '55555555-5555-5555-5555-555555555555';
UPDATE login_history    SET user_id = '00000003-0003-4000-8000-000000000001' WHERE user_id = '66666666-6666-6666-6666-666666666666';
UPDATE password_reset_tokens SET user_id = '00000002-0002-4000-8000-000000000001' WHERE user_id = '55555555-5555-5555-5555-555555555555';
UPDATE password_reset_tokens SET user_id = '00000003-0003-4000-8000-000000000001' WHERE user_id = '66666666-6666-6666-6666-666666666666';

SET session_replication_role = DEFAULT;

COMMIT;

-- Summary
SELECT 'organizations' AS entity, id::text, name FROM organizations
UNION ALL
SELECT 'branch', id::text, name FROM branches ORDER BY entity, name;

SELECT u.email, u.id::text AS user_id, b.name AS active_branch
  FROM users u
  LEFT JOIN branches b ON b.id = u.active_branch_id
 WHERE u.email IN ('test@test.com', 'badmin@test.com');

SELECT b.name, count(c.id) AS clients
  FROM branches b
  LEFT JOIN clients c ON c.branch_id = b.id AND c.is_active
 GROUP BY b.id, b.name
 ORDER BY b.name;

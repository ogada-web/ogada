-- Dev/demo cleanup: deactivate transport on legacy clients that duplicate demo
-- transport roster names (LTC-D10-* canonical set from demo-transport-dispatch-10.py).
--
-- Run:
--   sudo -u postgres psql -d ogada -f scripts/cleanup-transport-roster-duplicates.sql

BEGIN;

UPDATE clients c
   SET uses_transport = FALSE,
       updated_at = NOW()
 WHERE c.uses_transport = TRUE
   AND c.is_active = TRUE
   AND c.discharged_at IS NULL
   AND (c.ltc_cert_no IS NULL OR c.ltc_cert_no NOT LIKE 'LTC-D10-%')
   AND EXISTS (
         SELECT 1
           FROM clients demo
          WHERE demo.organization_id = c.organization_id
            AND demo.branch_id = c.branch_id
            AND demo.name = c.name
            AND demo.id <> c.id
            AND demo.uses_transport = TRUE
            AND demo.is_active = TRUE
            AND demo.discharged_at IS NULL
            AND demo.ltc_cert_no LIKE 'LTC-D10-%'
       );

COMMIT;

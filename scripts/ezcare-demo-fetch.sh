#!/usr/bin/env bash
# ezCare ERP shell fetch via public homepage demo flow (demoAction → POST /page/login.php → /new.ez).
# Used by benchmark_researcher (BNK) for authenticated /new.ez reverse-engineering.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SNAP_DIR="${ROOT}/docs/planning/research/snapshots"
BASE_URL="${EZCARE_BASE_URL:-https://ezcare.easyms.co.kr}"
COOKIE_JAR="${TMPDIR:-/tmp}/ezcare-demo-cookies-$$.txt"
OUT_SUMMARY="${TMPDIR:-/tmp}/ezcare-demo-summary-$$.json"

OCODE="${EZCARE_DEMO_OCODE:-DEMO}"
USER_ID="${EZCARE_DEMO_USER_ID:-admin}"
USER_PW="${EZCARE_DEMO_USER_PW:-g8317}"

usage() {
  cat <<'EOF'
Usage: scripts/ezcare-demo-fetch.sh [options]

Fetch ezCare /new.ez ERP shell using the public demo login flow.

Options:
  --no-save       Fetch only; do not write snapshots (prints summary to stdout)
  --pgid ID       Also fetch /new.ez?PGID=ID (authenticated)
  --batch IDS     Comma-separated PGIDs (e.g. patient-list,schedule-fix,receipt-list)
  --menu-catalog  Parse top-nav JS → ezcare_menu_catalog.json (runs with default fetch)
  -h, --help      Show this help
EOF
}

SAVE=1
EXTRA_PGIDS=()
MENU_CATALOG=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --no-save) SAVE=0; shift ;;
    --pgid) EXTRA_PGIDS+=("${2:-}"); shift 2 ;;
    --batch) IFS=',' read -ra _batch <<< "${2:-}"; EXTRA_PGIDS+=("${_batch[@]}"); shift 2 ;;
    --menu-catalog) MENU_CATALOG=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage; exit 1 ;;
  esac
done

cleanup() { rm -f "$COOKIE_JAR" "$OUT_SUMMARY"; }
trap cleanup EXIT

md5_of() { md5sum "$1" | awk '{print $1}'; }
size_of() { wc -c <"$1" | tr -d ' '; }

fetch() {
  curl -sL --max-time 45 -b "$COOKIE_JAR" -c "$COOKIE_JAR" -o "$2" "$1"
}

mkdir -p "$SNAP_DIR"
TMP_NEW_EZ="$(mktemp)"
TMP_NAV="$(mktemp)"
TMP_REDIRECT="$(mktemp)"

fetch "${BASE_URL}/new.ez" "$TMP_REDIRECT"

LOGIN_JSON="$(curl -sL --max-time 30 -c "$COOKIE_JAR" -b "$COOKIE_JAR" \
  -X POST "${BASE_URL}/page/login.php" \
  -d "oCode=${OCODE}&User_ID=${USER_ID}&User_PW=${USER_PW}")"

LOGIN_CODE="$(python3 -c "import json,sys; print(json.loads(sys.argv[1]).get('code',''))" "$LOGIN_JSON" 2>/dev/null || echo ERR)"

if [[ "$LOGIN_CODE" != "0000" ]]; then
  echo "ezCare demo login failed (code=${LOGIN_CODE})" >&2
  echo "$LOGIN_JSON" >&2
  exit 1
fi

fetch "${BASE_URL}/new.ez" "$TMP_NEW_EZ"

if grep -q 'logout_msg.html?code=001' "$TMP_NEW_EZ" && [[ "$(size_of "$TMP_NEW_EZ")" -lt 500 ]]; then
  echo "ezCare /new.ez returned session-expired stub after demo login" >&2
  exit 1
fi

NAV_QUERY="$(grep -o 'top-nav-item-V2\.js[^"]*' "$TMP_NEW_EZ" | head -1 || true)"
NAV_URL="${BASE_URL}/assets/${NAV_QUERY:-top-nav-item-V2.js}"
fetch "$NAV_URL" "$TMP_NAV"

REDIRECT_SIZE="$(size_of "$TMP_REDIRECT")"
REDIRECT_MD5="$(md5_of "$TMP_REDIRECT")"
NEW_EZ_SIZE="$(size_of "$TMP_NEW_EZ")"
NEW_EZ_MD5="$(md5_of "$TMP_NEW_EZ")"
NAV_SIZE="$(size_of "$TMP_NAV")"
NAV_MD5="$(md5_of "$TMP_NAV")"

TITLE="$(python3 -c "
import re,sys
html=open(sys.argv[1],encoding='utf-8',errors='replace').read()
m=re.search(r'<title>([^<]+)</title>', html, re.I)
print((m.group(1).strip() if m else '')[:120])
" "$TMP_NEW_EZ")"

NAV_ITEMS="$(python3 -c "
import re,sys
html=open(sys.argv[1],encoding='utf-8',errors='replace').read()
items=[]
for no, body in re.findall(r'nav-no=\"(\d+)\"[^>]*>(.*?)</li>', html, re.S):
    labels=[re.sub(r'\s+',' ',a).strip() for a in re.findall(r'<a[^>]*>([^<]+)</a>', body)]
    labels=[l for l in labels if l and l not in ('관리',)]
    if labels:
        items.append(f'{no}:{labels[0]}')
print(';'.join(items))
" "$TMP_NEW_EZ")"

if [[ "$SAVE" -eq 1 ]]; then
  cp "$TMP_REDIRECT" "${SNAP_DIR}/ezcare_new_ez_redirect.html"
  cp "$TMP_NEW_EZ" "${SNAP_DIR}/ezcare_new_ez_demo.html"
  cp "$TMP_NAV" "${SNAP_DIR}/ezcare_top_nav_v2.js"
fi

PGID_ARTIFACTS="[]"
if [[ ${#EXTRA_PGIDS[@]} -gt 0 ]]; then
  PGID_ARTIFACTS="$(python3 -c 'import json; print(json.dumps([]))')"
  for pgid in "${EXTRA_PGIDS[@]}"; do
    [[ -z "$pgid" ]] && continue
    tmp_pgid="$(mktemp)"
    fetch "${BASE_URL}/new.ez?PGID=${pgid}" "$tmp_pgid"
    psz="$(size_of "$tmp_pgid")"
    pmd="$(md5_of "$tmp_pgid")"
    if [[ "$SAVE" -eq 1 ]]; then
      cp "$tmp_pgid" "${SNAP_DIR}/ezcare_new_ez_pgid_${pgid}.html"
    fi
    PGID_ARTIFACTS="$(python3 -c "
import json
items=json.loads('''${PGID_ARTIFACTS}''')
items.append({'pgid':'${pgid}','path':'ezcare_new_ez_pgid_${pgid}.html','bytes':${psz},'md5':'${pmd}'})
print(json.dumps(items))
")"
    rm -f "$tmp_pgid"
  done
fi

if [[ "$MENU_CATALOG" -eq 1 ]] || [[ "$SAVE" -eq 1 ]]; then
  python3 - "$TMP_NAV" "${SNAP_DIR}/ezcare_menu_catalog.json" <<'PY'
import json, re, sys, datetime
js=open(sys.argv[1],encoding='utf-8',errors='replace').read()
menus=[]
cur=None
for line in js.split('\n'):
    m=re.search(r"menuNo\s*:\s*'(\d+)'", line)
    if m:
        if cur: menus.append(cur)
        cur={'no': m.group(1), 'name': '', 'items': []}
    m=re.search(r"menuName:\s*'([^']+)'", line)
    if m and cur: cur['name']=m.group(1)
    m=re.search(r"\{\s*name:\s*'([^']*)'", line)
    if m and cur and m.group(1) != '-':
        it={'name': m.group(1)}
        um=re.search(r"url:\s*'([^']*)'", line)
        am=re.search(r"action:\s*'([^']*)'", line)
        if um: it['url']=um.group(1)
        if am: it['action']=am.group(1)
        if it.get('url') or it.get('action') in ('popup','script'):
            cur['items'].append(it)
if cur: menus.append(cur)
urls=set()
for m in menus:
    for it in m['items']:
        u=it.get('url','')
        if u and not u.startswith('javascript') and 'popup' not in u:
            if u.startswith('/PU.ez'):
                pm=re.search(r'PGID=([^&]+)', u)
                if pm: urls.add(pm.group(1))
            elif not u.startswith('/'):
                urls.add(u.split('#')[0])
out={
  'source': 'ezcare_top_nav_v2.js main_nav_item',
  'fetched_at': datetime.datetime.utcnow().replace(microsecond=0).isoformat()+'Z',
  'module_count': len(menus),
  'leaf_item_count': sum(len(m['items']) for m in menus),
  'unique_pgid_count': len(urls),
  'modules': menus,
}
with open(sys.argv[2],'w',encoding='utf-8') as f:
    json.dump(out,f,ensure_ascii=False,indent=2)
PY
fi

python3 <<PY
import json, datetime

data = {
  "fetched_at": datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
  "base_url": ${BASE_URL@Q},
  "login": {"code": ${LOGIN_CODE@Q}, "oCode": ${OCODE@Q}},
  "title": ${TITLE@Q},
  "nav_top_level": [x for x in ${NAV_ITEMS@Q}.split(";") if x],
  "artifacts": {
    "redirect_stub": {"path": "ezcare_new_ez_redirect.html", "bytes": ${REDIRECT_SIZE@Q}, "md5": ${REDIRECT_MD5@Q}},
    "demo_shell": {"path": "ezcare_new_ez_demo.html", "bytes": ${NEW_EZ_SIZE@Q}, "md5": ${NEW_EZ_MD5@Q}},
    "top_nav_js": {"path": "ezcare_top_nav_v2.js", "bytes": ${NAV_SIZE@Q}, "md5": ${NAV_MD5@Q}, "url": ${NAV_URL@Q}},
    "pgid_pages": json.loads(${PGID_ARTIFACTS@Q}),
  },
}
with open(${OUT_SUMMARY@Q}, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(json.dumps(data, ensure_ascii=False, indent=2))
PY

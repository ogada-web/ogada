#!/usr/bin/env bash
# ogada Vite + Cloudflare quick tunnel 중지·정리.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=_dev_frontend_tunnel_common.sh
source "$SCRIPT_DIR/_dev_frontend_tunnel_common.sh"

case "${1:-}" in
  -h | --help)
    cat <<EOF
Usage: ./scripts/dev-frontend-tunnel-stop.sh [--status]

  Vite(:5173) + cloudflared quick tunnel 프로세스를 정리합니다.
  --status  정리 전후 상태만 출력 (정리는 하지 않음)
EOF
    exit 0
    ;;
  --status)
    dev_tunnel_print_status
    exit 0
    ;;
esac

dev_tunnel_stop
dev_tunnel_print_status

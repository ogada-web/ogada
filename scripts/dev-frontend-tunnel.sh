#!/usr/bin/env bash
# ogada 프론트 Vite + Cloudflare quick tunnel 기동.
# 이전 인스턴스 cleanup 확인 후 새로 시작합니다.
#
# Usage:
#   ./scripts/dev-frontend-tunnel.sh
#   ./scripts/dev-frontend-tunnel.sh --status
#   ./scripts/dev-frontend-tunnel.sh --restart   # (= 기본 동작)
#
# Stop:
#   ./scripts/dev-frontend-tunnel-stop.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=_dev_frontend_tunnel_common.sh
source "$SCRIPT_DIR/_dev_frontend_tunnel_common.sh"

case "${1:-}" in
  -h | --help)
    cat <<EOF
Usage: ./scripts/dev-frontend-tunnel.sh [--status]

  1) 이전 Vite/cloudflared 잔여 프로세스·포트 점유를 정리
  2) cleanup 완료 확인
  3) Vite dev server + Cloudflare quick tunnel 기동
  4) 공개 URL 출력

Options:
  --status   현재 상태만 출력 (기동하지 않음)

Environment:
  DEV_FRONTEND_PORT   (default 5173)
  DEV_BACKEND_PORT    (default 8080)
  DEV_FRONTEND_LOG    (default /tmp/ogada-frontend.log)
  DEV_TUNNEL_LOG      (default /tmp/ogada-cloudflare.log)
EOF
    exit 0
    ;;
  --status)
    dev_tunnel_print_status
    exit 0
    ;;
  --restart | "")
    dev_tunnel_start
    ;;
  *)
    echo "[dev-tunnel] fatal: unknown option: $1" >&2
    exit 2
    ;;
esac

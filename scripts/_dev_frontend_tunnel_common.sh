#!/usr/bin/env bash
# Cloudflare quick tunnel + Vite dev server 공통 라이브러리.
# source "$SCRIPT_DIR/_dev_frontend_tunnel_common.sh" 후 사용.

_dev_tunnel_init() {
  if [[ -n "${_DEV_TUNNEL_LOADED:-}" ]]; then
    return 0
  fi
  _DEV_TUNNEL_LOADED=1

  _DEV_TUNNEL_SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  _DEV_TUNNEL_ROOT="$(cd "$_DEV_TUNNEL_SCRIPT_DIR/.." && pwd)"
  _DEV_TUNNEL_FRONTEND="$_DEV_TUNNEL_ROOT/src/frontend"

  _DEV_TUNNEL_PORT="${DEV_FRONTEND_PORT:-5173}"
  _DEV_TUNNEL_BACKEND_PORT="${DEV_BACKEND_PORT:-8080}"
  _DEV_TUNNEL_HOST="${DEV_FRONTEND_HOST:-0.0.0.0}"
  _DEV_TUNNEL_VITE_LOG="${DEV_FRONTEND_LOG:-/tmp/ogada-frontend.log}"
  _DEV_TUNNEL_CF_LOG="${DEV_TUNNEL_LOG:-/tmp/ogada-cloudflare.log}"
  _DEV_TUNNEL_VITE_PID="${DEV_VITE_PIDFILE:-/tmp/ogada-vite.pid}"
  _DEV_TUNNEL_CF_PID="${DEV_TUNNEL_PIDFILE:-/tmp/ogada-cloudflare.pid}"
  _DEV_TUNNEL_STATE="${DEV_TUNNEL_STATE_FILE:-/tmp/ogada-cloudflare.url}"
}

_dev_tunnel_load_env() {
  _dev_tunnel_init
  local env_file="$_DEV_TUNNEL_ROOT/.env"
  if [[ -f "$env_file" ]]; then
    set -a
    # shellcheck disable=SC1090
    source "$env_file"
    set +a
  fi
}

_dev_tunnel_pids_for_pattern() {
  local pattern=$1
  local pid cwd cmd
  local out=""
  while IFS= read -r pid; do
    [[ -z "$pid" ]] && continue
    cwd="$(readlink -f "/proc/$pid/cwd" 2>/dev/null || true)"
    cmd="$(tr '\0' ' ' < "/proc/$pid/cmdline" 2>/dev/null || true)"
    if [[ "$cwd" == "$_DEV_TUNNEL_ROOT" || "$cwd" == "$_DEV_TUNNEL_ROOT/"* \
      || "$cmd" == *"$_DEV_TUNNEL_ROOT/"* ]]; then
      out+="$pid "
    fi
  done < <(pgrep -f "$pattern" 2>/dev/null || true)
  echo "${out%" "}"
}

_dev_tunnel_vite_pids() {
  _dev_tunnel_init
  local pids=""
  pids="$(_dev_tunnel_pids_for_pattern "node.*$_DEV_TUNNEL_FRONTEND/node_modules/.bin/vite")"
  if [[ -z "$pids" ]]; then
    pids="$(_dev_tunnel_pids_for_pattern "vite --host.*--port $_DEV_TUNNEL_PORT")"
  fi
  if [[ -z "$pids" ]]; then
    pids="$(_dev_tunnel_pids_for_pattern "npm run dev.*--port $_DEV_TUNNEL_PORT")"
  fi
  echo "$pids"
}

_dev_tunnel_cloudflared_pids() {
  _dev_tunnel_init
  local pids=""
  pids="$(_dev_tunnel_pids_for_pattern "cloudflared tunnel --url http://127.0.0.1:$_DEV_TUNNEL_PORT")"
  if [[ -z "$pids" ]]; then
    pids="$(_dev_tunnel_pids_for_pattern "cloudflared tunnel --url http://localhost:$_DEV_TUNNEL_PORT")"
  fi
  echo "$pids"
}

_dev_tunnel_read_pidfile() {
  local file=$1
  [[ -f "$file" ]] || return 0
  local pid
  pid="$(tr -d '[:space:]' < "$file" 2>/dev/null || true)"
  if [[ "$pid" =~ ^[0-9]+$ ]] && [[ -d "/proc/$pid" ]]; then
    echo "$pid"
  fi
}

_dev_tunnel_kill_pids() {
  local label=$1
  shift
  local pids=$*
  [[ -z "$pids" ]] && return 0
  echo "[dev-tunnel] stop $label: $pids"
  # shellcheck disable=SC2086
  kill $pids 2>/dev/null || true
  sleep 1
  # shellcheck disable=SC2086
  kill -9 $pids 2>/dev/null || true
}

_dev_tunnel_port_busy() {
  local port=$1
  if command -v ss >/dev/null 2>&1; then
    ss -ltn "( sport = :$port )" 2>/dev/null | grep -q ":$port"
    return $?
  fi
  curl -sf -o /dev/null --max-time 1 "http://127.0.0.1:$port/" >/dev/null 2>&1
}

_dev_tunnel_wait_port_free() {
  local port=$1
  local timeout=${2:-15}
  local i
  for ((i = 1; i <= timeout; i++)); do
    if ! _dev_tunnel_port_busy "$port"; then
      return 0
    fi
    sleep 1
  done
  return 1
}

_dev_tunnel_http_code() {
  local url=$1
  local code
  code="$(curl -s -o /dev/null -w '%{http_code}' --max-time 8 "$url" 2>/dev/null || true)"
  if [[ "$code" =~ ^[0-9]{3}$ ]]; then
    echo "$code"
  else
    echo "000"
  fi
}

_dev_tunnel_tunnel_url_from_log() {
  local log=$1
  [[ -f "$log" ]] || return 0
  grep -oE 'https://[a-z0-9-]+\.trycloudflare\.com' "$log" 2>/dev/null | tail -1 || true
}

dev_tunnel_collect_status() {
  _dev_tunnel_init

  local vite_pids cf_pids vite_pid cf_pid
  vite_pids="$(_dev_tunnel_vite_pids)"
  cf_pids="$(_dev_tunnel_cloudflared_pids)"
  vite_pid="$(_dev_tunnel_read_pidfile "$_DEV_TUNNEL_VITE_PID")"
  cf_pid="$(_dev_tunnel_read_pidfile "$_DEV_TUNNEL_CF_PID")"

  DEV_TUNNEL_STATUS_VITE_PIDS="$vite_pids"
  DEV_TUNNEL_STATUS_CF_PIDS="$cf_pids"
  DEV_TUNNEL_STATUS_VITE_PIDFILE="$vite_pid"
  DEV_TUNNEL_STATUS_CF_PIDFILE="$cf_pid"

  if [[ -n "$vite_pids" || -n "$vite_pid" ]]; then
    DEV_TUNNEL_STATUS_VITE=running
  else
    DEV_TUNNEL_STATUS_VITE=stopped
  fi

  if [[ -n "$cf_pids" || -n "$cf_pid" ]]; then
    DEV_TUNNEL_STATUS_CF=running
  else
    DEV_TUNNEL_STATUS_CF=stopped
  fi

  DEV_TUNNEL_STATUS_VITE_HTTP="$(_dev_tunnel_http_code "http://127.0.0.1:$_DEV_TUNNEL_PORT/")"
  DEV_TUNNEL_STATUS_BACKEND_HTTP="$(_dev_tunnel_http_code "http://127.0.0.1:$_DEV_TUNNEL_BACKEND_PORT/api/v1/health")"

  DEV_TUNNEL_STATUS_URL=""
  if [[ "$DEV_TUNNEL_STATUS_CF" == running ]]; then
    if [[ -f "$_DEV_TUNNEL_STATE" ]]; then
      DEV_TUNNEL_STATUS_URL="$(tr -d '[:space:]' < "$_DEV_TUNNEL_STATE" 2>/dev/null || true)"
    fi
    if [[ -z "$DEV_TUNNEL_STATUS_URL" ]]; then
      DEV_TUNNEL_STATUS_URL="$(_dev_tunnel_tunnel_url_from_log "$_DEV_TUNNEL_CF_LOG")"
    fi
  fi
  if [[ -n "$DEV_TUNNEL_STATUS_URL" ]]; then
    DEV_TUNNEL_STATUS_TUNNEL_HTTP="$(_dev_tunnel_http_code "$DEV_TUNNEL_STATUS_URL/")"
  else
    DEV_TUNNEL_STATUS_TUNNEL_HTTP="000"
  fi

  local port_free=0
  if ! _dev_tunnel_port_busy "$_DEV_TUNNEL_PORT"; then
    port_free=1
  fi
  if [[ "$DEV_TUNNEL_STATUS_VITE" == stopped && "$DEV_TUNNEL_STATUS_CF" == stopped && "$port_free" -eq 1 ]]; then
    DEV_TUNNEL_STATUS_CLEAN=1
  else
    DEV_TUNNEL_STATUS_CLEAN=0
  fi
}

dev_tunnel_print_status() {
  dev_tunnel_collect_status
  echo "[dev-tunnel] workspace=$_DEV_TUNNEL_ROOT"
  echo "[dev-tunnel] vite      : ${DEV_TUNNEL_STATUS_VITE} (pids=${DEV_TUNNEL_STATUS_VITE_PIDS:-${DEV_TUNNEL_STATUS_VITE_PIDFILE:-none}} http=${DEV_TUNNEL_STATUS_VITE_HTTP})"
  echo "[dev-tunnel] cloudflare: ${DEV_TUNNEL_STATUS_CF} (pids=${DEV_TUNNEL_STATUS_CF_PIDS:-${DEV_TUNNEL_STATUS_CF_PIDFILE:-none}})"
  if [[ -n "$DEV_TUNNEL_STATUS_URL" ]]; then
    echo "[dev-tunnel] url       : $DEV_TUNNEL_STATUS_URL (http=${DEV_TUNNEL_STATUS_TUNNEL_HTTP})"
  else
    echo "[dev-tunnel] url       : (none)"
  fi
  echo "[dev-tunnel] backend   : http://127.0.0.1:$_DEV_TUNNEL_BACKEND_PORT/api/v1/health (http=${DEV_TUNNEL_STATUS_BACKEND_HTTP})"
  echo "[dev-tunnel] clean     : $([[ "$DEV_TUNNEL_STATUS_CLEAN" -eq 1 ]] && echo yes || echo no)"
}

dev_tunnel_stop() {
  _dev_tunnel_init
  echo "[dev-tunnel] cleanup 시작"

  local pids pidfile_pids all_pids=""
  pidfile_pids="$(_dev_tunnel_read_pidfile "$_DEV_TUNNEL_VITE_PID") $(_dev_tunnel_read_pidfile "$_DEV_TUNNEL_CF_PID")"
  for pid in $pidfile_pids; do
    [[ -n "$pid" ]] && all_pids+="$pid "
  done
  for pids in "$(_dev_tunnel_vite_pids)" "$(_dev_tunnel_cloudflared_pids)"; do
    [[ -n "$pids" ]] && all_pids+="$pids "
  done

  if [[ -n "${all_pids// /}" ]]; then
    # shellcheck disable=SC2086
    _dev_tunnel_kill_pids "stale processes" $all_pids
  else
    echo "[dev-tunnel] stop 대상 프로세스 없음"
  fi

  rm -f "$_DEV_TUNNEL_VITE_PID" "$_DEV_TUNNEL_CF_PID" "$_DEV_TUNNEL_STATE"

  if ! _dev_tunnel_wait_port_free "$_DEV_TUNNEL_PORT" 20; then
    echo "[dev-tunnel] warn: port $_DEV_TUNNEL_PORT 아직 사용 중" >&2
    ss -ltnp 2>/dev/null | grep ":$_DEV_TUNNEL_PORT" || true
    return 1
  fi

  dev_tunnel_collect_status
  if [[ "$DEV_TUNNEL_STATUS_CLEAN" -eq 1 ]]; then
    echo "[dev-tunnel] cleanup 완료"
    return 0
  fi

  echo "[dev-tunnel] fatal: cleanup 후에도 잔여 프로세스/포트가 있습니다." >&2
  dev_tunnel_print_status >&2
  return 1
}

dev_tunnel_require_clean() {
  dev_tunnel_collect_status
  if [[ "$DEV_TUNNEL_STATUS_CLEAN" -eq 1 ]]; then
    return 0
  fi
  echo "[dev-tunnel] warn: 이전 dev tunnel 자원이 남아 있습니다 — cleanup 후 재시도합니다." >&2
  dev_tunnel_stop
}

dev_tunnel_start() {
  _dev_tunnel_init

  if ! command -v cloudflared >/dev/null 2>&1; then
    echo "[dev-tunnel] fatal: cloudflared 가 없습니다. 설치 후 재시도하세요." >&2
    return 1
  fi
  if [[ ! -d "$_DEV_TUNNEL_FRONTEND/node_modules" ]]; then
    echo "[dev-tunnel] fatal: frontend node_modules 없음 — cd src/frontend && npm install" >&2
    return 1
  fi

  dev_tunnel_require_clean || return 1

  _dev_tunnel_load_env

  : > "$_DEV_TUNNEL_VITE_LOG"
  : > "$_DEV_TUNNEL_CF_LOG"

  echo "[dev-tunnel] Vite 기동 (:$_DEV_TUNNEL_PORT)"
  (
    cd "$_DEV_TUNNEL_FRONTEND"
    nohup npm run dev -- --host "$_DEV_TUNNEL_HOST" --port "$_DEV_TUNNEL_PORT" \
      >> "$_DEV_TUNNEL_VITE_LOG" 2>&1 &
    echo $! > "$_DEV_TUNNEL_VITE_PID"
  )

  local i code
  for ((i = 1; i <= 30; i++)); do
    code="$(_dev_tunnel_http_code "http://127.0.0.1:$_DEV_TUNNEL_PORT/")"
    if [[ "$code" == "200" ]]; then
      break
    fi
    sleep 1
  done
  code="$(_dev_tunnel_http_code "http://127.0.0.1:$_DEV_TUNNEL_PORT/")"
  if [[ "$code" != "200" ]]; then
    echo "[dev-tunnel] fatal: Vite 가 응답하지 않습니다 (http=$code)" >&2
    tail -20 "$_DEV_TUNNEL_VITE_LOG" >&2 || true
    dev_tunnel_stop || true
    return 1
  fi

  echo "[dev-tunnel] cloudflared 기동"
  nohup cloudflared tunnel --url "http://127.0.0.1:$_DEV_TUNNEL_PORT" \
    >> "$_DEV_TUNNEL_CF_LOG" 2>&1 &
  echo $! > "$_DEV_TUNNEL_CF_PID"

  local url=""
  for ((i = 1; i <= 45; i++)); do
    url="$(_dev_tunnel_tunnel_url_from_log "$_DEV_TUNNEL_CF_LOG")"
    if [[ -n "$url" ]]; then
      break
    fi
    sleep 1
  done
  if [[ -z "$url" ]]; then
    echo "[dev-tunnel] fatal: Cloudflare tunnel URL 을 받지 못했습니다." >&2
    tail -20 "$_DEV_TUNNEL_CF_LOG" >&2 || true
    dev_tunnel_stop || true
    return 1
  fi

  echo "$url" > "$_DEV_TUNNEL_STATE"
  dev_tunnel_collect_status

  echo ""
  echo "========================================"
  echo "[dev-tunnel] 프론트 Cloudflare 프리뷰 준비"
  echo "  URL     : $url"
  echo "  local   : http://127.0.0.1:$_DEV_TUNNEL_PORT/"
  echo "  kakao   : 지도 미리보기 사용 시 카카오 개발자 콘솔 Web 도메인에 등록 필요"
  echo "            - $url"
  echo "            - http://127.0.0.1:$_DEV_TUNNEL_PORT"
  echo "            - http://localhost:$_DEV_TUNNEL_PORT"
  echo "  vite log: $_DEV_TUNNEL_VITE_LOG"
  echo "  cf log  : $_DEV_TUNNEL_CF_LOG"
  if [[ "$DEV_TUNNEL_STATUS_BACKEND_HTTP" != "200" ]]; then
    echo "  warn    : backend :$_DEV_TUNNEL_BACKEND_PORT 미기동 — API 호출 불가"
    echo "            Vite /api 프록시는 Spring Boot 기동 후 사용 가능"
  else
    echo "  backend : OK (:$_DEV_TUNNEL_BACKEND_PORT)"
  fi
  echo "  stop    : ./scripts/dev-frontend-tunnel-stop.sh"
  echo "========================================"
}

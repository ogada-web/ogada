#!/usr/bin/env python3
"""Serve compiled demo assets. Forward auth, route queries, and vehicle registration.

Vehicle writes are still authorized by Spring; dispatch writes remain blocked.
"""
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import argparse
import json
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1] / 'src/frontend/dist'
VEHICLE_PATH = re.compile(r'/api/v1/transport/vehicles/[0-9a-fA-F]{8}(?:-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12}')


class DemoPreview(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def proxy_demo_api(self):
        request = HTTPConnection('127.0.0.1', 8080, timeout=90)
        body = self.rfile.read(int(self.headers.get('Content-Length', '0')))
        headers = {key: value for key, value in self.headers.items()
                   if key.lower() not in {'host', 'connection', 'content-length', 'transfer-encoding'}}
        request.request(self.command, self.path, body=body, headers=headers)
        response = request.getresponse()
        payload = response.read()
        self.send_response(response.status)
        for key, value in response.getheaders():
            if key.lower() not in {'connection', 'transfer-encoding', 'content-length'}:
                self.send_header(key, value)
        self.send_header('Content-Length', str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)
        request.close()

    def do_GET(self):
        name = unquote(urlsplit(self.path).path)
        if name.startswith('/api/v1/'):
            self.proxy_demo_api()
            return
        candidate = (ROOT / name.lstrip('/')).resolve()
        if (candidate != ROOT and ROOT not in candidate.parents) or any(
            part.startswith('.') for part in Path(name).parts
        ) or name.startswith(('/api', '/@fs', '/src', '/scripts', '/docs')):
            self.send_error(404)
            return
        if candidate.is_dir() and candidate != ROOT:
            self.send_error(404)
            return
        if not candidate.is_file() and not Path(name).suffix:
            self.path = '/index.html'
        super().do_GET()

    def reject_preview_write(self):
        # Keep the existing write allowlist; return a message the app can display.
        payload = json.dumps({"message": "이 미리보기에서는 조회와 차량 등록·수정만 지원합니다. 다른 저장 작업은 운영 환경에서 진행하세요.",
                              "code": "PREVIEW_WRITE_DISABLED"}, ensure_ascii=False).encode('utf-8')
        self.send_response(405)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_POST(self):
        name = unquote(urlsplit(self.path).path)
        if self.command == 'POST' and name in {
            '/api/v1/auth/login', '/api/v1/auth/refresh', '/api/v1/auth/logout',
            '/api/v1/transport/route-preview', '/api/v1/transport/vehicles'
        }:
            self.proxy_demo_api()
        else:
            self.reject_preview_write()

    def do_PATCH(self):
        # Spring retains all JWT, tenant and manager-role authorization checks.
        if VEHICLE_PATH.fullmatch(unquote(urlsplit(self.path).path)):
            self.proxy_demo_api()
        else:
            self.reject_preview_write()

    do_PUT = do_POST
    do_DELETE = do_POST


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--port', type=int, default=4174)
    args = parser.parse_args()
    ROOT = args.root.resolve()
    print(f'Compiled demo on http://127.0.0.1:{args.port}', flush=True)
    ThreadingHTTPServer(('127.0.0.1', args.port), DemoPreview).serve_forever()

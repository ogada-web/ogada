"""HTTP checks for authenticated vehicle, dispatch and attendance forwarding."""
import importlib.util
import json
import tempfile
import threading
import unittest
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('preview', Path(__file__).with_name('demo-preview-server.py'))
preview = importlib.util.module_from_spec(spec)
spec.loader.exec_module(preview)


class Backend(BaseHTTPRequestHandler):
    calls = []

    def do_POST(self):
        body = self.rfile.read(int(self.headers.get('Content-Length', '0')))
        self.calls.append((self.command, self.path, body))
        status = 200 if self.headers.get('Authorization') == 'Bearer manager' else 403
        payload = b'{"accepted": true}'
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    do_PATCH = do_POST
    do_PUT = do_POST

    def log_message(self, *args):
        pass


class QuietPreview(preview.DemoPreview):
    def log_message(self, *args):
        pass


class PreviewHttpTest(unittest.TestCase):
    def test_authorization_forwarding_and_unsupported_writes(self):
        with tempfile.TemporaryDirectory() as folder:
            preview.ROOT = Path(folder)
            (preview.ROOT / 'index.html').write_text('Compiled preview')
            backend = ThreadingHTTPServer(('127.0.0.1', 0), Backend)
            server = ThreadingHTTPServer(('127.0.0.1', 0), QuietPreview)
            threads = [threading.Thread(target=s.serve_forever, daemon=True) for s in (backend, server)]
            for thread in threads:
                thread.start()
            try:
                real_connection = HTTPConnection
                def backend_connection(host, port, **kwargs):
                    self.assertEqual(host, '127.0.0.1')
                    return real_connection(host, backend.server_port, **kwargs)

                def request(method, path, authenticated=False):
                    client = HTTPConnection('127.0.0.1', server.server_port, timeout=5)
                    headers = {'Content-Type': 'application/json'}
                    if authenticated:
                        headers['Authorization'] = 'Bearer manager'
                    body = json.dumps({'plateNumber': 'DEMO', 'capacity': 8}) if method != 'GET' else None
                    client.request(method, path, body=body, headers=headers)
                    response = client.getresponse()
                    status = response.status
                    response.read()
                    client.close()
                    return status

                with patch.object(preview, 'HTTPConnection', backend_connection):
                    self.assertEqual(request('POST', '/api/v1/transport/vehicles'), 403)
                    self.assertEqual(request('POST', '/api/v1/transport/vehicles', True), 200)
                    self.assertEqual(json.loads(Backend.calls[-1][2])['capacity'], 8)
                    vehicle = '/api/v1/transport/vehicles/00000000-0000-4000-8000-000000000001'
                    self.assertEqual(request('PATCH', vehicle, True), 200)
                    self.assertEqual(request('PATCH', vehicle), 403)
                    for method, path in [('POST', '/api/v1/transport/runs/suggest'),
                                         ('PUT', '/api/v1/transport/settings'),
                                         ('POST', '/api/v1/staff/work-attendance/check-in')]:
                        self.assertEqual(request(method, path), 403)
                        self.assertEqual(request(method, path, True), 200)
                    count = len(Backend.calls)
                    for method, path in [('POST', '/api/v1/users'),
                                         ('PUT', '/api/v1/staff/payroll/settings'),
                                         ('DELETE', vehicle), ('PATCH', vehicle + '/extra')]:
                        self.assertEqual(request(method, path, True), 405)
                    self.assertEqual(len(Backend.calls), count)
                    for path in ['/.env', '/src/App.jsx', '/scripts/demo-preview-server.py']:
                        self.assertEqual(request('GET', path), 404)
                    self.assertEqual(request('GET', '/transport'), 200)
            finally:
                for process in (server, backend):
                    process.shutdown()
                    process.server_close()
                for thread in threads:
                    thread.join(timeout=2)


if __name__ == '__main__':
    unittest.main()

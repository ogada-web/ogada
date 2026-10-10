"""Verify the preview forwards only the supported workflow paths; no network calls."""
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import Mock

spec = importlib.util.spec_from_file_location('demo_preview', Path(__file__).with_name('demo-preview-server.py'))
preview = importlib.util.module_from_spec(spec)
spec.loader.exec_module(preview)


class PreviewDispatchRoutesTest(unittest.TestCase):
    def handler(self, method, path):
        handler = preview.DemoPreview.__new__(preview.DemoPreview)
        handler.command = method
        handler.path = path
        handler.proxy_demo_api = Mock()
        handler.reject_preview_write = Mock()
        return handler

    def test_scoped_dispatch_operations_reach_spring_authorization(self):
        run = '/api/v1/transport/runs/00000000-0000-4000-8000-000000000001'
        for method, path in [('POST', '/api/v1/transport/runs'), ('POST', '/api/v1/transport/runs/suggest'),
                             ('POST', run + '/confirm'), ('PATCH', run), ('PATCH', run + '/unconfirm'),
                             ('PUT', '/api/v1/transport/settings')]:
            with self.subTest(method=method, path=path):
                handler = self.handler(method, path)
                getattr(handler, 'do_' + method)()
                handler.proxy_demo_api.assert_called_once()
                handler.reject_preview_write.assert_not_called()

    def test_other_workflows_deletion_and_invalid_ids_remain_blocked(self):
        for method, path in [('DELETE', '/api/v1/transport/runs/00000000-0000-4000-8000-000000000001'),
                             ('POST', '/api/v1/users'), ('PATCH', '/api/v1/transport/runs/not-a-uuid'),
                             ('PUT', '/api/v1/transport/runs'), ('DELETE', '/api/v1/transport/runs')]:
            with self.subTest(method=method, path=path):
                handler = self.handler(method, path)
                getattr(handler, 'do_' + method)()
                handler.proxy_demo_api.assert_not_called()
                handler.reject_preview_write.assert_called_once()


if __name__ == '__main__':
    unittest.main()

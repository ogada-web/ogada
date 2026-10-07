"""Agent failure and model-selection regression tests; no API/Git writes."""
import argparse
import contextlib
import importlib.util
import io
import os
from pathlib import Path
import subprocess
import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock, patch


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("ogada_agent_runner", ROOT / "scripts/run_agent.py")
runner = importlib.util.module_from_spec(spec)
with patch.dict(os.environ, {"AGENT_BRIDGE_PRUNE": "0"}):
    spec.loader.exec_module(runner)


class BuildTests(unittest.TestCase):
    def invoke(self, result, role="coder", loop=False, **extra):
        args = argparse.Namespace(role=role, target="src/backend", stream="backend", loop=loop, interval=1, task="test")
        mocks = {
            "require_api_key": MagicMock(return_value="test-only"),
            "approval_present": MagicMock(return_value=True),
            "ensure_role_branch": MagicMock(),
            "print_coder_preflight": MagicMock(),
            "_build_role_prompt": MagicMock(return_value="test"),
            "_role_watched_paths": MagicMock(return_value=[]),
            "_recover_build_bridge": MagicMock(),
            "call_agent": MagicMock(return_value=result),
            "push_submodule_develop": MagicMock(),
            "maybe_merge_version_to_test": MagicMock(return_value=False),
            "_roadmap_merge_ready": MagicMock(return_value=None),
            "run_live_e2e_post_merge": MagicMock(return_value=0),
            "render_build_changes": MagicMock(),
            "render_agent_output": MagicMock(),
            "_release_bridge_resources": MagicMock(),
        }
        mocks.update(extra)
        with patch.multiple(runner, **mocks), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            try:
                runner.cmd_build(args)
                code = 0
            except SystemExit as e:
                code = e.code
        return code, mocks

    def test_failed_runs_never_push_or_merge(self):
        for role in ("coder", "ux_designer", "tester"):
            for result in (None, SimpleNamespace(status="error", result="failure"), SimpleNamespace(status="cancelled", result="")):
                with self.subTest(role=role, result=result):
                    code, mocks = self.invoke(result, role)
                    self.assertEqual(code, 1)
                    mocks["push_submodule_develop"].assert_not_called()
                    mocks["maybe_merge_version_to_test"].assert_not_called()
                    mocks["_release_bridge_resources"].assert_called_once()

    def test_finished_coder_can_push(self):
        code, mocks = self.invoke(SimpleNamespace(status="finished", result="done"))
        self.assertEqual(code, 0)
        mocks["push_submodule_develop"].assert_called_once_with("coder", "backend")

    def test_loop_stops_after_failure_without_sleep(self):
        with patch.object(runner.time, "sleep") as sleep:
            code, mocks = self.invoke(None, loop=True)
        self.assertEqual(code, 1)
        sleep.assert_not_called()
        mocks["call_agent"].assert_called_once()

    def test_missing_key_stops_before_checkout(self):
        code, mocks = self.invoke(None, require_api_key=MagicMock(side_effect=SystemExit(2)))
        self.assertEqual(code, 2)
        mocks["ensure_role_branch"].assert_not_called()
        mocks["call_agent"].assert_not_called()

    def test_live_e2e_failure_is_nonzero(self):
        code, _ = self.invoke(SimpleNamespace(status="finished", result="done"), "tester",
                              maybe_merge_version_to_test=MagicMock(return_value=True),
                              run_live_e2e_post_merge=MagicMock(return_value=1))
        self.assertEqual(code, 1)

    def test_push_failure_propagates(self):
        with patch.multiple(runner, _git_repo_ready=MagicMock(return_value=True),
                            _git_current_branch=MagicMock(return_value="develop"),
                            _git_status_porcelain=MagicMock(return_value=""),
                            _git_commits_ahead=MagicMock(return_value=1)), \
             patch.object(runner.subprocess, "run", side_effect=subprocess.CalledProcessError(1, "git push", stderr="rejected")), \
             contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as caught:
                runner.push_submodule_develop("coder", "backend")
        self.assertEqual(caught.exception.code, 1)


class ModelTests(unittest.TestCase):
    def test_explicit_model_has_no_other_provider_fallback(self):
        with patch.object(runner, "ENV_MODEL", " grok-test "):
            for role in runner.ALL_BUILD_ROLES:
                self.assertEqual(runner.resolve_model_chain(role), ["grok-test"])

    def test_default_role_chain_is_preserved(self):
        with patch.object(runner, "ENV_MODEL", None):
            self.assertGreater(len(runner.resolve_model_chain("coder")), 1)

    def test_doctor_is_targeted_tools_disabled_and_hides_key(self):
        output = io.StringIO()
        with patch.object(runner, "require_api_key", return_value="secret-must-not-print"), \
             patch.object(runner, "_build_agent_prompt", return_value=SimpleNamespace(status="finished", result="")) as prompt, \
             patch.object(runner, "_recover_build_bridge"), patch.object(runner, "_release_bridge_resources"), \
             contextlib.redirect_stdout(output):
            runner.cmd_doctor(SimpleNamespace(model=["grok-test"], list_models=False, ok_only=False))
        self.assertEqual(prompt.call_count, 1)
        self.assertEqual(prompt.call_args.kwargs["model_id"], "grok-test")
        self.assertEqual(prompt.call_args.kwargs["tools"], [])
        self.assertNotIn("secret-must-not-print", output.getvalue())

    def test_doctor_failure_has_nonzero_exit(self):
        with patch.object(runner, "require_api_key", return_value="test-only"), \
             patch.object(runner, "_build_agent_prompt", return_value=SimpleNamespace(status="error", result="failure")), \
             patch.object(runner, "_recover_build_bridge"), patch.object(runner, "_release_bridge_resources"), \
             contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(SystemExit) as caught:
                runner.cmd_doctor(SimpleNamespace(model=["grok-test"], list_models=False, ok_only=False))
        self.assertEqual(caught.exception.code, 1)

    def test_list_models_does_not_start_an_agent(self):
        client = MagicMock()
        client.models.list.return_value = [SimpleNamespace(id="grok-test")]
        output = io.StringIO()
        with patch.object(runner, "require_api_key", return_value="test-only"), \
             patch.object(runner, "_ensure_build_client", return_value=client), \
             patch.object(runner, "_build_agent_prompt") as prompt, \
             patch.object(runner, "_release_bridge_resources"), contextlib.redirect_stdout(output):
            runner.cmd_doctor(SimpleNamespace(list_models=True))
        client.models.list.assert_called_once_with(api_key="test-only")
        prompt.assert_not_called()
        self.assertEqual(output.getvalue(), "grok-test\n")


if __name__ == "__main__":
    unittest.main()

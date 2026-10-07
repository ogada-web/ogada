"""Agent failure and model-selection regression tests; no API/Git writes."""
import argparse
import contextlib
import importlib.util
import io
import os
from pathlib import Path
import subprocess
import tempfile
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
            "_roadmap_mark_merged": MagicMock(),
            "run_live_e2e_post_merge": MagicMock(return_value=0),
            "render_build_changes": MagicMock(),
            "render_agent_output": MagicMock(),
            "_release_bridge_resources": MagicMock(),
            "require_tester_pass": MagicMock(),
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
        code, mocks = self.invoke(SimpleNamespace(status="finished", result="done"), "tester",
                              _roadmap_merge_ready=MagicMock(return_value="v3"),
                              maybe_merge_version_to_test=MagicMock(return_value=True),
                              run_live_e2e_post_merge=MagicMock(return_value=1))
        self.assertEqual(code, 1)
        mocks["_roadmap_mark_merged"].assert_not_called()

    def test_successful_merge_is_recorded_after_live_check(self):
        code, mocks = self.invoke(SimpleNamespace(status="finished", result="done"), "tester",
                              _roadmap_merge_ready=MagicMock(return_value="v3"),
                              maybe_merge_version_to_test=MagicMock(return_value=True))
        self.assertEqual(code, 0)
        mocks["_roadmap_mark_merged"].assert_called_once_with("v3")

    def test_tester_receives_the_merged_head(self):
        merge = MagicMock(return_value=True)
        result = SimpleNamespace(status="finished", result="done")

        def call(*args, **kwargs):
            merge.assert_called_once_with("backend")
            return result

        code, _ = self.invoke(result, "tester",
                             _roadmap_merge_ready=MagicMock(return_value="v3"),
                             maybe_merge_version_to_test=merge,
                             call_agent=MagicMock(side_effect=call))
        self.assertEqual(code, 0)

    def test_merge_failure_is_nonzero_and_never_marked_complete(self):
        with patch.object(runner, "_roadmap_merge_ready", return_value="v3"), \
             patch.object(runner, "merge_develop_to_test", return_value=False), \
             patch.object(runner, "_roadmap_mark_merged") as mark:
            with self.assertRaises(SystemExit) as caught:
                runner.maybe_merge_version_to_test("backend")
        self.assertEqual(caught.exception.code, 1)
        mark.assert_not_called()

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

    def test_local_commit_mode_does_not_contact_git_remote(self):
        with patch.dict(os.environ, {"AGENT_AUTO_PUSH": "0"}), \
             patch.multiple(runner, _git_repo_ready=MagicMock(return_value=True),
                            _git_current_branch=MagicMock(return_value="develop"),
                            _git_status_porcelain=MagicMock(return_value="")), \
             patch.object(runner, "_git_commits_ahead") as ahead, \
             patch.object(runner.subprocess, "run") as git, contextlib.redirect_stdout(io.StringIO()):
            runner.push_submodule_develop("coder", "backend")
        ahead.assert_not_called()
        git.assert_not_called()


class ModelTests(unittest.TestCase):
    def test_baseline_ahead_does_not_fetch_or_request_credentials(self):
        with patch.object(runner, "_git_repo_ready", return_value=True), \
             patch.object(runner.subprocess, "run", return_value=SimpleNamespace(stdout="0")) as git:
            self.assertEqual(runner._git_commits_ahead(ROOT / "src/backend", "develop"), 0)
        self.assertEqual(git.call_count, 1)
        self.assertEqual(git.call_args.args[0][:3], ["git", "rev-list", "--count"])

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

    def test_local_commit_policy_is_passed_to_the_agent(self):
        result = SimpleNamespace(status="finished", result="done", id="test-run", duration_ms=1)
        with patch.dict(os.environ, {"AGENT_AUTO_PUSH": "0"}), \
             patch.object(runner, "require_api_key", return_value="test-only"), \
             patch.object(runner, "ENV_MODEL", "grok-test"), \
             patch.object(runner, "_RICH", False), \
             patch.object(runner, "_build_agent_prompt", return_value=result) as prompt, \
             contextlib.redirect_stdout(io.StringIO()):
            self.assertIs(runner.call_agent("task", ROOT, role="coder"), result)
        self.assertIn("AGENT_AUTO_PUSH=0", prompt.call_args.args[0])
        self.assertIn("원격 push는 수행하지 말고", prompt.call_args.args[0])


class TesterVerdictTests(unittest.TestCase):
    def validate(self, verdict="PASS", sha="1234567", history="", present=True):
        with tempfile.TemporaryDirectory(prefix="ogada-manifest-test-") as folder:
            root = Path(folder)
            (root / "manifests").mkdir()
            if present:
                (root / "manifests/latest.yaml").write_text(
                    f"<!-- latest -->\nstream: backend\nverdict: {verdict}\ntest_sha: {sha}\ndevelop_sha: {sha}\n{history}")
            with patch.object(runner, "transfer_dir_for_stream", return_value=root), \
                 patch.object(runner, "_git_short_rev", return_value="12345678"), \
                 contextlib.redirect_stderr(io.StringIO()):
                runner.require_tester_pass("backend")

    def test_current_pass_manifest_is_accepted(self):
        self.validate()

    def test_current_block_cannot_be_overridden_by_historical_pass(self):
        with self.assertRaises(SystemExit):
            self.validate(verdict="BLOCK", history="\n<!-- history -->\nverdict: PASS\n")

    def test_pass_on_old_head_is_rejected(self):
        with self.assertRaises(SystemExit):
            self.validate(sha="abcdef01")

    def test_missing_manifest_is_rejected(self):
        with self.assertRaises(SystemExit):
            self.validate(present=False)


if __name__ == "__main__":
    unittest.main()

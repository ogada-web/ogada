"""Execute shell entrypoints against disposable fake tools, never live agents."""
import os
from pathlib import Path
import shutil
import signal
import subprocess
import tempfile
import time
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ShellTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="ogada-loop-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ("scripts", ".agents", ".venv/bin", "bin", "src/backend", "src/frontend", "src/backend-test", "src/frontend-test"):
            (self.root / name).mkdir(parents=True)
        for name in ("agent_pipeline.sh", "agent_team_start.sh", "_agent_common.sh"):
            shutil.copyfile(ROOT / "scripts" / name, self.root / "scripts" / name)
        for name in ("backend", "frontend"):
            (self.root / "src" / name / ".git").touch()
        (self.root / ".agents/pipeline_cycle").write_text("1")
        (self.root / ".venv/bin/activate").write_text('export PATH="' + str(self.root / ".venv/bin") + ':$PATH"\n')
        self.write_tool(".venv/bin/python", '''#!/usr/bin/env bash
if [[ "$2" == preflight ]]; then exit "${PREFLIGHT_EXIT:-0}"; fi
if [[ "$2" == status ]]; then echo 'approved  : YES'; exit 0; fi
if [[ "$2" == prune-bridges ]]; then exit 0; fi
role=''; stream=''
while [[ $# -gt 0 ]]; do
 case "$1" in
 --role) role="$2"; shift ;;
 --stream) stream="$2"; shift ;;
 esac
 shift
done
echo "$role:$stream" >> "$TEST_CALLS"
if [[ "$role:$stream" == "${FAIL_STEP:-never}" ]]; then exit 1; fi
''')
        self.write_tool("bin/git", '#!/usr/bin/env bash\nif [[ "$*" == *branch* ]]; then echo develop; fi\nexit 0\n')
        self.write_tool("bin/tmux", '''#!/usr/bin/env bash
if [[ "$1" == has-session ]]; then exit 1; fi
if [[ "$1" == new-session ]]; then printf '%s\\n' "${@: -1}" >> "$TEST_TMUX"; fi
''')
        self.env = {**os.environ, "PATH": str(self.root / "bin") + ":" + os.environ["PATH"],
                    "TEST_CALLS": str(self.root / "calls"), "TEST_TMUX": str(self.root / "tmux"),
                    "AGENT_INTERVAL_SECONDS": "180", "AGENT_PIPELINE_FULL_EVERY": "6"}

    def write_tool(self, name, body):
        path = self.root / name
        path.write_text(body)
        path.chmod(0o755)

    def run_script(self, name, *args, **env):
        return subprocess.run(["bash", str(self.root / "scripts" / name), *args],
                              cwd=self.root, env={**self.env, **env}, capture_output=True, text=True, timeout=10)

    def calls(self):
        path = self.root / "calls"
        return path.read_text().splitlines() if path.exists() else []

    def test_one_cycle_keeps_backend_frontend_order(self):
        result = self.run_script("agent_pipeline.sh", "--once")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.calls(), ["coder:backend", "tester:backend", "coder:frontend", "tester:frontend"])

    def test_coder_failure_blocks_tester_and_next_stream(self):
        result = self.run_script("agent_pipeline.sh", "--once", FAIL_STEP="coder:backend")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(self.calls(), ["coder:backend"])

    def test_tester_failure_blocks_next_stream(self):
        result = self.run_script("agent_pipeline.sh", "--once", FAIL_STEP="tester:backend")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(self.calls(), ["coder:backend", "tester:backend"])

    def test_full_cycle_planner_failure_blocks_all_followup(self):
        (self.root / ".agents/pipeline_cycle").write_text("0")
        result = self.run_script("agent_pipeline.sh", "--once", FAIL_STEP="planner:")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(self.calls(), ["planner:"])

    def test_loop_failure_stops_instead_of_repeating(self):
        result = self.run_script("agent_pipeline.sh", FAIL_STEP="coder:backend")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(self.calls(), ["coder:backend"])

    def test_preflight_failure_never_starts_agents(self):
        for script in ("agent_pipeline.sh", "agent_team_start.sh"):
            with self.subTest(script=script):
                result = self.run_script(script, "--no-loop", PREFLIGHT_EXIT="2")
                self.assertEqual(result.returncode, 2)
                self.assertEqual(self.calls(), [])
                self.assertFalse((self.root / "tmux").exists())

    def test_team_no_loop_applies_to_all_four_sessions(self):
        result = self.run_script("agent_team_start.sh", "--no-loop")
        self.assertEqual(result.returncode, 0, result.stderr)
        commands = (self.root / "tmux").read_text().splitlines()
        self.assertEqual(len(commands), 4)
        self.assertIn("--once", commands[0])
        self.assertTrue(all("--loop" not in command for command in commands))

    def test_team_default_keeps_support_loops(self):
        result = self.run_script("agent_team_start.sh")
        self.assertEqual(result.returncode, 0, result.stderr)
        commands = (self.root / "tmux").read_text().splitlines()
        self.assertEqual(len(commands), 4)
        self.assertNotIn("--once", commands[0])
        self.assertTrue(all("--loop" in command for command in commands[1:]))

    def test_invalid_interval_never_starts_agents(self):
        for script in ("agent_pipeline.sh", "agent_team_start.sh"):
            for setting in ("AGENT_INTERVAL_SECONDS", "AGENT_PIPELINE_FULL_EVERY"):
                with self.subTest(script=script, setting=setting):
                    result = self.run_script(script, **{setting: "0"})
                    self.assertEqual(result.returncode, 2)
                    self.assertEqual(self.calls(), [])
                    self.assertFalse((self.root / "tmux").exists())

    def test_sigterm_stops_pipeline_during_interval(self):
        with tempfile.TemporaryFile(mode="w+") as output:
            process = subprocess.Popen(["bash", str(self.root / "scripts/agent_pipeline.sh")], cwd=self.root,
                                       env=self.env, stdout=output, stderr=output, start_new_session=True)
            try:
                deadline = time.monotonic() + 5
                while len(self.calls()) < 4 and time.monotonic() < deadline:
                    time.sleep(0.02)
                self.assertEqual(len(self.calls()), 4)
                os.killpg(process.pid, signal.SIGTERM)
                self.assertEqual(process.wait(timeout=5), 143)
                self.assertEqual(len(self.calls()), 4)
            finally:
                if process.poll() is None:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()


if __name__ == "__main__":
    unittest.main()

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


APP_PATH = Path(__file__).resolve().parents[1] / "app.py"


class AppTests(unittest.TestCase):
    def run_app(self, folder):
        return subprocess.run(
            [sys.executable, str(APP_PATH)],
            cwd=folder,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_reports_healthy_repository(self):
        with tempfile.TemporaryDirectory() as temporary_folder:
            repository = Path(temporary_folder)
            (repository / "README.md").touch()
            (repository / "tests").mkdir()
            (repository / "requirements.txt").touch()

            result = self.run_app(repository)

        self.assertEqual(result.returncode, 0)
        self.assertIn("PASS: README.md found", result.stdout)
        self.assertIn("PASS: Test folder found", result.stdout)
        self.assertIn("PASS: requirements.txt found", result.stdout)
        self.assertIn("Overall health: Good", result.stdout)

    def test_warns_when_repository_items_are_missing(self):
        with tempfile.TemporaryDirectory() as temporary_folder:
            result = self.run_app(temporary_folder)

        self.assertEqual(result.returncode, 0)
        self.assertIn("WARN: README.md not found", result.stdout)
        self.assertIn("WARN: Test folder not found", result.stdout)
        self.assertIn("WARN: requirements.txt not found", result.stdout)
        self.assertIn("Overall health: Some items are missing", result.stdout)


if __name__ == "__main__":
    unittest.main()
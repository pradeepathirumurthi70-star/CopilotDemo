"""Check a few useful basics in a project folder."""

import argparse
import subprocess
from pathlib import Path


def is_git_repository(folder):
    """Return True when folder is inside a Git working tree."""
    result = subprocess.run(
        ["git", "rev-parse", "--is-inside-work-tree"],
        cwd=folder,
        capture_output=True,
        text=True,
        check=False,
    )
    return result.returncode == 0


def check_repository(folder):
    """Return a list of basic checks and their results."""
    python_files = list(folder.rglob("*.py"))
    has_tests = (folder / "tests").is_dir() or any(
        file.name.startswith("test_") or file.name.endswith("_test.py")
        for file in python_files
    )
    has_project_config = any(
        (folder / name).is_file()
        for name in ("pyproject.toml", "setup.py", "requirements.txt")
    )

    return [
        ("Git repository", is_git_repository(folder)),
        ("README file", any((folder / name).is_file() for name in ("README.md", "README.rst", "README"))),
        ("Python files", bool(python_files)),
        ("Tests", has_tests),
        ("Project configuration", has_project_config),
    ]


def main():
    parser = argparse.ArgumentParser(
        description="Check a project folder for a few useful repository basics."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="project folder to check (defaults to the current folder)",
    )
    args = parser.parse_args()

    folder = Path(args.path).expanduser().resolve()
    if not folder.is_dir():
        parser.error(f"{folder} is not a folder")

    print(f"Repository health check: {folder}")
    results = check_repository(folder)

    for name, passed in results:
        status = "PASS" if passed else "WARN"
        print(f"[{status}] {name}")

    passed_count = sum(passed for _, passed in results)
    print(f"\nResult: {passed_count} of {len(results)} checks passed.")


if __name__ == "__main__":
    main()
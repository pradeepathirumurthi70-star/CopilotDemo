"""Check a repository for a few important files and folders."""

from pathlib import Path


repository = Path.cwd()

checks = {
    "README.md": (repository / "README.md").is_file(),
    "Test folder": (repository / "test").is_dir()
    or (repository / "tests").is_dir(),
    "requirements.txt": (repository / "requirements.txt").is_file(),
}

print("Repository Health Report")
print("------------------------")

for check_name, passed in checks.items():
    if passed:
        print(f"PASS: {check_name} found")
    else:
        print(f"WARN: {check_name} not found")

if all(checks.values()):
    print("\nOverall health: Good")
else:
    print("\nOverall health: Some items are missing")
# Repository Health Checker

A beginner-friendly Python command-line app that checks whether the current
repository contains a `README.md` file, a test folder, and a `requirements.txt`
file. It prints a simple report with a `PASS` or `WARN` for each item and an
overall health message. Warnings are informational; they do not stop the app.

## Setup

Install Python 3.8 or later. The app uses only Python's standard library, so no
third-party packages need to be installed. The `requirements.txt` file is kept
as a project marker and is intentionally empty of external dependencies.

## Usage

Run the app from the repository you want to check:

```bash
python3 app.py
```

The app checks the current working directory. For example, to check another
project, change into that project's folder and run this app by its path:

```bash
cd /path/to/project
python3 /path/to/repository-health-checker/app.py
```

## Tests

Run the automated tests from this repository's root folder:

```bash
python3 -m unittest discover -s tests
```
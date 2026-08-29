#!/usr/bin/env python3
import subprocess
import sys


def lint() -> int:
    """Run pylint on all tracked Python files and return pylint's exit code.

    This collects all Python files tracked by git, runs pylint on them,
    prints the exit code, stdout and stderr, and returns the exit code.
    """

    files = subprocess.run(
        ["git", "ls-files", "*.py"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.splitlines()

    if not files:
        print("No Python files found.")
        return 0

    result = subprocess.run(
        [sys.executable, "-m", "pylint", *files],
        capture_output=True,
        text=True,
        check=False,
    )

    print("Exit code:", result.returncode)
    print("Output:")
    print(result.stdout)

    if result.stderr:
        print("Errors:")
        print(result.stderr)

    return result.returncode


if __name__ == "__main__":
    raise SystemExit(lint())

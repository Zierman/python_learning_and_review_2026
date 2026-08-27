#!/usr/bin/env python3
import subprocess
import sys


def install_dev_dependencies():  # pylint: disable=missing-function-docstring
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "-e", ".[dev]"],
        capture_output=False,
        text=True,
        check=True,
    )


def install_pre_commit():  # pylint: disable=missing-function-docstring
    subprocess.run(
        [sys.executable, "-m", "pre_commit", "install"],
        capture_output=False,
        text=True,
        check=True,
    )


def main():  # pylint: disable=missing-function-docstring
    try:
        print()
        print("Installing dev dependencies...")
        install_dev_dependencies()
        print()
        print("Installing pre-commit...")
        install_pre_commit()
        print()
        print("dev setup complete")
    except Exception:
        error_message = "    dev setup failed    "
        divider = len(error_message)*'-'
        print(divider, file=sys.stderr)
        print(error_message, file=sys.stderr)
        print(divider, file=sys.stderr)
        raise


if __name__ == "__main__":
    main()

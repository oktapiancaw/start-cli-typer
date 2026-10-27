#!/usr/bin/env python3
"""Runs after cookiecutter renders the project. Inits git, prints next steps."""

import subprocess
import sys
from pathlib import Path


def main() -> None:
    root = Path.cwd()
    try:
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"warning: git init skipped ({e})", file=sys.stderr)

    cli_command = "{{ cookiecutter.cli_command }}"
    print(
        f"\n Project ready at {root}\n"
        f"   Next: cd {root.name} && uv sync\n"
        f"   Run:  uv run {cli_command} --help"
    )


if __name__ == "__main__":
    main()

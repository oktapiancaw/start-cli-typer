#!/usr/bin/env python3
"""Personalize this template after `git clone`. Rewrites pyproject.toml, resets git.

Usage:
    git clone https://git.blackeye.id/utility/starter-cli-typer.git myapp
    cd myapp && python scaffold.py
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
PYPROJECT = ROOT / "pyproject.toml"


def ask(label: str, default: str) -> str:
    got = input(f"{label} [{default}]: ").strip()
    return got or default


def sub1(text: str, pattern: str, repl: str) -> str:
    new, n = re.subn(pattern, repl, text, count=1, flags=re.MULTILINE)
    assert n == 1, f"pattern not found (already scaffolded?): {pattern}"
    return new


def main() -> None:
    if not PYPROJECT.exists():
        sys.exit("pyproject.toml not found — run from the cloned repo root.")

    name = ask("Project name (kebab-case)", "my-cli")
    description = ask("Description", "A Typer CLI app")
    script = ask("CLI command name", name)

    text = PYPROJECT.read_text()
    text = sub1(text, r'^name = ".*"', f'name = "{name}"')
    text = sub1(text, r'^description = ".*"', f'description = "{description}"')
    text = sub1(text, r'^cli-data = ".*"', f'{script} = "src.main:app"')
    PYPROJECT.write_text(text)

    # fresh git history
    shutil.rmtree(ROOT / ".git", ignore_errors=True)
    subprocess.run(["git", "init", "-q"], cwd=ROOT, check=True)

    # self-delete: template-only file
    Path(__file__).unlink()

    print(f"\nDone. `{name}` ready. Run: uv sync && uv run {script} --help")


if __name__ == "__main__":
    main()

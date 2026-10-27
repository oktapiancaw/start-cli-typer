# {{ cookiecutter.project_name }}

{{ cookiecutter.package_description }}

Batteries-included [Typer](https://typer.tiangolo.com/) CLI: auto-discovered
subcommands, Pydantic settings, structured logging. Managed with
[uv](https://docs.astral.sh/uv/).

## Quick start

```bash
uv sync
uv run {{ cookiecutter.cli_command }} --help
uv run {{ cookiecutter.cli_command }} base hello --name World
# Hello, World!
```

## Project structure

```
src/
  main.py              # Typer entrypoint; wires regular commands + auto-loads onrequest/*
  commands/
    base.py            # regular command module (registered as `base`)
    <your_cmd>.py      # add new commands here — one module per subcommand
    onrequest/         # one-off, parameterless utilities; auto-loaded, no wiring
  configs/
    __init__.py        # logger setup + config/project_meta singletons
    env.py             # ApplicationConfig (Pydantic settings from .env)
  connections/         # place clients/adapters here
  core/                # place business logic here
  models/              # place data models here
public/                # input/ output/ cache/ data/ working dirs
logs/                  # rotating log files (prod_debug.log)
```

## Commands

Two panels:

- **regular** — modules under `src/commands/` (e.g. `base.py`). Wired explicitly
  in `main.py` with `app.add_typer(...)`. Use for real commands: anything with
  arguments, options, subcommands, or that you expect to maintain.
- **on-request** — modules under `src/commands/onrequest/`. Auto-discovered,
  no wiring. Reserved for throwaway, parameterless utilities (one-off scripts,
  quick dumps). If it takes a `--flag`, it does **not** belong here — promote
  it to a regular command.

```bash
uv run {{ cookiecutter.cli_command }} --help            # top-level, --verbose/-v enables debug logging
uv run {{ cookiecutter.cli_command }} base hello        # regular command
```

### Adding a regular command (default)

Create a module under `src/commands/` exposing a Typer `app`, then wire it in
`src/main.py`.

```python
# src/commands/greet.py
import typer
from typing import Annotated

app = typer.Typer()


@app.command()
def morning(name: Annotated[str, typer.Option()] = "World"):
    typer.echo(f"Good morning, {name}!")
```

```python
# src/main.py
from src.commands import base, greet
app.add_typer(base.app, name="base")
app.add_typer(greet.app, name="greet")
```

```bash
uv run {{ cookiecutter.cli_command }} greet morning --name Okta
```

### Adding a one-off (on-request) utility

Only when the task is parameterless and disposable. Drop a module in
`src/commands/onrequest/` that exposes a Typer `app` — it's auto-registered
under the module name, no edits to `main.py`.

```python
# src/commands/onrequest/dump_health.py
import typer

app = typer.Typer()


@app.command()
def run():
    typer.echo("ok")
```

```bash
uv run {{ cookiecutter.cli_command }} dump_health run
```

## Configuration

Copy `.env.example` to `.env`. Settings load via `ApplicationConfig` (nested
keys use `__`):

| Var          | Default            | Purpose            |
| ------------ | ------------------ | ------------------ |
| `OUTPUT_DIR` | `./public/output`  | Default output dir |

Access anywhere via `from src.configs import config` → `config.output_dir`.

## Development

```bash
uv run ruff check .        # lint (F/E/W/I/N/UP/B/S rule sets)
uv run ruff format .       # format
```

Requires Python >= {{ cookiecutter.python_version }}.

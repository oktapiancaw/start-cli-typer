# start-cli-typer

A batteries-included [Typer](https://typer.tiangolo.com/) CLI starter: auto-discovered subcommands, Pydantic settings, structured logging, and a post-clone scaffold script. Managed with [uv](https://docs.astral.sh/uv/).

## Quick start

```bash
git clone https://git.blackeye.id/utility/starter-cli-typer.git myapp
cd myapp
python scaffold.py          # prompts for name/description/command, resets git, self-deletes
uv sync
uv run <your-command> --help
```

Before scaffolding, the default command is `cli-data`:

```bash
uv run cli-data base hello --name World
# Hello, World!
```

## Project structure

```
src/
  main.py              # Typer entrypoint; auto-registers onrequest/* subcommands
  commands/
    base.py            # always-on commands (registered as `base`)
    onrequest/         # drop-in modules; any module exposing `app` is auto-loaded
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

Two panels: **base** (always registered) and **on-request** (auto-discovered).

```bash
uv run cli-data --help            # top-level, --verbose/-v enables debug logging
uv run cli-data base hello        # base commands
```

### Adding a command

Drop a module in `src/commands/onrequest/` that exposes a Typer `app`. It's auto-registered under the module name — no wiring in `main.py`.

```python
# src/commands/onrequest/greet.py
import typer

app = typer.Typer()


@app.command()
def morning(name: str = "World"):
    typer.echo(f"Good morning, {name}!")
```

```bash
uv run cli-data greet morning --name Okta
```

## Configuration

Copy `.env.example` to `.env`. Settings load via `ApplicationConfig` (nested keys use `__`):

| Var          | Default            | Purpose            |
| ------------ | ------------------ | ------------------ |
| `OUTPUT_DIR` | `./public/output`  | Default output dir |

Access anywhere via `from src.configs import config` → `config.output_dir`.

## Development

```bash
uv run ruff check .        # lint (F/E/W/I/N/UP/B/S rule sets)
uv run ruff format .       # format
```

Requires Python >= 3.12.

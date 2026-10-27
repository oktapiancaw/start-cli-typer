# start-cli-typer

Cookiecutter template for a Typer CLI app with auto-discovered subcommands,
pydantic-settings, structured logging, and `uv` packaging.

## Generate a project

```bash
uvx cookiecutter gh:oktapiancaw/start-cli-typer
# or from a local clone:
uvx cookiecutter path/to/start-cli-typer
```

Prompts collected:

| Variable              | Default                        |
| --------------------- | ------------------------------ |
| `project_name`        | `My CLI`                       |
| `project_slug`        | derived from name              |
| `cli_command`         | same as `project_slug`         |
| `package_description` | `A Typer CLI app`              |
| `author_name`         | `Your Name`                    |
| `author_email`        | `you@example.com`              |
| `python_version`      | `3.12`                         |

The post-gen hook runs `git init` and prints the next commands.

## Layout shipped to the generated project

```
<project_slug>/
  pyproject.toml
  .env.example
  .python-version
  README.md
  src/
    main.py              Typer entrypoint; auto-registers onrequest/*
    commands/
      base.py            always-on commands (`<cli> base ...`)
      onrequest/         drop-in modules; any `app` is auto-loaded
    configs/             logger + pydantic-settings
    connections/
    core/
    models/
  public/{cache,data,input,output}/
  tests/
  logs/
```

See the generated project's own `README.md` for day-to-day commands.

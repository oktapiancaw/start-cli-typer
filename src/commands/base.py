import logging
from datetime import datetime
from typing import Annotated

import typer

from src.configs import project_meta

LOGGER = logging.getLogger(project_meta.name)
execution_start = int(datetime.now().timestamp() * 1000)
app = typer.Typer(pretty_exceptions_show_locals=False)


@app.command()
def hello(name: Annotated[str | None, typer.Option()] = "Okta"):
    typer.echo(f"Hello, {name}!")

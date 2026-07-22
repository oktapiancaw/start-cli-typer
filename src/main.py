import importlib
import pkgutil

import typer

from src.commands import base, onrequest
from src.configs import CustomLogLevel, logging, project_meta

app = typer.Typer(pretty_exceptions_show_locals=False)

LOGGER = logging.getLogger(project_meta.name)


app.add_typer(base.app, name="base")


for mod in pkgutil.iter_modules(onrequest.__path__):
    sub = importlib.import_module(f"{onrequest.__name__}.{mod.name}")
    if hasattr(sub, "app"):  # skip empty/stub modules
        app.add_typer(sub.app, name=mod.name, rich_help_panel="on-request")


@app.callback()
def main(
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose logging"
    ),
):
    if verbose:
        logging.getLogger().setLevel(CustomLogLevel.INFO)
        LOGGER.debug("Verbose mode enabled")
    else:
        logging.getLogger().setLevel(CustomLogLevel.NOTSET)


if __name__ == "__main__":
    app()

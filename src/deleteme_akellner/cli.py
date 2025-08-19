"""Console script for deleteme_akellner."""

import typer
from rich.console import Console

from ._utils import example

app = typer.Typer()
console = Console()


@app.command()
def main() -> None:
    """Console script for deleteme_akellner."""
    console.print(
        "Replace this message by putting your code into deleteme_akellner.cli.main"
    )
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    example()


if __name__ == "__main__":
    app()

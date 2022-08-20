import typer
import os
from pathlib import Path

app = typer.Typer()


@app.command()
def init_terraform(
    location: Path = typer.Option(
        ".",
        "--location",
        "-l",
        help="The location where you want to initialize your Terraform project.",
    )
):
    files = ("main.tf", "variables.tf", "output.tf", "README.md")
    [os.makedirs(Path() / "terraform" / file) for file in files]


if __name__ == "__main__":
    app()

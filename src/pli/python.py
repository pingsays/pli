import typer
import os
from pathlib import Path
from typing import Optional

app = typer.Typer()


@app.command()
def init_python(
    location: Optional[Path] = typer.Option(
        ".",
        "--location",
        "-l",
        help="The location where you want to initialize your Python project.",
    )
):

    files = (
        "__init__.py",
        ".gitignore",
        "Dockerfile",
        "docker-compose.yml",
        ".dockerignore",
    )

    [os.makedirs(Path() / location / "src" / file) for file in files]


if __name__ == "__main__":
    app()

import typer
import os
from pathlib import Path

app = typer.Typer()


@app.command()
def init_python(
    location: Path = typer.Option(
        ".",
        "--location",
        "-l",
        help="The location where you want to initialize your Python project.",
    )
):

    # files to create in python project
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

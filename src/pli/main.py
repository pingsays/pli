import typer
import os
from typing import Optional

app = typer.Typer()


def init_terraform(pkg_location):
    terraform_files = ("main.tf", "variables.tf", "output.tf", "README.md")
    [os.makedirs(f"{pkg_location}/terraform/{file}") for file in terraform_files]
    # print(pkg_location)


@app.command()
def init(
    pkg_name: Optional[str] = typer.Option(
        "pkg_name", "--name", "-n", help="Give your application a name."
    ),
    location: Optional[str] = typer.Option(
        ".",
        "--location",
        "-l",
        help="Specify the location where you want to initialize the project.",
    ),
    terraform: bool = typer.Option(
        False,
        "--terraform",
        help="Initialize a Terraform module.",
    ),
):
    print(f"Initializing a new project at {location}")

    os.makedirs(f"{location}/src/{pkg_name}/__init__.py")

    if terraform:
        init_terraform(location)


@app.callback()
def callback():
    pass


if __name__ == "__main__":
    app()

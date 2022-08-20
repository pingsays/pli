import typer
import os
from typing import Optional
from pathlib import Path
import python
import pipeline
import terraform

app = typer.Typer()
app.add_typer(python.app, name="python")
app.add_typer(terraform.app, name="terraform")


features = ("Python", "Terraform", "Pipeline")


@app.command()
def all(
    value: bool = typer.Option(
        True, "--all", help=f"Initialize a project with all features: {features}."
    )
):
    pass


# def init(
#     pkg_name: Optional[str] = typer.Option(
#         "pkg_name", "--name", "-n", help="Give your application a name."
#     ),
#     location: Optional[Path] = typer.Option(
#         ".",
#         "--location",
#         "-l",
#         help="Specify the location where you want to initialize the project.",
#     ),
#     terraform: bool = typer.Option(
#         False,
#         "--terraform",
#         help="Initialize a Terraform module to the project.",
#     ),
#     pipeline: bool = typer.Option(
#         False, "--pipeline", help="Add a pipeline folder to the project."
#     ),
# ):
#     print(f"Initializing a new project at {location}")

#     # os.makedirs(f"{location}/src/{pkg_name}/__init__.py")
#     os.makedirs(Path() / location / "src" / pkg_name / __init__.py)

# if terraform:
#     init_terraform(location)

# if pipeline:
#     init_pipeline(location)


# def init_pipeline(location: Path):
#     os.makedirs(f"{location}/pipelines")


# @app.callback()
# def callback():
#     pass


if __name__ == "__main__":
    app()

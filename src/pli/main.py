import typer
import initialize

app = typer.Typer()
app.add_typer(initialize.app, name="init")

if __name__ == "__main__":
    app()

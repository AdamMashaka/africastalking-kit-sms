import typer
import shutil
from pathlib import Path

app = typer.Typer()


@app.command()
def init(project_name: str = "starter_project"):

    source = Path(__file__).parent / "templates"
    destination = Path(project_name)

    destination.mkdir(exist_ok=True)

    shutil.copy(
        source / "fastapi_app.py",
        destination / "main.py"
    )

    typer.echo(f"Project '{project_name}' created successfully!")
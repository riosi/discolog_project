from typing import Optional
import typer  # a biblioteca cria uma interface de CLI e utiliza type annotation
from beerlog.core import add_beer_to_database, get_beers_from_database
from rich.table import Table
from rich.console import Console

# objeto main que é a instância da classe Typer
main = typer.Typer(help="Beer Management Application")
console = Console()

# capturar comandos, ler os atributos
@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer to database."""
    if add_beer_to_database(name, style, flavor, image, cost):
        print("🍺 beer added to database" )


@main.command("list")
def list_beers(style: Optional[str] = None):
    """Lists beers in database."""
    beers = get_beers_from_database()
    table = Table(title="Beerlog :beer_mug:")
    headers = ["id", "name", "style", "rate", "date"]
    for header in headers:
        table.add_column(header, style="magenta")
    for beer in beers:
        beer.date = beer.date.strftime("%Y-%m-%d")
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)

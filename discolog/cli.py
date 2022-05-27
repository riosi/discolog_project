from typing import Optional

import typer  # a biblioteca cria uma interface de CLI e utiliza type annotation
from rich.console import Console
from rich.table import Table
from rich import print

from discolog.core import add_album_to_database, get_albums_from_database

# objeto main que é a instância da classe Typer
main = typer.Typer(help="Album Review Application")
console = Console()


# capturar comandos, ler os atributos
@main.command()
def add(
    name: str, 
    artist: str,
    year: int = typer.Option(...),
    rate: int = typer.Option(...),
    review: str = typer.Option(...),
):
    """Adds a new album to the database"""
    if add_album_to_database(name, artist, year, rate, review):
        print(":cd: Album added!!")
    else:
        print("Cannot add album.")

@main.command("list")
def list_albums(artist: Optional[str] = None):
    """Lists albums in database."""
    albums = get_albums_from_database()
    table = Table(title="Discolog :cd:", show_lines=True)
    headers = ["id", "name", "artist", "year", "rate", "review", "date"]
    for header in headers:
        table.add_column(header, style="magenta")
    for album in albums:
        album.date = album.date.strftime("%Y-%m-%d")
        values = [str(getattr(album, header)) for header in headers]
        table.add_row(*values)
    console.print(table)

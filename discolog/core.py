# salvar informações no banco de dados
from typing import List, Optional
from webbrowser import get
from sqlalchemy import delete

from sqlmodel import select

from discolog.database import get_session
from discolog.models import Album


def add_album_to_database(
    name: str,
    artist: str,
    year: int,
    rate: int,
    review: str
) -> bool:
    with get_session() as session:
        album = Album(
            name=name,
            artist=artist,
            year=year,
            rate=rate,
            review=review
        )
        session.add(album)
        session.commit()
    return True


def get_albums_from_database() -> List[Album]:
     with get_session() as session:
         sql = select(Album)  # select * from album;
         return list(session.exec(sql))


def delete_album_from_database(id) -> bool:
    with get_session() as session:
        sql = delete(Album).where(Album.id == id)
        session.exec(sql)
        session.commit()
    return True

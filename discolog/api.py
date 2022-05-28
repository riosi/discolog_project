from typing import List

from fastapi import FastAPI, Response, status
from sqlalchemy import delete, select, update  # ASGI -> protocolo da FastAPI

from discolog.core import get_albums_from_database
from discolog.database import get_session
from discolog.models import Album
from discolog.serializers import AlbumEdit, AlbumIn, AlbumOut

api = FastAPI(title="Discolog")


@api.get("/albums/", response_model=List[AlbumOut])
async def list_albums():
    albums = get_albums_from_database()
    return albums


@api.post("/albums/", response_model=AlbumOut)
async def add_album(album_in: AlbumIn):
    album = Album(**album_in.dict())
    with get_session() as session:
        session.add(album)
        session.commit()
        session.refresh(album)

    Response.status_code = status.HTTP_201_CREATED
    return album


@api.put("/albums/{id}/edit_review", response_model=AlbumEdit)
async def edit_album_review(id: int, album_edit: AlbumEdit):
    album = Album(**album_edit.dict())
    with get_session() as session:
        sql = update(Album).where(id == Album.id).values(review = album.review)
        session.exec(sql)
        session.commit()
    return album

@api.put("/albums/{id}/edit_name", response_model=AlbumEdit)
async def edit_album_name(id: int, album_edit: AlbumEdit):
    album = Album(**album_edit.dict())
    with get_session() as session:
        sql = update(Album).where(id == Album.id).values(name = album.name)
        session.exec(sql)
        session.commit()
    return album
   

@api.delete("/albums/{id}")
async def delete_album(id: int):
    with get_session() as session:
        sql = delete(Album).where(Album.id == id)
        session.exec(sql)
        session.commit()
    return "Album deleted successfully!"
       
      

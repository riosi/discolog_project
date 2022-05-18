# from typing import List

# from fastapi import FastAPI, Response, status  # ASGI -> protocolo da FastAPI

# from discolog.core import get_albums_from_database
# from discolog.database import get_session
# from discolog.models import Album
# from discolog.serializers import AlbumIn, AlbumOut

# api = FastAPI(title="Discolog")


# @api.get("/albums/", response_model=List[AlbumOut])
# async def list_albums():
#     albums = get_albums_from_database()
#     return albums


# @api.post("/albums/", response_model=AlbumOut)
# async def add_beer(album_in: AlbumIn):
#     album = Album(**album_in.dict())
#     with get_session() as session:
#         session.add(album)
#         session.commit()
#         session.refresh(album)

#     Response.status_code = status.HTTP_201_CREATED
#     return album

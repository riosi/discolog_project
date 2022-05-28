from datetime import datetime

from fastapi import HTTPException, status
from pydantic import BaseModel, validator


class AlbumOut(BaseModel):
    id: int
    name: str
    artist: str
    year: int
    rate: int
    review: str
    date: datetime


class AlbumIn(BaseModel):
    name: str
    artist: str
    year: int
    rate: int
    review: str

    @validator("rate")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise HTTPException(
                detail=f"{field.name} must be between 1 and 10",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return v


class AlbumEdit(BaseModel):
    name: str
    artist: str
    year: int
    rate: int
    review: str
from datetime import datetime
from typing import Optional
from pydantic import validator
from sqlmodel import Field, SQLModel
from sqlmodel import select


class Album(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    artist: str
    year: int
    rate: int
    review: str
    date: datetime = Field(default_factory=datetime.now)

    @validator("rate")  
    def validate_ratings(cls, v, field):  # classe, valor & campo
        if v < 0 or v > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return v


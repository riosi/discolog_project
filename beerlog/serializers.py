from datetime import datetime
from statistics import mean

from fastapi import HTTPException, status
from pydantic import BaseModel, validator


class BeerOut(BaseModel):
    # optional faz com que o próprio sql nos dê um id automático
    id: int
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0
    date: datetime


class BeerIn(BaseModel):
    name: str
    style: str
    flavor: int
    image: int
    cost: int

    @validator("image", "flavor", "cost")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise HTTPException(
                detail=f"{field.name} must be between 1 and 10",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return v

    @validator("rate", check_fields=False)
    def calculate_rate(cls, v, values):
        rate = mean([values["flavor"], values["image"], values["cost"]])
        return int(rate)

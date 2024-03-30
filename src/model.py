from typing import NamedTuple

from pydantic import BaseModel
from enum import Enum


class StatusExperation(Enum):
    FEW = 'RED'
    ORDER = 'YELLOW'
    MANY = 'GREEN'


class ContainerData(BaseModel):
    name: str
    weight: int
    value: int
    status: StatusExperation

    # class Config:
    #     json_encoders = {StatusExperation: lambda v: v.name}


class Container(NamedTuple):
    key: int
    data: ContainerData

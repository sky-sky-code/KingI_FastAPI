from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel

class TCBase(BaseModel):
    id: int
    title: str
    status: str
    count_pavilions: int
    city: str
    cost: Decimal
    add_value_rito: Decimal
    storyes: int
    photo: str

    class Config():
        orm_mode = True

class Worker(BaseModel):
    id: int
    email: str
    password: str
    role: str
    phone: str
    gender: str
    photo: str

    class Config():
        orm_mode = True

class Pavilion(BaseModel):
    id: int
    title_tc: str
    number_pavilion: str
    floor: int
    status: str
    area: int
    cost_sqm: Decimal
    add_value_rito: Decimal

class Tenant(BaseModel):
    id: int
    title_phone: str
    phone: str
    address: str

class Rent(BaseModel):
    id: int
    title_tc: str
    number_pavilion: str
    status: str
    start_rent: datetime
    finish_rent: datetime
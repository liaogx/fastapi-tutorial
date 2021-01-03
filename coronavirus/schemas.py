#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from datetime import date as date_
from datetime import datetime

from pydantic import BaseModel


class CreateData(BaseModel):
    date: date_
    confirmed: int = 0
    deaths: int = 0
    recovered: int = 0


class CreateCity(BaseModel):
    province: str
    country: str
    country_code: str
    country_population: int


class ReadData(CreateData):
    id: int
    city_id: int
    updated_at: datetime
    created_at: datetime

    class Config:
        orm_mode = True


class ReadCity(CreateCity):
    id: int
    updated_at: datetime
    created_at: datetime

    class Config:
        orm_mode = True

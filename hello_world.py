#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()  # 这里不一定是app，名字随意


class CityInfo(BaseModel):
    province: str
    country: str
    is_affected: Optional[bool] = None  # 与bool的区别是可以不传，默认是null


# @app.get('/')
# def hello_world():
#     return {'hello': 'world'}
#
#
# @app.get('/city/{city}')
# def result(city: str, query_string: Optional[str] = None):
#     return {'city': city, 'query_string': query_string}
#
#
# @app.put('/city/{city}')
# def result(city: str, city_info: CityInfo):
#     return {'city': city, 'country': city_info.country, 'is_affected': city_info.is_affected}
#

@app.get('/')
async def hello_world():
    return {'hello': 'world'}


@app.get('/city/{city}')
async def result(city: str, query_string: Optional[str] = None):
    return {'city': city, 'query_string': query_string}


@app.put('/city/{city}')
async def result(city: str, city_info: CityInfo):
    return {'city': city, 'country': city_info.country, 'is_affected': city_info.is_affected}

# 启动命令：uvicorn hello_world:app --reload

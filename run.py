#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

import uvicorn
from fastapi import FastAPI

from tutorial import app03
from coronavirus import application

app = FastAPI(
    title='FastAPI Tutorial and Coronavirus Tracker API Docs',
    description='FastAPI教程和新冠病毒疫情跟踪器API接口文档，项目地址：https://github.com/liaogx/fastapi-tutorial',
    version='1.0.0',
    docs_url='/docs',
    redoc_url='/redocs',
)

app.include_router(app03, prefix="/tutorial", tags=['Request请求'])
app.include_router(application, prefix="/coronavirus", tags=['Coronavirus Tracker'])

if __name__ == '__main__':
    uvicorn.run("run:app", host="0.0.0.0", port=8000, reload=True, debug=True, workers=1)

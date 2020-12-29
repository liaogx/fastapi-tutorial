#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from coronavirus import application
from tutorial import app03, app04

app = FastAPI(
    title='FastAPI Tutorial and Coronavirus Tracker API Docs',
    description='FastAPI教程 新冠病毒疫情跟踪器API接口文档，项目代码：https://github.com/liaogx/fastapi-tutorial',
    version='1.0.0',
    docs_url='/docs',
    redoc_url='/redocs',
)


# @app.exception_handler(StarletteHTTPException)  # 重写HTTPException异常处理器
# async def http_exception_handler(request, exc):
#     """
#     :param request: 这个参数不能省
#     :param exc:
#     :return:
#     """
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)
#
#
# @app.exception_handler(RequestValidationError)  # 重写请求验证异常处理器
# async def validation_exception_handler(request, exc):
#     """
#     :param request: 这个参数不能省
#     :param exc:
#     :return:
#     """
#     return PlainTextResponse(str(exc), status_code=400)


app.include_router(app03, prefix="/chapter03", tags=['第三章 请求参数和验证'])
app.include_router(app04, prefix="/chapter04", tags=['第四章 响应处理和FastAPI配置'])
app.include_router(application, prefix="/coronavirus", tags=['新冠病毒疫情跟踪器API'])

if __name__ == '__main__':
    uvicorn.run("run:app", host="0.0.0.0", port=8000, reload=True, debug=True, workers=1)

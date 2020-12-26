#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from fastapi import APIRouter

app03 = APIRouter()


@app03.get("/")
async def tutorial():
    """This is a simple tutorial"""
    return {"message": {"This is another route"}}

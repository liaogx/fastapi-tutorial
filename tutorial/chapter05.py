#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

# from typing import List
#
# from fastapi import Form, File, UploadFile
# from starlette.requests import Request
#
# from fastapi import APIRouter
#
#
# app02 = APIRouter()
#
#
# @app02.post("/user/")
# async def login_post(request: Request, username: str = Form(...), password: str = Form(...)):
#     """
#     Form表单操作
#     :param request:
#     :param username:
#     :param password:
#     :return:
#     """
#
#     print(f"username: {username}, password: {password}")
#
#     return templates.TemplateResponse("post.html", {"request": request, "username": username, "password": password})
#
#
# @app02.get("/user/")
# async def login_get(request: Request):
#     return templates.TemplateResponse("post.html", {"request": request})
#
#
# @app02.get("/file/")
# async def login_get(request: Request):
#     return templates.TemplateResponse("file.html", {"request": request})
#
#
# @app02.post("/file/")
# async def upload_file(request: Request, files_list: List[bytes] = File(...), files_name: List[UploadFile] = File(...)):
#     """
#     上传多个文件
#     :param request:
#     :param files_list: List[bytes]表示可上传多个文件，bytes表示上传一个文件
#     :param files_name:
#     :return:
#     """
#
#     return templates.TemplateResponse("file.html", {
#         "request": Request,
#         "file_sizes": [len(file) for file in files_list],  # 用字节长度表示文件大小
#         "filenames": [file.filename for file in files_name]
#     })
#
#
# @app02.post("/create_file/")
# async def create_file(request: Request, file1: bytes = File(...), file2: UploadFile = File(...), notes: str = Form(...)):
#     """
#     上传单个文件
#     :param request:
#     :param file1: bytes类型可以统计长度，但是没有content_type属性
#     :param file2: UploadFile类有content_type属性，但是不能len()统计文件长度
#     :param notes:
#     :return:
#     """
#
#     return templates.TemplateResponse("file.html", {
#         "request": Request,
#         "file_size": len(file1),
#         "notes": notes,
#         "file2_content_type": file2.content_type
#     })

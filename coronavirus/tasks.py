#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

# import time
# from datetime import datetime
#
# from fastapi import BackgroundTasks
#
# from coronavirus import app
#
#
# def _run_task(name: str, id_=None):  # _开头表示私有函数
#     time.sleep(3)
#     with open("tasks_out.txt", mode="a") as file:
#         now = datetime.now()
#         content = f"{name} [{id_}]: {now}\n"
#         file.write(content)
#
#
# @app.post("/task/run/{name}/{id_}")
# async def task_run(name: str, id_: int, background_task: BackgroundTasks):
#     """receiver a task, and writes it into a file"""
#     background_task.add_task(_run_task, name=name, id_=id_)
#     return {"message": f"Task {name} ID {id_} is being run."}

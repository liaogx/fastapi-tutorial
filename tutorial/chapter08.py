#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from typing import Optional

from fastapi import APIRouter, BackgroundTasks, Depends

app08 = APIRouter()

"""【见run.py】Middleware 中间件"""

# 注：带yield的依赖的退出部分的代码 和 后台任务 会在中间件之后运行

"""【见run.py】CORS (Cross-Origin Resource Sharing) 跨源资源共享"""

# 域的概念：协议+域名+端口

"""Background Tasks 后台任务"""


def bg_task(framework: str):
    with open("README.md", mode="a") as f:
        f.write(f"## {framework} 框架精讲")


@app08.post("/background_tasks")
async def run_bg_task(framework: str, background_tasks: BackgroundTasks):
    """
    :param framework: 被调用的后台任务函数的参数
    :param background_tasks: FastAPI.BackgroundTasks
    :return:
    """
    background_tasks.add_task(bg_task, framework)
    return {"message": "任务已在后台运行"}


def continue_write_readme(background_tasks: BackgroundTasks, q: Optional[str] = None):
    if q:
        background_tasks.add_task(bg_task, "\n> 整体的介绍 FastAPI，快速上手开发，结合 API 交互文档逐个讲解核心模块的使用\n")
    return q


@app08.post("/dependency/background_tasks")
async def dependency_run_bg_task(q: str = Depends(continue_write_readme)):
    if q:
        return {"message": "README.md更新成功"}

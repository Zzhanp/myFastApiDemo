# -*- coding: utf-8 -*-            
# @Author : Zzhan
# @Time : 2024/7/9 19:57
from fastapi import APIRouter
from pydantic import BaseModel, Field, validator
from common import commonResult
from services import autoPlatformService
from loguru import logger


class Task(BaseModel):
    modules: dict = Field(default_factory=dict, description="模块与对应分支")


class TaskRemote(BaseModel):
    modules: dict = Field(default_factory=dict, description="模块与对应分支")
    ip: str = Field(default="", description="远程服务器ip")
    username: str = Field(default="", description="远程服务器用户名")
    password: str = Field(default="", description="远程服务器密码")


class Callback(BaseModel):
    task_id: str = Field(default="", description="任务id")
    status: int = Field(default="", description="任务状态")

# @field_validator("modules")
# def check_modules(v):
#     if not isinstance(v, dict):
#         raise ValueError("modules must be dict")
#     return v


autoPlatform = APIRouter(prefix="/autoPlatform")


@autoPlatform.post("/updategit")
def checkout_branch(task: Task):
    try:
        logger.info("更新git")
        result = autoPlatformService.checkout_branch(task.modules)
        if result:
            return commonResult.response()
        else:
            return commonResult.response(code=999, message="更新失败")
    except Exception as e:
        logger.error(e)
        return commonResult.response(code=999, message="更新失败")


@autoPlatform.post("/updategitremote")
def checkout_branch_remote(task: TaskRemote):
    try:
        logger.info("更新git")
        result = autoPlatformService.checkout_branch_remote(task)
        if result:
            return commonResult.response()
        else:
            return commonResult.response(code=999, message="更新失败")
    except Exception as e:
        logger.error(e)
        return commonResult.response(code=999, message="更新失败")


@autoPlatform.post("/callback")
def callback(c: Callback):
    result = autoPlatformService.callback(c)
    if result:
        return commonResult.response()
    else:
        return commonResult.response(code=999, message="回调失败")

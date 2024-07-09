# -*- coding: utf-8 -*-            
# @Author : Zzhan
# @Time : 2024/7/9 19:57
from datetime import date
from typing import Any
from typing_extensions import Self

from fastapi import APIRouter
from pydantic import BaseModel, Field, field_validator
from common import commonResult
from models.autoPlatform import updateGit


class Task(BaseModel):
    modules: dict = Field(default_factory=dict, description="模块与对应分支")


autoPlatform = APIRouter(prefix="/autoPlatform")


@autoPlatform.post("/updategit")
def checkout_branch(task: Task):
    task.modules = {
        "srm": "master",
        "sdsdata": "test_branch"
    }
    return updateGit.checkout_branch(task.modules)


if __name__ == '__main__':
    checkout_branch(Task())

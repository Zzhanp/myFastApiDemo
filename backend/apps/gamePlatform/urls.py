# -*- coding: utf-8 -*-            
# @Author : Zzhan
# @Time : 2024/7/2 14:47
from datetime import date
from typing import Any
from typing_extensions import Self

from fastapi import APIRouter
from pydantic import BaseModel, Field, field_validator
from common import commonResult

class Game(BaseModel):
    gameName: str
    platform: str = None
    gamePrice: float = None
    purchaseDate: date = None
    gameAccount: str = None

    @field_validator("gamePrice")
    def check_price(cls, value):
        if value < 0:
            raise ValueError("price must be greater than 0")


gamePlatform = APIRouter(prefix="/gamePlatform")


@gamePlatform.post("/list")
def get_game_list(game: Game):
    data = {
        "gameName": "大表哥",
        "platform": "Steam",
        "gamePrice": "20.00",
        "purchaseDate": "2024-02-01",
        "gameAccount": "Zzhanp"
    }
    return commonResult.resp_200(data=data)

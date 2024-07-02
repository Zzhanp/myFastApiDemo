# -*- coding: utf-8 -*-            
# @Author : Zzhan
# @Time : 2024/7/2 14:47
from datetime import date

from fastapi import APIRouter
from pydantic import BaseModel


class Game(BaseModel):
    gameName: str
    purchasePlatform: str = None
    gamePrice: float = None
    purchaseDate: date = None
    gameAccount: str = None


gamePlatform = APIRouter(prefix="/gamePurchase")


@gamePlatform.post("/list")
def get_game_list(game: Game):
    return {"code": 200, "msg": "success", "data": [{"id": 1, "name": "王者荣耀", "price": 100}, {"id": 2, "name": "绝地求生", "price": 200}]}
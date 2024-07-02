from fastapi import FastAPI
from apps.gamePlatform.urls import gamePlatform
app = FastAPI()

app.include_router(gamePlatform)

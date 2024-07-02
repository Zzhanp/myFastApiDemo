from fastapi import FastAPI
from apps.urls import gamePlatform
app = FastAPI()

app.include_router(gamePlatform)

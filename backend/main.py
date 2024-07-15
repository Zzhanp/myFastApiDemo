from fastapi import FastAPI
from apis.gamePlatformApi import gamePlatform
from apis.autoPlatformApi import autoPlatform
from common.log import init_logger, logger
import uvicorn


app = FastAPI()
app.include_router(autoPlatform)
app.include_router(gamePlatform)


async def init_app():
    init_logger()
    logger.info("日志初始化成功！！!")


@app.on_event("startup")
async def startup():
    await init_app()


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8679, reload=True)
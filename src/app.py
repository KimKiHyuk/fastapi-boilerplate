from typing import Optional
from fastapi import FastAPI
from src.router.status_router import router as status_router
from src.router.index_router import router as index_router
from src.database.mongodb import connect_mongo, disconnect_mongo
from dotenv import load_dotenv
from pathlib import Path
import os
import logging
import logging.config
from src.database.redis import connect_redis, disconnect_redis

load_dotenv(dotenv_path=f".{os.getenv('DOT_ENV', 'test')}.env")
logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    app = FastAPI()
    return app


app = create_app()
app.include_router(index_router, prefix="/api")
app.include_router(status_router, prefix="/api/status")


@app.on_event("startup")
async def on_app_start():
    mongo_conn_url = os.getenv("MONGO_CONNECTION_URL")
    redis_conn_url = os.getenv("REDIS_CONNECTION_URL")

    if mongo_conn_url:
        await connect_mongo(mongo_conn_url)

    if redis_conn_url:
        await connect_redis(redis_conn_url)


@app.on_event("shutdown")
async def on_app_shutdown():
    await disconnect_mongo()
    await disconnect_redis()

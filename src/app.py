from typing import Optional
from fastapi import FastAPI
from .router.status_router import router as status_router
from .router.index_router import router as index_router
import logging
import logging.config
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(dotenv_path=f".{os.getenv('DOT_ENV')}.env")
logging.config.fileConfig("./logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    app = FastAPI()
    return app


app = create_app()
app.include_router(status_router)
app.include_router(index_router)


@app.on_event("startup")
async def on_app_start():
    logger.info("hello!")


@app.on_event("shutdown")
async def on_app_shutdown():
    """Anything that needs to be done while app shutdown"""
    logger.info("good bye!")

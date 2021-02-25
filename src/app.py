from typing import Optional
from fastapi import FastAPI

from .router.status_router import router as status_router
from .router.index_router import router as index_router


def create_app() -> FastAPI:
    app = FastAPI()
    return app


app = create_app()
app.include_router(status_router)
app.include_router(index_router)


@app.on_event("startup")
async def on_app_start():
    """Anything that needs to be done while app starts"""
    print("app started")


@app.on_event("shutdown")
async def on_app_shutdown():
    """Anything that needs to be done while app shutdown"""
    print("app closed")

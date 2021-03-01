import logging
from src.database.redis import RedisDatabase
from aioredis.commands import Redis

from fastapi import APIRouter, Depends, HTTPException
from src.database.mongodb import AsyncIOMotorClient, get_connection as mongo_connection
from src.database.redis import get_connection as redis_connection
from src.dtos.status_dto import HealthStatusOutDto, StatusOutDto
from src.models.status_model import HealthStatusModel, StatusModel
from src.services.status_service import StatusService
from src.database.redis import db

logger = logging.getLogger(__name__)

router = APIRouter(tags=["index"])


@router.get(
    "/",
    responses={200: {"description": "ok"}},
)
async def index() -> dict:
    return {"system": True}

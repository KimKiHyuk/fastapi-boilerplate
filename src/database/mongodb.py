from motor.motor_asyncio import AsyncIOMotorClient
import src.config as config
import logging
import pymongo

__all__ = ["get_connection"]

logger = logging.getLogger(__name__)


class MongoDataBase:
    client: AsyncIOMotorClient = None


db = MongoDataBase()


def get_connection() -> AsyncIOMotorClient:
    return db.client


async def connect_mongo(
    connect_string: str, max_pool_size: int = 10, min_pool_size: int = 1
):
    db.client = AsyncIOMotorClient(
        connect_string, maxPoolSize=max_pool_size, minPoolSize=min_pool_size
    )


async def disconnect_mongo():
    await db.client.close()

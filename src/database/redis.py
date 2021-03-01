import asyncio
from aioredis import create_redis_pool, Redis
import logging

logger = logging.getLogger(__name__)


class RedisDatabase:
    client: Redis = None


db = RedisDatabase()


def get_connection() -> Redis:
    return db.client


async def connect_redis(connect_string: str):
    logger.info("connect redis")
    db.client = await create_redis_pool(connect_string)


async def disconnect_redis():
    logger.info("disconnect redis")
    await db.client.close()


# >>> pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
# >>> r = redis.Redis(connection_pool=pool)

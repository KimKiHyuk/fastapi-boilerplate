from src.database.mongodb import get_connection

"""
In vscode, AsyncIOMotorClient intelisense not works.
so wrappping it with custom method
"""


async def insert_one(database: str, collection: str, param: dict):
    return await get_connection()[database][collection].insert_one(param)


async def find_one(database: str, collection: str, param: dict):
    return await get_connection()[database][collection].find_one(param)

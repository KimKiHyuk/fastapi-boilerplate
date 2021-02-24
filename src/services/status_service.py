from ..repo.status_repo import StatusRepository
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi import Depends


class StatusService:
    def __init__(self, status_repo: StatusRepository = Depends(StatusRepository)):
        self.status_repo = status_repo

    async def check_alive(self, id: int):
        return await self.status_repo.get(id)

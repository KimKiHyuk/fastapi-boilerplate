from ..dtos.status_dto import StatusOutDto
from ..models.status_model import StatusModel


class StatusRepository:
    def __init__(self):
        pass

    async def get(self, id: int):
        return StatusModel(id=id, os=" ubuntu ", gpu_status=False)

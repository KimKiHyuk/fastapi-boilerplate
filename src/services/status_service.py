import logging
import src.config as config
from src.models.status_model import HealthStatusModel, StatusModel
from src.repo.base_repo import find_one, insert_one

logger = logging.getLogger(__name__)


class StatusService:
    async def check_alive(self, id: int):
        return StatusModel(id=id, os=" ubuntu ", gpu_status=False)

    async def health_check(self):
        created_model = HealthStatusModel(
            service_name="boilerplate", ip="127.0.0.1", alive=True, version=1
        )

        result = await insert_one(
            config.DB_DEVELOPMENT,
            config.COLLECTION_STATUS,
            created_model.dict(by_alias=True),
        )

        get_result = await find_one(
            config.DB_DEVELOPMENT,
            config.COLLECTION_STATUS,
            {"_id": result.inserted_id},
        )

        return get_result

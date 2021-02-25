from fastapi import APIRouter, Depends, HTTPException
from ..models.status_model import StatusModel
from ..services.status_service import StatusService
from ..dtos.status_dto import StatusOutDto
import logging


logger = logging.getLogger(__name__)
router = APIRouter()


@router.get(
    "/",
    responses={200: {"description": "ok"}},
)
async def proper_name_for_explanation() -> dict:
    logger.info("api called")
    return {"result": False}

from fastapi import APIRouter, Depends, HTTPException
from ..models.status_model import StatusModel
from ..services.status_service import StatusService
from fastapi_utils.cbv import cbv
from ..dtos.status_dto import StatusOutDto
from fastapi_utils.inferring_router import InferringRouter

router = APIRouter(
    prefix="/status",
    tags=["status", "system"],
    responses={404: {"description": "not found"}, 200: {"description": "ok"}},
)


@router.get(
    "/",
    tags=["index"],
    responses={512: {"description": "my error"}},
    response_model=StatusOutDto,
)
async def proper_name_for_explanation(
    status_service: StatusService = Depends(StatusService),
) -> StatusOutDto:
    from_db = await status_service.check_alive(15)
    return StatusOutDto(id=from_db.id, os=from_db.os, gpu_status=from_db.gpu_status)

from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from src.dtos.status_dto import HealthStatusOutDto, StatusOutDto
from src.models.status_model import StatusModel
from src.services.status_service import StatusService

router = APIRouter(
    tags=["status"],
    responses={404: {"description": "not found"}, 200: {"description": "ok"}},
)


@router.get(
    "/me",
    responses={200: {"description": "ok", "model": HealthStatusOutDto}},
)
async def index(
    status_service: StatusService = Depends(StatusService),
) -> HealthStatusOutDto:
    health_status = await status_service.health_check()

    return HealthStatusOutDto(**health_status)


@router.get(
    "/gpu",
    responses={512: {"description": "my error"}},
    response_model=StatusOutDto,
)
async def get_gpu_status(
    status_service: StatusService = Depends(StatusService),
) -> StatusOutDto:
    from_db = await status_service.check_alive(15)
    return StatusOutDto(id=from_db.id, os=from_db.os, gpu_status=from_db.gpu_status)

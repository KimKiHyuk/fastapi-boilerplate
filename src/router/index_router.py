from fastapi import APIRouter, Depends, HTTPException
from ..models.status_model import StatusModel
from ..services.status_service import StatusService
from fastapi_utils.cbv import cbv
from ..dtos.status_dto import StatusOutDto
from fastapi_utils.inferring_router import InferringRouter

router = APIRouter()


@router.get(
    "/",
    responses={200: {"description": "ok"}},
)
async def proper_name_for_explanation() -> dict:
    return {"result": True}

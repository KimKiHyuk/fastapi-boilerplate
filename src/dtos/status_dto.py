from src.dtos.base_dto import BaseDtoMixin
from typing import Optional
from pydantic import BaseModel, validator, Field
from src.models.base_model import PyObjectId
from datetime import date, datetime


class HealthStatusOutDto(BaseDtoMixin):
    def __init__(self, **data):
        super().__init__(**data)

    ip: Optional[str]
    alive: Optional[bool]
    service_name: Optional[str]
    optional_field: Optional[str] = None


# sample for neuralworks.. WIP
class StatusOutDto(BaseModel):
    _id: Optional[PyObjectId] = Field(alias="_id")
    id: int = ...
    os: str = ...
    gpu_status: bool = ...

    @validator("os")
    def check_os(cls, os, values):
        print(os, values)
        return os.strip()

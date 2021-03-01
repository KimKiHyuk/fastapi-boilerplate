from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field
from src.models.base_model import PyObjectId


class HealthStatusModel(BaseModel):
    _id: Optional[PyObjectId] = Field(alias="_id")
    service_name: str = ...
    ip: str = ...
    alive: bool = ...
    version: int = ...

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


# for neural works
class StatusModel:
    id: int
    os: str
    gpu_status: bool = False

    def __init__(self, *args, **kwargs):
        self.id = kwargs.get("id")
        self.os = kwargs.get("os")
        self.gpu_status = kwargs.get("gpu_status")

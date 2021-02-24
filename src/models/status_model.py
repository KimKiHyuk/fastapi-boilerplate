from typing import Optional
from pydantic import BaseModel


class StatusModel:
    id: int
    os: str
    gpu_status: bool = False

    def __init__(self, *args, **kwargs):
        self.id = kwargs.get("id")
        self.os = kwargs.get("os")
        self.gpu_status = kwargs.get("gpu_status")

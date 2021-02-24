from typing import Optional
from pydantic import BaseModel, validator


class StatusOutDto(BaseModel):
    id: int
    os: str
    gpu_status: bool

    @validator("os")
    def check_os(cls, os, values):
        print(os, values)
        return os.strip()

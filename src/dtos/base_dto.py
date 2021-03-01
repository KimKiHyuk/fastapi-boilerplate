from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel, Field


class BaseDtoMixin(BaseModel):
    def __init__(self, **data):
        if "_id" in data:
            data["created_at"] = data["_id"].generation_time
            data["_id"] = str(data["_id"])
        super().__init__(**data)

    id: Optional[str] = Field(
        alias="_id",
    )
    created_at: Optional[datetime] = None

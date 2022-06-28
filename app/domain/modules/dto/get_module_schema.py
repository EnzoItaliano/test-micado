from bson import ObjectId
from pydantic import BaseModel, Field

from app.core.common.base_entity import PyObjectId


class GetModulesDto(BaseModel):
    id: PyObjectId = Field(alias="_id")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

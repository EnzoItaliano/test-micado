from typing import List
from bson import ObjectId
from pydantic import BaseModel, Field

from app.core.common.base_entity import PyObjectId
from app.domain.modules.entities.components_entity import Components


class GetModulesDto(BaseModel):
    id: PyObjectId = Field(alias="_id")
    name: str = None
    price: float = 0
    components: List[Components] = []

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        orm_mode = True

from typing import List

from app.core.common.base_entity import BaseGetEntity
from app.domain.modules.entities.components_entity import Components


class GetModulesDto(BaseGetEntity):
    name: str = None
    price: float = 0
    components: List[Components] = []

    class Config:
        orm_mode = True

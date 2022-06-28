from typing import List
from app.core.common.base_entity import BaseEntity

from app.modules.entities.components_entity import Components


class ModulesEntity(BaseEntity):
    name: str = None
    price: float = 0
    components: List[Components] = []

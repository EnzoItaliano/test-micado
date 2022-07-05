from typing import List

from pydantic import Extra
from app.core.common.base_entity import BaseEntity

from app.domain.modules.entities.components_entity import Components


class CreateModuleDto(BaseEntity, extra=Extra.forbid):
    name: str
    price: float
    components: List[Components]

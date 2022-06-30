from typing import List

from pydantic import BaseModel, Extra

from app.domain.modules.entities.components_entity import Components


class CreateModuleDto(BaseModel, extra=Extra.forbid):
    name: str
    price: float
    components: List[Components]

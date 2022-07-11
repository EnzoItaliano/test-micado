from typing import List
from pydantic import BaseModel, Extra

from app.domain.modules.entities.components_entity import Components


class ModuleBudgetRequest(BaseModel, extra=Extra.forbid):
    name: str
    units: int


class BudgetRequest(BaseModel, extra=Extra.forbid):
    modules: List[ModuleBudgetRequest]


class BudgetResponse(BaseModel):
    module: str
    units: int
    unit_price: float
    total_price: float
    components: Components

from typing import Dict
from pydantic import BaseModel, Extra
from app.domain.contents.dtos.grids_schema import GridsObject
from app.domain.contents.dtos.groups_schema import GroupObject
from app.domain.contents.dtos.guides_schema import GuidesObject
from app.domain.contents.dtos.layers_schema import LayersObject


class CreateContentDto(BaseModel, extra=Extra.forbid):
    unit: str
    name: str
    layers: Dict[str, LayersObject]
    grids: GridsObject
    selected_layer: str
    groups: Dict[str, GroupObject]
    width: int
    height: int
    meta: object
    guides: GuidesObject
    customer: str

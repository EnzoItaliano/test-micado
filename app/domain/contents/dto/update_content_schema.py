from typing import Dict
from pydantic import BaseModel, Extra
from app.domain.contents.dto.grids_schema import GridsObject
from app.domain.contents.dto.groups_schema import GroupObject
from app.domain.contents.dto.guides_schema import GuidesObject
from app.domain.contents.dto.layers_schema import LayersObject


class UpdateContentDto(BaseModel, extra=Extra.forbid):
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

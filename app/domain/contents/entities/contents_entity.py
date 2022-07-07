from typing import Dict, List
from pydantic import Extra
from app.core.common.base_entity import BaseEntity, PyObjectId
from app.domain.contents.dtos.grids_schema import GridsObject
from app.domain.contents.dtos.groups_schema import GroupArrayObject
from app.domain.contents.dtos.guides_schema import GuidesArrayObject
from app.domain.contents.dtos.layers_schema import LayersArrayObject


class ContentEntity(BaseEntity, extra=Extra.forbid):
    name: str
    unit: str
    layers: List[LayersArrayObject]
    grids: GridsObject
    selected_layer: str
    groups: List[GroupArrayObject]
    width: int
    height: int
    meta: object
    guides: GuidesArrayObject
    customer: PyObjectId

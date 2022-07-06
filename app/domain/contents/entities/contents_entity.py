from typing import Dict
from pydantic import Extra
from app.core.common.base_entity import BaseEntity, PyObjectId
from app.domain.contents.dtos.grids_schema import GridsObject
from app.domain.contents.dtos.groups_schema import GroupObject
from app.domain.contents.dtos.guides_schema import GuidesObject
from app.domain.contents.dtos.layers_schema import LayersObject


class ContentEntity(BaseEntity, extra=Extra.forbid):
    name: str
    unit: str
    layers: Dict[str, LayersObject]
    grids: GridsObject
    selected_layer: str
    groups: Dict[str, GroupObject]
    width: int
    height: int
    meta: object
    guides: GuidesObject
    customer: PyObjectId

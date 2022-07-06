from typing import Dict
from pydantic import BaseModel, Extra

from app.domain.contents.dtos.layers_schema import SelectedObject


class GroupObject(BaseModel, extra=Extra.forbid):
    id: str
    type: str
    prototype: str
    name: str
    misc: object
    selected: bool
    properties: object
    visible: bool
    x: float
    y: float
    rotation: float
    elements: Dict[str, SelectedObject]

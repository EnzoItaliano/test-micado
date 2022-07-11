from typing import Dict, List
from pydantic import BaseModel, Extra

from app.domain.contents.dto.layers_schema import SelectedObject, SelectedArrayObject


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
    rotation: int
    elements: Dict[str, SelectedObject]


class GroupArrayObject(BaseModel, extra=Extra.forbid):
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
    rotation: int
    elements: List[SelectedArrayObject]

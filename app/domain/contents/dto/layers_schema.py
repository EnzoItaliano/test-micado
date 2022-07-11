from typing import Dict, List
from pydantic import BaseModel, Extra, validator


class SelectedObject(BaseModel, extra=Extra.forbid):
    vertices: List[str] = None
    lines: List[str] = None
    holes: List[str] = None
    areas: List[str] = None
    items: List[str] = None


class SelectedArrayObject(BaseModel, extra=Extra.forbid):
    vertices: List[str] = None
    lines: List[str] = None
    holes: List[str] = None
    areas: List[str] = None
    items: List[str] = None
    layer: str


class ItemsObject(BaseModel, extra=Extra.forbid):
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


class AreasObject(BaseModel, extra=Extra.forbid):
    id: str
    type: str
    prototype: str
    name: str
    misc: object
    selected: bool
    properties: object
    visible: bool
    vertices: List[str]
    holes: List[str]


class HolesObject(BaseModel, extra=Extra.forbid):
    id: str
    type: str
    prototype: str
    name: str
    misc: object
    selected: bool
    properties: object
    visible: bool
    offset: float
    line: str


class LinesObject(BaseModel, extra=Extra.forbid):
    id: str
    type: str
    prototype: str
    name: str
    misc: object
    selected: bool
    properties: object
    visible: bool
    proj_mod: Dict[str, int]
    vertices: List[str]
    holes: List[str]


class ProjModObject(BaseModel, extra=Extra.forbid):
    id: str
    value: int


class LinesArrayObject(BaseModel, extra=Extra.forbid):
    id: str
    type: str
    prototype: str
    name: str
    misc: object
    selected: bool
    properties: object
    visible: bool
    proj_mod: List[ProjModObject]
    vertices: List[str]
    holes: List[str]


class VerticesObject(BaseModel, extra=Extra.forbid):
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
    lines: List[str]
    areas: List[str]


class LayersObject(BaseModel, extra=Extra.forbid):
    id: str
    altitude: int
    order: int
    opacity: int
    name: str
    visible: bool
    vertices: Dict[str, VerticesObject]
    lines: Dict[str, LinesObject]
    holes: Dict[str, HolesObject]
    areas: Dict[str, AreasObject]
    items: Dict[str, ItemsObject]
    selected: SelectedObject


class LayersArrayObject(BaseModel, extra=Extra.forbid):
    id: str
    altitude: int
    order: int
    opacity: int
    name: str
    visible: bool
    vertices: List[VerticesObject]
    lines: List[LinesArrayObject]
    holes: List[HolesObject]
    areas: List[AreasObject]
    items: List[ItemsObject]
    selected: SelectedObject

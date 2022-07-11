from typing import List
from pydantic import BaseModel, Extra


class PropertiesObjects(BaseModel, extra=Extra.forbid):
    step: int
    colors: List[str]


class GridObjects(BaseModel, extra=Extra.forbid):
    id: str
    type: str
    properties: PropertiesObjects


class GridsObject(BaseModel, extra=Extra.forbid):
    h1: GridObjects
    v1: GridObjects

from typing import Dict, List
from pydantic import BaseModel, Extra

from app.domain.contents.dtos.layers_schema import ProjModObject


class GuidesObject(BaseModel, extra=Extra.forbid):
    horizontal: Dict[str, int]
    vertical: Dict[str, int]
    circular: Dict[str, int]


class GuidesArrayObject(BaseModel, extra=Extra.forbid):
    horizontal: List[ProjModObject]
    vertical: List[ProjModObject]
    circular: List[ProjModObject]

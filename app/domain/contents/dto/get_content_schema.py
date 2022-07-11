from app.core.common.base_entity import BaseGetEntity, PyObjectId


class GetContentDto(BaseGetEntity):
    unit: str
    name: str
    layers: object
    grids: object
    selected_layer: str
    groups: object
    width: int
    height: int
    meta: object
    guides: object
    customer: PyObjectId

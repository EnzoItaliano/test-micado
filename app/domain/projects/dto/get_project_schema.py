from app.core.common.base_entity import BaseGetEntity, PyObjectId


class GetProjectDto(BaseGetEntity):
    contents: PyObjectId
    status: str
    forecast: str
    reviewer: PyObjectId
    owner: PyObjectId

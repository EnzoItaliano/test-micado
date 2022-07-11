from app.core.common.base_entity import BaseEntity, PyObjectId


class ProjectsEntity(BaseEntity):
    contents: PyObjectId
    status: str
    forecast: str
    reviewer: PyObjectId
    owner: PyObjectId

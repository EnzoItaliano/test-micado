from pydantic import BaseModel, Extra


class GuidesObject(BaseModel, extra=Extra.forbid):
    horizontal: object
    vertical: object
    circular: object

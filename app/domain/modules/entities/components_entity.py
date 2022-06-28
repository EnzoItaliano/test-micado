from pydantic import BaseModel


class Components(BaseModel):
    name: str = None
    units: int = 0
    description: str = None

from typing import Optional
from pydantic import BaseModel, Extra


class UpdateCustomersDto(BaseModel, extra=Extra.forbid):
    name: Optional[str]
    nif: Optional[int]
    username: Optional[str]
    password: Optional[str]
    email: Optional[str]

from pydantic import BaseModel, Extra


class CreateCustomersDto(BaseModel, extra=Extra.forbid):
    name: str
    nif: int
    username: str
    password: str
    email: str

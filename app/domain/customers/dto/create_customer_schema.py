from pydantic import BaseModel, Extra, validator

from app.core.helpers.hash_utils import get_password_hash, is_hash


class CreateCustomersDto(BaseModel, extra=Extra.forbid):
    name: str
    nif: int
    username: str
    password: str
    email: str

    @validator("password", pre=True)
    def parse_birthdate(cls, value):
        if value is not None and not is_hash(value):
            return get_password_hash(value)

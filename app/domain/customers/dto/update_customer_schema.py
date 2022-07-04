from typing import Optional
from pydantic import BaseModel, Extra, validator

from app.core.helpers.hash_utils import get_password_hash, is_hash


class UpdateCustomersDto(BaseModel, extra=Extra.forbid):
    name: Optional[str]
    nif: Optional[int]
    username: Optional[str]
    password: Optional[str]
    email: Optional[str]

    @validator("password", pre=True)
    def parse_birthdate(cls, value):
        if value is not None and not is_hash(value):
            return get_password_hash(value)

from app.core.common.base_entity import BaseGetEntity
from app.core.constants.enums.role_enum import Role


class GetCustomersDto(BaseGetEntity):
    name: str
    nif: int
    username: str
    email: str
    role: Role


class GetCustomerFullDto(BaseGetEntity):
    name: str
    nif: int
    username: str
    email: str
    password: str
    role: Role

from app.core.common.base_entity import BaseEntity
from app.core.constants.enums.role_enum import Role


class CustomersEntity(BaseEntity):
    name: str = None
    nif: int = 0
    username: str = None
    password: str = None
    email: str = None
    role: Role = None

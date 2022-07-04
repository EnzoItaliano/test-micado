from pydantic import validator
from app.core.common.base_entity import BaseEntity
from app.core.constants.enums.role_enum import Role
from app.core.helpers.hash_utils import get_password_hash, is_hash


class CustomersEntity(BaseEntity):
    name: str = None
    nif: int = 0
    username: str = None
    password: str = None
    email: str = None
    role: Role = None

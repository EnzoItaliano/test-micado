from app.core.common.base_entity import BaseEntity


class CustomersEntity(BaseEntity):
    name: str = None
    nif: int = 0
    username: str = None
    password: str = None
    email: str = None
    role: str = None

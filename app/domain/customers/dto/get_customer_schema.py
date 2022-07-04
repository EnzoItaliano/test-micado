from app.core.common.base_entity import BaseGetEntity


class GetCustomersDto(BaseGetEntity):
    name: str
    nif: int
    username: str
    email: str

from app.domain.customers.dto.get_customer_schema import GetCustomersDto


class Token(GetCustomersDto):
    access_token: str
    token_type: str

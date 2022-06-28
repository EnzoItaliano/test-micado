from fastapi import APIRouter, Request, Body, status
from fastapi.encoders import jsonable_encoder
from app.core.constants.enums.role_enum import Role

from app.core.helpers.hash_utils import get_password_hash
from app.domain.customers.dto.create_customer_schema import CreateCustomersDto
from app.domain.customers.dto.get_customer_schema import GetCustomersDto

router = APIRouter()


@router.post(
    "/add",
    response_description="Add new client",
    response_model=GetCustomersDto,
    status_code=status.HTTP_201_CREATED,
)
async def create_client(request: Request, body: CreateCustomersDto = Body(...)):
    body = jsonable_encoder(body)
    body["password"] = get_password_hash(body["password"])
    body["role"] = Role.CLIENT.value
    new_client = await request.app.mongodb["Customers"].insert_one(body)
    created_client = await request.app.mongodb["Customers"].find_one(
        {"_id": new_client.inserted_id}
    )
    return created_client

from bson import ObjectId
from fastapi import APIRouter, HTTPException, Request, Body, status
from fastapi.encoders import jsonable_encoder
from pymongo import ReturnDocument
from app.core.constants.enums.role_enum import Role

from app.core.helpers.hash_utils import get_password_hash
from app.domain.customers.dto.create_customer_schema import CreateCustomersDto
from app.domain.customers.dto.get_customer_schema import GetCustomersDto
from app.domain.customers.dto.update_customer_schema import UpdateCustomersDto

router = APIRouter()


@router.post(
    "/add",
    response_description="Add new client",
    response_model=GetCustomersDto,
    status_code=status.HTTP_201_CREATED,
)
async def create_client(request: Request, content: CreateCustomersDto = Body(...)):
    content = jsonable_encoder(content)
    content["password"] = get_password_hash(content["password"])
    content["role"] = Role.CLIENT.value
    try:
        new_client = await request.app.mongodb["Customers"].insert_one(content)
        created_client = await request.app.mongodb["Customers"].find_one(
            {"_id": new_client.inserted_id}
        )
        return created_client
    except Exception:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, "The customer couldn't be created"
        )


@router.put(
    "/update/{id}",
    response_description="Update a client",
    response_model=GetCustomersDto,
)
async def update_client(
    id: str, request: Request, customer: UpdateCustomersDto = Body(...)
):
    if customer.password:
        customer.password = get_password_hash(customer.password)
    try:
        updated_customer = await request.app.mongodb["Customers"].find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": customer.dict(skip_defaults=True)},
            projection={"password": False},
            return_document=ReturnDocument.AFTER,
        )
        return updated_customer
    except Exception:
        raise HTTPException(status_code=404, detail=f"Customer {id} not found")

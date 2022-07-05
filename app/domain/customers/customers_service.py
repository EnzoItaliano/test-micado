from datetime import datetime, timezone
from bson import ObjectId
from fastapi import HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from pymongo import ReturnDocument
from app.core.constants.enums.role_enum import Role
from pymongo.errors import DuplicateKeyError
from app.core.helpers.hash_utils import get_password_hash
from app.domain.customers.dto.create_customer_schema import CreateCustomersDto
from app.domain.customers.dto.update_customer_schema import UpdateCustomersDto
from app.domain.customers.entities.customers_entity import CustomersEntity


class CustomersService:
    async def create(request: Request, content: CreateCustomersDto):
        content = jsonable_encoder(content)
        content["password"] = get_password_hash(content["password"])
        content["role"] = Role.CLIENT.value
        content = CustomersEntity(**content)
        content = jsonable_encoder(content)
        try:
            new_client = await request.app.mongodb["Customers"].insert_one(content)
            created_client = await request.app.mongodb["Customers"].find_one(
                {"_id": new_client.inserted_id}
            )
            return created_client
        except DuplicateKeyError:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, "Username already in use")
        except Exception:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST, "The customer couldn't be created"
            )

    async def update(request: Request, id: str, customer: UpdateCustomersDto):
        content = customer.dict(skip_defaults=True)
        content["updated_at"] = datetime.now(tz=timezone.utc).isoformat()
        try:
            updated_customer = await request.app.mongodb[
                "Customers"
            ].find_one_and_update(
                {"_id": ObjectId(id)},
                {"$set": content},
                projection={"password": False},
                return_document=ReturnDocument.AFTER,
            )
            return updated_customer
        except Exception:
            raise HTTPException(status_code=404, detail=f"Customer {id} not found")

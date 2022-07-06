from bson import ObjectId
from fastapi import HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from app.domain.contents.dtos.create_content_schema import CreateContentDto

from app.domain.contents.entities.contents_entity import ContentEntity


class ContentsService:
    async def get_one(request: Request, id: str):
        return await request.app.mongodb["Contents"].find_one({"_id": ObjectId(id)})

    async def create(request: Request, content: CreateContentDto):
        content = jsonable_encoder(content)
        content = ContentEntity(**content)
        content = jsonable_encoder(content)
        content["customer"] = ObjectId(content["customer"])
        try:
            new_content = await request.app.mongodb["Contents"].insert_one(content)
            created_content = await request.app.mongodb["Contents"].find_one(
                {"_id": new_content.inserted_id}
            )
            return created_content
        except Exception:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST, "The content couldn't be created"
            )

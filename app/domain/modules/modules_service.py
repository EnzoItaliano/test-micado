import re
from fastapi import HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from app.core.common.pagination_response_schema import create_pagination_response_dto
from app.core.decorators.pagination_decorator import GetPagination

from app.domain.modules.dto.create_module_schema import CreateModuleDto
from app.domain.modules.dto.get_module_schema import GetModulesDto


class ModulesService:
    async def create(request: Request, content: CreateModuleDto):
        content = jsonable_encoder(content)
        try:
            new_module = await request.app.mongodb["Modules"].insert_one(content)
            created_module = await request.app.mongodb["Modules"].find_one(
                {"_id": new_module.inserted_id}
            )
            return created_module
        except Exception:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST, "The module couldn't be created"
            )

    async def get_all(request: Request, pagination_info: GetPagination):
        for key in ["name"]:
            pagination_info.search[key] = {"$regex": pagination_info.search[key]}
        modules = request.app.mongodb["Modules"].find(pagination_info.search)
        modules.skip(pagination_info.skip).limit(pagination_info.limit)
        response = [GetModulesDto(**x) for x in await modules.to_list(None)]
        total = await request.app.mongodb["Modules"].count_documents({})
        return create_pagination_response_dto(
            response, total, pagination_info.skip, pagination_info.limit
        )

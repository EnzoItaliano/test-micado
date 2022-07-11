import re
from fastapi import HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from app.core.common.pagination_response_schema import create_pagination_response_dto
from app.core.decorators.pagination_decorator import GetPagination
from app.domain.modules.dto.budget_schema import BudgetRequest

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
            pagination_info.search[key] = {
                "$regex": pagination_info.search[key],
                "$options": "i",
            }
        modules = request.app.mongodb["Modules"].find(pagination_info.search)
        modules.skip(pagination_info.skip).limit(pagination_info.limit)
        response = [GetModulesDto(**x) for x in await modules.to_list(None)]
        total = await request.app.mongodb["Modules"].count_documents({})
        return create_pagination_response_dto(
            response, total, pagination_info.skip, pagination_info.limit
        )

    async def get_budget(request: Request, content: BudgetRequest):
        response = []
        for module_dict in content.modules:
            module_info = await request.app.mongodb["Modules"].find_one(
                {"name": module_dict.name}
            )
            response.append(
                {
                    "module": module_info["name"],
                    "units": module_dict.units,
                    "unit_price": module_info["price"],
                    "total_price": module_info["price"] * module_dict.units,
                    "components": module_info["components"],
                }
            )
        return response

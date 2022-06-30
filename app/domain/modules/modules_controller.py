from typing import Dict, Optional
from fastapi import APIRouter, HTTPException, Request, Body, status
from fastapi.encoders import jsonable_encoder
from app.core.common.pagination_response_schema import (
    PaginationResponseDto,
    create_pagination_response_dto,
)

from app.domain.modules.dto.create_module_schema import CreateModuleDto
from app.domain.modules.dto.get_module_schema import GetModulesDto

router = APIRouter()


@router.get("/")
async def index() -> Dict[str, str]:
    return {
        "info": "This is the index page of Micado modules. "
        "You probably want to go to 'http://<hostname:port>/docs'.",
    }


@router.post(
    "/add",
    response_description="Add new module",
    response_model=GetModulesDto,
    status_code=status.HTTP_201_CREATED,
)
async def create_module(request: Request, content: CreateModuleDto = Body(...)):
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


@router.get("/get", response_model=PaginationResponseDto[GetModulesDto])
async def get_modules(request: Request, skip: int = 1, limit: int = 10):
    modules = request.app.mongodb["Modules"].find()
    modules.skip((skip - 1) * limit).limit(limit)
    response = [GetModulesDto(**x) for x in await modules.to_list(None)]
    total = await request.app.mongodb["Modules"].count_documents({})
    return create_pagination_response_dto(response, total, skip, limit)

from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query, Request, Body, status
from app.core.common.pagination_response_schema import PaginationResponseDto
from app.core.constants.enums.role_enum import Role
from app.core.decorators.pagination_decorator import pagination_info
from app.domain.customers.dto.get_customer_schema import GetCustomersDto

from app.domain.modules.dto.create_module_schema import CreateModuleDto
from app.domain.modules.dto.get_module_schema import GetModulesDto
from app.domain.modules.modules_service import ModulesService
from app.infrastrucutre.auth.auth_service import get_current_active_user

router = APIRouter()


@router.post(
    "/add",
    response_description="Add new module",
    response_model=GetModulesDto,
    status_code=status.HTTP_201_CREATED,
)
async def create_module(
    request: Request,
    content: CreateModuleDto = Body(...),
    current_user: GetCustomersDto = Depends(get_current_active_user),
):
    if current_user.role != Role.ADMIN:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Forbidden.")
    return await ModulesService.create(request, content)


@router.get("/get", response_model=PaginationResponseDto[GetModulesDto])
async def get_modules(
    request: Request,
    pagination_info=Depends(pagination_info),
    current_user: GetCustomersDto = Depends(get_current_active_user),
):
    return await ModulesService.get_all(request, pagination_info)

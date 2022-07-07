from fastapi import APIRouter, Body, Depends, Request
from app.core.common.pagination_response_schema import PaginationResponseDto
from app.core.decorators.pagination_decorator import pagination_info
from app.domain.contents.contents_service import ContentsService
from app.domain.contents.dtos.create_content_schema import CreateContentDto
from app.domain.contents.dtos.get_content_schema import GetContentDto
from app.domain.customers.dto.get_customer_schema import GetCustomersDto
from app.infrastrucutre.auth.auth_service import get_current_active_user

router = APIRouter()

content_service = ContentsService()


@router.get("/get", response_model=PaginationResponseDto[GetContentDto])
async def get_all(request: Request, pagination_info=Depends(pagination_info)):
    return await content_service.get_all(request, pagination_info)


@router.get("/get/{id}", response_model=GetContentDto)
async def get_one(request: Request, id: str):
    return await content_service.get_one(request, id)


@router.post("/add", response_model=GetContentDto)
async def create(request: Request, content: CreateContentDto = Body(...)):
    return await content_service.create(request=request, content=content)

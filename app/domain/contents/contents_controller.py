from fastapi import APIRouter, Body, Depends, Request
from app.domain.contents.contents_service import ContentsService
from app.domain.contents.dtos.create_content_schema import CreateContentDto
from app.domain.contents.dtos.get_content_schema import GetContentDto
from app.domain.customers.dto.get_customer_schema import GetCustomersDto
from app.infrastrucutre.auth.auth_service import get_current_active_user

router = APIRouter()


@router.get("/get/{id}", response_model=GetContentDto)
async def get_content(request: Request, id: str):
    return await ContentsService.get_one(request, id)


@router.post("/add", response_model=GetContentDto)
async def create_content(request: Request, content: CreateContentDto = Body(...)):
    return await ContentsService.create(request, content)

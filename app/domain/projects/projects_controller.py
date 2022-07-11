from fastapi import APIRouter, Body, Depends, Request, status
from fastapi.responses import JSONResponse
from app.domain.projects.dto.create_project_schema import CreateProjectDto
from app.domain.projects.dto.get_project_schema import GetProjectDto
from app.core.common.pagination_response_schema import PaginationResponseDto
from app.domain.projects.projects_service import ProjectsService
from app.core.decorators.pagination_decorator import pagination_info

router = APIRouter()

projects_service = ProjectsService()


@router.get(
    "/get/user/{id}",
    response_description="Get Projects Info by user",
    response_model=PaginationResponseDto[GetProjectDto],
)
async def get_by_user(
    id: str, request: Request, pagination_info=Depends(pagination_info)
):
    return await projects_service.get_by_user(request, id, pagination_info)


@router.post(
    "/add", response_description="Add new project", response_model=GetProjectDto
)
async def create_project(request: Request, content: CreateProjectDto = Body(...)):
    return await projects_service.create(request, content)

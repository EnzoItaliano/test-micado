from bson import ObjectId
from fastapi import HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from app.core.common.pagination_response_schema import create_pagination_response_dto
from app.core.decorators.pagination_decorator import GetPagination
from app.domain.projects.dto.create_project_schema import CreateProjectDto
from app.domain.projects.dto.get_project_schema import GetProjectDto
from app.domain.projects.entities.projects_entity import ProjectsEntity


class ProjectsService:
    async def create(self, request: Request, content: CreateProjectDto):
        content = jsonable_encoder(content)
        content = ProjectsEntity(**content)
        try:
            new_project = await request.app.mongodb["Projects"].insert_one(
                content.dict()
            )
            created_project = await request.app.mongodb["Projects"].find_one(
                {"_id": new_project.inserted_id}
            )
            return created_project
        except Exception:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST, "The project couldn't be created"
            )

    async def get_by_user(
        self, request: Request, id: str, pagination_info: GetPagination
    ):
        if pagination_info.search:
            for key in ["status"]:
                pagination_info.search[key] = {
                    "$regex": pagination_info.search[key],
                    "$options": "i",
                }
            pagination_info.search.update({"owner": ObjectId(id)})
            projects = request.app.mongodb["Projects"].find(pagination_info.search)
        else:
            projects = request.app.mongodb["Projects"].find({"owner": ObjectId(id)})
        projects.skip(pagination_info.skip).limit(pagination_info.limit)
        response = [GetProjectDto(**x) for x in await projects.to_list(None)]
        total = await request.app.mongodb["Projects"].count_documents(
            {"owner": ObjectId(id)}
        )
        return create_pagination_response_dto(
            response, total, pagination_info.skip, pagination_info.limit
        )

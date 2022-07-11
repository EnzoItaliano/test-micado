from datetime import datetime, timezone
from bson import ObjectId
from fastapi import HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from pymongo import ReturnDocument
from app.core.common.pagination_response_schema import create_pagination_response_dto
from app.core.decorators.pagination_decorator import GetPagination, pagination_info
from app.domain.contents.dto.create_content_schema import CreateContentDto
from app.domain.contents.dto.get_content_schema import GetContentDto
from app.domain.contents.dto.update_content_schema import UpdateContentDto
from app.domain.contents.entities.contents_entity import ContentEntity


class ContentsService:
    def __init__(self) -> None:
        pass

    def convert_model_to_get(self, content):
        for layer in content["layers"]:
            layer["vertices"] = {
                vertice["id"]: vertice for vertice in layer["vertices"]
            }
            for line in layer["lines"]:
                line["proj_mod"] = {x["id"]: x["value"] for x in line["proj_mod"]}
            layer["lines"] = {line["id"]: line for line in layer["lines"]}
            layer["areas"] = {area["id"]: area for area in layer["areas"]}
            layer["holes"] = {hole["id"]: hole for hole in layer["holes"]}
            layer["items"] = {item["id"]: item for item in layer["items"]}
        content["layers"] = {layer["id"]: layer for layer in content["layers"]}
        for group in content["groups"]:
            group["elements"] = {x["layer"]: x for x in group["elements"]}
        content["groups"] = {group["id"]: group for group in content["groups"]}
        content["guides"]["horizontal"] = {
            x["id"]: x["value"] for x in content["guides"]["horizontal"]
        }
        content["guides"]["vertical"] = {
            x["id"]: x["value"] for x in content["guides"]["vertical"]
        }
        content["guides"]["circular"] = {
            x["id"]: x["value"] for x in content["guides"]["circular"]
        }
        return GetContentDto(**content)

    async def get_all(self, request: Request, pagination_info: GetPagination):
        if pagination_info.search:
            for key in ["name"]:
                pagination_info.search[key] = {
                    "$regex": pagination_info.search[key],
                    "$options": "i",
                }
        modules = request.app.mongodb["Contents"].find(pagination_info.search)
        modules.skip(pagination_info.skip).limit(pagination_info.limit)
        response = [self.convert_model_to_get(x) for x in await modules.to_list(None)]
        total = await request.app.mongodb["Contents"].count_documents({})
        return create_pagination_response_dto(
            response, total, pagination_info.skip, pagination_info.limit
        )

    async def get_one(self, request: Request, id: str):
        response = await request.app.mongodb["Contents"].find_one({"_id": ObjectId(id)})
        return self.convert_model_to_get(response)

    async def get_all_from_user(
        self, request: Request, id: str, pagination_info: GetPagination
    ):
        if pagination_info.search:
            for key in ["name"]:
                pagination_info.search[key] = {
                    "$regex": pagination_info.search[key],
                    "$options": "i",
                }
            pagination_info.search.update({"customer": ObjectId(id)})
            contents = request.app.mongodb["Contents"].find(pagination_info.search)
        else:
            contents = request.app.mongodb["Contents"].find({"customer": ObjectId(id)})
        contents.skip(pagination_info.skip).limit(pagination_info.limit)
        response = [self.convert_model_to_get(x) for x in await contents.to_list(None)]
        total = await request.app.mongodb["Contents"].count_documents(
            {"customer": ObjectId(id)}
        )
        return create_pagination_response_dto(
            response, total, pagination_info.skip, pagination_info.limit
        )

    def convert_create_to_model(self, content, create):
        content.layers = list(content.layers.values())
        for layer in content.layers:
            layer.vertices = list(layer.vertices.values())
            layer.lines = list(layer.lines.values())
            for line in layer.lines:
                line.proj_mod = [
                    {"id": x, "value": line.proj_mod[x]} for x in line.proj_mod.keys()
                ]
            layer.areas = list(layer.areas.values())
            layer.holes = list(layer.holes.values())
            layer.items = list(layer.items.values())
        content.groups = list(content.groups.values())
        elements_list = []
        for group in content.groups:
            for element in group.elements.items():
                element_1 = jsonable_encoder(element[1])
                elements_list.append({x: element_1[x] for x in element_1.keys()})
                elements_list[-1].update({"layer": element[0]})
            group.elements = elements_list
        content.guides.horizontal = [
            {"id": x, "value": content.guides.horizontal[x]}
            for x in content.guides.horizontal.keys()
        ]
        content.guides.vertical = {
            {"id": x, "value": content.guides.vertical[x]}
            for x in content.guides.vertical.keys()
        }
        content.guides.circular = {
            {"id": x, "value": content.guides.circular[x]}
            for x in content.guides.circular.keys()
        }
        if create:
            content = jsonable_encoder(content)
            content = ContentEntity(**content)
            content = jsonable_encoder(content)
            content["customer"] = ObjectId(content["customer"])
        return content

    async def create(self, request: Request, content: CreateContentDto):
        content = self.convert_create_to_model(content, True)
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

    async def update(self, request: Request, id: str, content: UpdateContentDto):
        content = self.convert_create_to_model(content, False)
        content = jsonable_encoder(content)
        content["updated_at"] = datetime.now(tz=timezone.utc).isoformat()
        try:
            updated_content = await request.app.mongodb["Contents"].find_one_and_update(
                {"_id": ObjectId(id)},
                {"$set": content},
                return_document=ReturnDocument.AFTER,
            )
            return updated_content
        except Exception:
            raise HTTPException(status_code=404, detail=f"Content {id} not found")

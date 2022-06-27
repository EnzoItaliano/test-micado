from fastapi import APIRouter, Request, Body, status
from fastapi.responses import JSONResponse

from app.core.helpers.get_entities import get_entities

router = APIRouter()


@router.get("/")
async def index() -> dict[str, str]:
    return {
        "info": "This is the index page of Micado modules. "
        "You probably want to go to 'http://<hostname:port>/docs'.",
    }


@router.post("/add", response_description="Add new module")
async def create_module(request: Request, content=Body(...)):
    new_doc = dict(
        [
            ("name", content["name"]),
            ("price", content["price"]),
            ("components", content["components"]),
        ]
    )

    content = new_doc
    new_content = await request.app.mongodb["Modules"].insert_one(content)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED, content=str(new_content.inserted_id)
    )


@router.get("/get")
async def get_modules(request: Request, skip: int = 1, limit: int = 10):
    modules = request.app.mongodb["Modules"].find()
    modules.skip(skip - 1).limit(limit)
    response = await get_entities(modules)
    return response

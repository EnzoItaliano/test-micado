from pydantic import BaseModel


class CreateProjectDto(BaseModel):
    contents: str
    status: str
    forecast: str
    reviewer: str
    owner: str

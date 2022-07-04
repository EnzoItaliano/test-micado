from datetime import datetime, timezone
from pydantic import BaseModel, Field
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class BaseEntity(BaseModel):
    created_at: datetime = Field(default=datetime.now(tz=timezone.utc))
    updated_at: datetime = Field(default=datetime.now(tz=timezone.utc))
    deleted_at: datetime | None = Field(default=None)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class BaseGetEntity(BaseModel):
    id: PyObjectId = Field(alias="_id")
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

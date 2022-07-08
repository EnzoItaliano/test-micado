from typing import Dict, List
from fastapi import Query
from pydantic import BaseModel


class GetPagination(BaseModel):
    skip: int
    limit: int
    search: Dict | None


def pagination_info(
    skip: int = 1, limit: int = 10, search: List | None = Query(None)
) -> GetPagination:
    if search:
        search = [search_item.split(":") for search_item in search]
        search = {search_item[0]: search_item[1] for search_item in search}
    return GetPagination(skip=(skip - 1) * limit, limit=limit, search=search)

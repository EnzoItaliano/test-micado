from fastapi import APIRouter

from app.modules import modules_controller
from app.customers import customers_controller

api_router = APIRouter()
api_router.include_router(
    modules_controller.router, prefix="/modules", tags=["modules"]
)
api_router.include_router(
    customers_controller.router, prefix="/customers", tags=["customers"]
)

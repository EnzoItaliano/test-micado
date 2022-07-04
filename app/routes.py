from fastapi import APIRouter

from app.domain.modules import modules_controller
from app.domain.customers import customers_controller
from app.infrastrucutre.auth import auth_controller

api_router = APIRouter()
api_router.include_router(
    modules_controller.router, prefix="/modules", tags=["modules"]
)
api_router.include_router(
    customers_controller.router, prefix="/customers", tags=["customers"]
)
api_router.include_router(auth_controller.router, prefix="/auth", tags=["auth"])

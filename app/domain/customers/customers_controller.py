from fastapi import APIRouter, Depends, HTTPException, Request, Body, status
from app.domain.customers.customers_service import CustomersService
from app.domain.customers.dto.create_customer_schema import CreateCustomersDto
from app.domain.customers.dto.get_customer_schema import GetCustomersDto
from app.domain.customers.dto.update_customer_schema import UpdateCustomersDto
from app.infrastrucutre.auth.auth_service import get_current_active_user

router = APIRouter()


@router.post(
    "/add",
    response_description="Add new client",
    response_model=GetCustomersDto,
    status_code=status.HTTP_201_CREATED,
)
async def create_client(request: Request, content: CreateCustomersDto = Body(...)):
    return await CustomersService.create(request, content)


@router.put(
    "/update/{id}",
    response_description="Update a client",
    response_model=GetCustomersDto,
)
async def update_client(
    id: str,
    request: Request,
    customer: UpdateCustomersDto = Body(...),
    current_user: GetCustomersDto = Depends(get_current_active_user),
):
    if id != current_user.id.__str__():
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY, "Id different from token"
        )
    return await CustomersService.update(request, id, customer)

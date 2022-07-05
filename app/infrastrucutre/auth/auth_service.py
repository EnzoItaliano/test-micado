from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, Request, status
from app.core.helpers.hash_utils import verify_password
from fastapi.security import OAuth2PasswordBearer
from app.domain.customers.dto.get_customer_schema import (
    GetCustomerFullDto,
    GetCustomersDto,
)
from app.core.constants.configs import SECRET_KEY, ALGORITHM
from app.domain.customers.entities.customers_entity import CustomersEntity

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")


async def get_user(db, username: str):
    user = await db.find_one({"username": username})
    if user:
        return GetCustomerFullDto(**user)


async def authenticate_user(request, username: str, password: str):
    user = await get_user(request.app.mongodb["Customers"], username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(request: Request, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = CustomersEntity(username=username)
    except JWTError:
        raise credentials_exception
    user = await get_user(
        request.app.mongodb["Customers"], username=token_data.username
    )
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: GetCustomersDto = Depends(get_current_user),
):
    if current_user.deleted_at:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

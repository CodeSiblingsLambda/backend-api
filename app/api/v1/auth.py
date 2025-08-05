from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse

from app.schemas.auth import CustomerLogin, CustomerResponse, CustomerSignUp
from app.services.auth import login_user, signup_client
from app.database.get_db import get_db
from app.utils.logger import create_logger

logger = create_logger(__name__)
router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=CustomerResponse, status_code=status.HTTP_200_OK)
async def login(
    data: CustomerLogin, db: AsyncSession = Depends(get_db)
) -> CustomerResponse:
    """
    Authenticate a customer and return their profile (excluding password).
    """
    logger.info(f"Calling login_user with the following data: {data}")
    return await login_user(data, db)


@router.post("/signup/client", status_code=status.HTTP_201_CREATED)
async def signup_client_endpoint(data: CustomerSignUp) -> JSONResponse:
    """
    Register a new customer. Returns success message if created.
    """
    logger.info(f"Calling signup_client with the following data: {data}")
    await signup_client(data)
    return JSONResponse(
        status_code=201, content={"message": "Customer created successfully"}
    )

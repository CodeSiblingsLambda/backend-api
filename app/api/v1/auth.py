from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.responses import JSONResponse
from app.schemas.auth import CustomerLogin, CustomerResponse, CustomerSignUp
from app.services.auth import login_user, signup_client

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=CustomerResponse, status_code=status.HTTP_200_OK)
def login(data: CustomerLogin) -> CustomerResponse:
    """
    Authenticate a customer and return their profile (excluding password).
    """
    return login_user(data)


@router.post("/signup/client", status_code=status.HTTP_201_CREATED)
def signup_client_endpoint(data: CustomerSignUp) -> JSONResponse:
    """
    Register a new customer. Returns success message if created.
    """
    signup_client(data)
    return JSONResponse(
        status_code=201, content={"message": "Customer created successfully"}
    )

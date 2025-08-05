from fastapi import APIRouter, HTTPException, Depends
from app.schemas.auth import LoginRequest, SignupClientRequest, SignupBusinessRequest
from app.services.auth import login_user, signup_client, signup_business

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(data: LoginRequest):
    return login_user(data)

@router.post("/signup/client")
def signup_client_endpoint(data: SignupClientRequest):
    return signup_client(data)

@router.post("/signup/business")
def signup_business_endpoint(data: SignupBusinessRequest):
    return signup_business(data)
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from uuid import UUID


class CustomerSignUp(BaseModel):
    email: EmailStr
    full_name: str = Field(..., max_length=100)
    password: str = Field(..., min_length=8)


class CustomerLogin(BaseModel):
    email: EmailStr
    password: str


class CustomerResponse(BaseModel):
    email: EmailStr
    full_name: str
    qr_code: UUID

    class Config:
        orm_mode = True

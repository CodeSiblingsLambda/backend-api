from fastapi import HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
import bcrypt

from app.schemas.auth import CustomerLogin, CustomerSignUp, CustomerResponse
from app.models import Customer
from app.database import get_db
from app.utils.logger import create_logger

logger = create_logger(__name__)


async def signup_client(
    data: CustomerSignUp, db: AsyncSession = Depends(get_db)
) -> None:
    hashed_password = bcrypt.hashpw(
        data.password.encode("utf-8"), bcrypt.gensalt()
    ).decode("utf-8")

    new_customer = Customer(
        email=data.email, full_name=data.full_name, password_hash=hashed_password
    )

    db.add(new_customer)
    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Customer with this email already exists.",
        )


async def login_user(
    data: CustomerLogin, db: AsyncSession = Depends(get_db)
) -> CustomerResponse:
    query = select(Customer).where(Customer.email == data.email)
    result = await db.execute(query)
    customer = result.scalars().first()
    logger.info(f"Customer retrieved: ({customer.email}, {customer.full_name})")

    if not customer:
        logger.error(f"The customer introduced does not exist: {data}")

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password.",
        )

    # Compare password
    if not bcrypt.checkpw(
        data.password.encode("utf-8"), customer.password_hash.encode("utf-8")
    ):
        logger.error(f"The password introduced does not match: {data}")

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password.",
        )

    # Return customer data (excluding password)
    return CustomerResponse(
        email=customer.email, full_name=customer.full_name, qr_code=customer.qr_code
    )

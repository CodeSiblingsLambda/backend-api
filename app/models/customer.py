# app/models.py

from sqlalchemy import Column, String, Text
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"

    email = Column(String(100), primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    password_hash = Column(Text)
    qr_code = Column(
        String(255), unique=True, nullable=False, default=lambda: str(uuid.uuid4())
    )

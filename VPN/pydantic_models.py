from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class validate_user(BaseModel):
    # use either username/email
    email: str = Field(examples=["test@example.com"])
    password: str = Field(examples=["testpassword"])

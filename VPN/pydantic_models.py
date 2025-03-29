from typing import Optional
from pydantic import BaseModel, EmailStr, Field

"""
class select_server_type(BaseModel):
    server_type: Optional[str] = Field(default=None, examples=["public", "private"])
    # private: bool = Field(default=False, examples=[True, False])
"""

class ip_pydantic(BaseModel):
    ip_address: str = Field(examples=["127.0.0.1"])


"""
class validate_user(BaseModel):
    # use either username/email
    email: str = Field(examples=["test@example.com"])
    password: str = Field(examples=["testpassword"])
"""

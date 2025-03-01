from VPN import app
from fastapi import status, Depends, HTTPException, Form

"""
from VPN.models import (
)

from QUIET.helper import (
)

from QUIET.pydantic_models import (
)
"""

from database import SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated

# import jwt
import json
import time
import os
import re
import httpx
from httpx import Timeout
from random import randint
from passlib.hash import bcrypt_sha256


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
db_dependency = Annotated[Session, Depends(get_db)]


#  [ INDEX/MISC ]
@app.get("/", status_code=status.HTTP_200_OK)
def index():
    return {
        "statusCode": 200,
        "message": "nothing to see here!"
    }

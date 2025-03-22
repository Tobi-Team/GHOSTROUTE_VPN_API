from VPN import app
from fastapi import status, Depends, HTTPException, Form

# import jwt
import json
import os
import httpx
from httpx import Timeout
from random import randint


#  [ INDEX/MISC ]
@app.get("/", status_code=status.HTTP_200_OK)
def index():
    return {
        "statusCode": 200,
        "message": "nothing to see here!"
    }

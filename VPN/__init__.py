from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# List of allowed origins
origins = [
    "https://security.ghostroute.io",
    "http://localhost:5173",
]
"""
origins = ["*"]
"""

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


from VPN import models
from database import engine

# to not create any model/table that will affect the main model/table
# models.Base.metadata.create_all(bind=engine)


from VPN import (
    routes, pydantic_models,
    helper
)

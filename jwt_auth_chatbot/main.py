from fastapi import FastAPI
import uvicorn
from jwt_auth_chatbot.api import models
from jwt_auth_chatbot.api.db import engine
from jwt_auth_chatbot.api.routes import router
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv
import os

load_dotenv()

ALLOWED_DOMAIN = os.getenv("ALLOWED_DOMAIN")

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.middleware("http")
async def add_cors_headers(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = f"{ALLOWED_DOMAIN}, http://localhost:8000"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

origins = [
    ALLOWED_DOMAIN
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

def main():
    uvicorn.run(app, host="127.0.0.1", port=5555)   
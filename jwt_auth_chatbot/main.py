from fastapi import FastAPI
import uvicorn
from jwt_auth_chatbot.api import models
from jwt_auth_chatbot.api.db import engine
from jwt_auth_chatbot.api.routes import router

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(router)

def main():
    uvicorn.run(app, host="127.0.0.1", port=5555)   
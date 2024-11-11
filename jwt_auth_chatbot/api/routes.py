from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Annotated

from jwt_auth_chatbot.api import models, schemas, security, auth
from jwt_auth_chatbot.api.db import get_db

router = APIRouter()

@router.post("/register/", response_model=schemas.UserInDBBase)
async def register_user(user: schemas.UserIn, db: Session = Depends(get_db)):
    
    db_user = auth.get_user(db, user.username)
    
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = security.get_password_hash(user.password)
    db_user = models.User(
        **user.dict(exclude={"password"}),
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/token/", response_model=schemas.Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    user = auth.get_user(db, form_data.username)
    if not user or not security.pwd_context.verify(
        form_data.password, user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRES_MINUTES)

    access_token = security.create_access_token(
        data={"sub": user.username}, 
        expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/conversation/")
async def read_conversation(
    current_user: models.User = Depends(auth.get_current_user)
):
    return {
        "conversation": "This is a conversation",
        "username": current_user.username,
        }
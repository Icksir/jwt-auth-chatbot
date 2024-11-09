from sqlalchemy import Column, Integer, String
from sqlalchemy import Enum as SQLEnum

from jwt_auth_chatbot.api.db import Base
from jwt_auth_chatbot.api.schemas import UserLevel

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    age = Column(Integer)
    level = Column(SQLEnum(UserLevel))
    hashed_password = Column(String)
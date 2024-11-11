from datetime import datetime, timedelta, timezone
from typing import Optional

import jwt
from passlib.context import CryptContext

SECRET_KEY = "dfd265f4fa9bc64e66af54ebcfd20b12265ae423a1ca9c49f455827d0036f34e"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRES_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
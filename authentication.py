"""_summary_

- This module contains the authentication utilities for the application.
- jwt is used for generating and verifying JWT tokens.
- passlib is used for hashing and verifying passwords.
- google-auth is used for verifying Google Sign-In tokens.

    """

# Import additional modules
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException


from datetime import datetime, timedelta
from dotenv import load_dotenv

import os

load_dotenv()

# JWT settings
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEY = os.environ.get("SECRET_KEY")
if SECRET_KEY is None:
    raise ValueError("SECRET_KEY must be set")


# Security utilities
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function Create Access Token


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Fucntion to verify token


def verify_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise credentials_exception

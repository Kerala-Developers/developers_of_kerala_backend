from pydantic import BaseModel
from typing import List, Optional

class Developer(BaseModel):
    name: str
    place: str
    skills: list
    email: str
    resume: Optional[str] = None

class User(BaseModel):
    username: str
    email: str
    hashed_password: str

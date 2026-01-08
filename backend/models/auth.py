from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password_hash: str
    name: str

class UserRetreive(BaseModel):
    id: int
    email: str
    password_hash: str
    name: str
    created_at: datetime

class UserLogin(BaseModel):
    email: str
    password: str

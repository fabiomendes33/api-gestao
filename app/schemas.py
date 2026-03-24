from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool
    created_at: datetime
    class Config:
        from_attributes = True

class ItemCreate(BaseModel):
    title: str
    description: Optional[str] = None

class ItemOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    is_active: bool
    created_at: datetime
    owner_id: int
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

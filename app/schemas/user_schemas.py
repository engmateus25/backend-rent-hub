from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str  # A senha será recebida no cadastro

class UserUpdate(UserBase):
    pass

class UserResponse(UserBase):
    id: UUID
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

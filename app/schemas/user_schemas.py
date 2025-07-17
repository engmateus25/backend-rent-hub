from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class UserBase(BaseModel):
    name: str
    email: str


class UserRequest(UserBase):
    password: str | None = None  # A senha será opcional, pois é usada apenas no cadastro


class UserResponse(UserBase):
    id: UUID
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

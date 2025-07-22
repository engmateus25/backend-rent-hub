from typing import Protocol
from app.database.models.user_models import User


class UserRepositoryInterface(Protocol):
    async def create_user(self, name: str, email: str, password_hash: str) -> User:
        ...


    async def get_user_by_id(self, user_id: str) -> User:
        ...

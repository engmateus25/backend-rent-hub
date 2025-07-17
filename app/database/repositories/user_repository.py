from app.database.models.user_models import User
from tortoise.exceptions import DoesNotExist


class UserRepository:
    async def get_user_by_id(self, user_id: str):
        try:
            return await User.get(id=user_id)
        except DoesNotExist:
            return None

    async def create_user(self, name: str, email: str, password_hash: str):
        user = await User.create(name=name, email=email, password_hash=password_hash)
        return user

    async def update_user(self, user_id: str, name: str, email: str):
        user = await User.get(id=user_id)
        user.name = name
        user.email = email
        await user.save()
        return user

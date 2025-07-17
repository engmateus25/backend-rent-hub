from app.database.models.user_models import User
from app.schemas.user_schemas import UserCreate, UserUpdate
from tortoise.exceptions import DoesNotExist


class UserService:
    async def create_user(self, user_data: UserCreate):
        user = await User.create(**user_data.dict())
        return user


    async def update_user(self, user_id: str, user_data: UserUpdate):
        user = await User.get(id=user_id)
        user.name = user_data.name
        user.email = user_data.email
        await user.save()
        return user


    async def get_user(self, user_id: str):
        try:
            return await User.get(id=user_id)
        except DoesNotExist:
            return None

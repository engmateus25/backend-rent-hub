from app.database.models.user_models import User
from app.schemas.user_schemas import UserCreate, UserUpdate
from app.database.interfaces.user_repository_interface import UserRepositoryInterface
from tortoise.exceptions import DoesNotExist

class UserRepository(UserRepositoryInterface):
    async def create_user(self, user_data: UserCreate):
        user = await User.create(
            name=user_data.name,
            email=user_data.email,
            password_hash=user_data.password  # Lembre-se de criptografar a senha no Service
        )
        return user

    async def get_user_by_id(self, user_id: str):
        try:
            return await User.get(id=user_id)
        except DoesNotExist:
            return None

    async def update_user(self, user_id: str, user_data: UserUpdate):
        user = await User.get(id=user_id)
        user.name = user_data.name
        user.email = user_data.email
        await user.save()
        return user

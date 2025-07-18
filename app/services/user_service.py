from app.database.repositories.user_repository import UserRepository
from app.schemas.user_schemas import UserCreate, UserUpdate, UserResponse
from passlib.context import CryptContext
from app.core.config import settings
from datetime import datetime, timedelta
from jose import JWTError, jwt

# Inicializando o contexto para criptografia de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create_user(self, user_data: UserCreate):
        # Criptografando a senha
        hashed_password = pwd_context.hash(user_data.password)
        user_data.password = hashed_password
        user = await self.user_repository.create_user(user_data)
        return UserResponse.from_orm(user)

    async def authenticate_user(self, email: str, password: str):
        user = await self.user_repository.get_user_by_id(email)
        if user and pwd_context.verify(password, user.password_hash):
            return user
        return None

    async def get_user(self, user_id: str):
        return await self.user_repository.get_user_by_id(user_id)

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt

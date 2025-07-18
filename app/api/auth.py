from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from app.schemas.user_schemas import UserCreate, UserResponse
from app.services.user_service import UserService
from app.core.config import settings
from datetime import timedelta
from app.database.repositories.user_repository import UserRepository


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

router = APIRouter()

user_service = UserService(user_repository=UserRepository())  # Injeção de dependência

# Função para gerar o token JWT
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    return user_service.create_access_token(data, expires_delta)

# Rota de Registro
@router.post("/register", response_model=UserResponse)
async def register(user_data: UserCreate):
    return await user_service.create_user(user_data)

# Rota de Login (gera o JWT)
@router.post("/login")
async def login(user_data: UserCreate):
    user = await user_service.authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Rota para obter informações do usuário autenticado
@router.get("/me", response_model=UserResponse)
async def read_users_me(current_user: UserResponse = Depends(oauth2_scheme)):
    return current_user

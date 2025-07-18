from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Para lidar com CORS
from app.api import auth, users
from app.core.config import settings  # Para acessar configurações, como o segredo do JWT
from tortoise.contrib.fastapi import register_tortoise

# Criar a aplicação FastAPI
app = FastAPI()

# Configuração de CORS
origins = [
    "http://localhost",  # Adicionar o endereço do frontend (ex: React)
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Ou '*' para permitir todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos
    allow_headers=["*"],  # Permitir todos os headers
)

# Incluir as rotas da API
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])

# Configuração do banco de dados com Tortoise ORM
register_tortoise(
    app,
    db_url=settings.DATABASE_URL,  # A URL do banco de dados
    modules={"models": ["app.database.models"]},  # O caminho para os modelos
    generate_schemas=True,  # Gera as tabelas automaticamente
    add_exception_handlers=True,  # Adiciona os handlers de exceção do Tortoise
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Equipment Rent API!"}

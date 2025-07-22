import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Configuração do banco de dados
    DATABASE_URL: str = "postgres://rentdb:rentdb@localhost:5441/rent"
    
    # Configuração do JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "mysecretkey") 
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30 

    class Config:
        env_file = ".env"  

settings = Settings()  



"""
TORTOISE_ORM = {
    "connections": {
        "default": "postgres://rentdb:rentdb@localhost:5441/rent", 
    },
    "apps": {
        "models": {
            "models": ["app.database.models", "aerich.models"],  
            "default_connection": "default",
        },
    },
}
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from app.api import auth, users
from app.core.config import settings  
from tortoise.contrib.fastapi import register_tortoise


app = FastAPI()


origins = [
    "http://localhost",  
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])


register_tortoise(
    app,
    db_url=settings.DATABASE_URL,  
    modules={"models": ["app.database.models"]},  
    generate_schemas=True,  
    add_exception_handlers=True,  
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Equipment Rent API!"}

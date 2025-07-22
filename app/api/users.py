from fastapi import APIRouter, HTTPException
from app.schemas.user_schemas import UserResponse, UserUpdate
from app.services.user_service import UserService
from app.database.repositories.user_repository import UserRepository

router = APIRouter()

user_service = UserService(user_repository=UserRepository())  


@router.get("/users", response_model=list[UserResponse])
async def get_users():
    users = await User.all()  
    return users


@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    user = await user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.patch("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: str, user_data: UserUpdate):
    user = await user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    updated_user = await user_service.update_user(user_id, user_data)
    return updated_user


@router.delete("/users/{user_id}")
async def delete_user(user_id: str):
    user = await user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await user.delete()
    return {"detail": "User deleted"}

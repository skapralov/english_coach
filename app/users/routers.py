from fastapi import APIRouter

from app.users.models import (
    User,
    User_Pydantic,
    UserIn_Pydantic,
    RefreshToken_Pydantic,
)

tags = ["users"]
users_router = APIRouter()


@users_router.get('/user')
async def get_user():
    return {'user': 1}


@users_router.post('/user/registration', response_model=User_Pydantic)
async def registration(user: UserIn_Pydantic):
    user_obj = await User.create(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)


@users_router.post('/user/login')
async def login():
    return {'user': 1}


@users_router.post('/user/obtain')
async def obtain():
    return {'user': 1}

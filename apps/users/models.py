from fastapi_users import models
from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import TortoiseBaseUserModel, TortoiseUserDatabase

from apps import settings


class User(models.BaseUser):
    pass


class UserCreate(models.BaseUserCreate):
    pass


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass


class UserModel(TortoiseBaseUserModel):
    pass


user_db = TortoiseUserDatabase(UserDB, UserModel)
jwt_authentication = JWTAuthentication(
    secret=settings.SECRET,
    lifetime_seconds=settings.JWT_ACCESS_LIFETIME.seconds,
)

auth_backends = [
    jwt_authentication,
]
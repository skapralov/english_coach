from pydantic import validator
from fastapi_users import models
from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import TortoiseBaseUserModel, TortoiseUserDatabase

import settings


class User(models.BaseUser):
    pass


class UserCreate(models.BaseUserCreate):
    @validator('password')
    def valid_password(cls, value: str):
        value = value.strip()

        if len(value) < 6:
            raise ValueError('Length should be at least 6 characters')

        # if len(value) > 20:
        #     raise ValueError('Length should be not be greater than 20')
        #
        # if not any(char.isdigit() for char in value):
        #     raise ValueError('Password should have at least one numeral')
        #
        # if not any(char.isupper() for char in value):
        #     raise ValueError('Password should have at least one uppercase letter')
        #
        # if not any(char.islower() for char in value):
        #     raise ValueError('Password should have at least one lowercase letter')

        return value


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

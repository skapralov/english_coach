from fastapi import APIRouter
from fastapi import Depends, Request, Response
from fastapi_users import FastAPIUsers

from settings import SECRET
from users.models import user_db, auth_backends, User, UserCreate, UserUpdate, UserDB, jwt_authentication


class ErrorCode:
    REGISTER_USER_ALREADY_EXISTS = "sdfgdsgfsd"
    LOGIN_BAD_CREDENTIALS = "sdfgdgsd"
    RESET_PASSWORD_BAD_TOKEN = "sdfgsdgds"


def on_after_register(user: UserDB, request: Request):
    print(f"User {user.id} has registered.")


def on_after_forgot_password(user: UserDB, token: str, request: Request):
    print(f"User {user.id} has forgot their password. Reset token: {token}")


fastapi_users = FastAPIUsers(
    user_db,
    auth_backends,
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)

users_router = APIRouter()

users_router.include_router(fastapi_users.get_auth_router(jwt_authentication), prefix='/users/jwt', tags=['users'])
users_router.include_router(fastapi_users.get_register_router(on_after_register), prefix='/users', tags=['users'])
users_router.include_router(fastapi_users.get_users_router(), prefix='/users', tags=['users'])
users_router.include_router(
    fastapi_users.get_reset_password_router(SECRET, after_forgot_password=on_after_forgot_password),
    prefix='/users',
    tags=['users'],
)


@users_router.post("/auth/jwt/refresh")
async def refresh_jwt(response: Response, user=Depends(fastapi_users.get_current_active_user)):
    return await jwt_authentication.get_login_response(user, response)

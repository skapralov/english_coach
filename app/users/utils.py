from datetime import datetime
from time import time

from jose import jwt

from app.users.models import RefreshToken_Pydantic, RefreshToken, User
from app import settings


def generate_access_token(user_id: int) -> str:
    expires_in = int(time() + datetime.timestamp(settings.JWT_ACCESS_LIFETIME))
    payload = {'id': user_id, 'expires_in': expires_in}
    return jwt.encode(payload, settings.SECRET_KEY, settings.JWT_ALGORITHM)


async def generate_refresh_token(user_id: int) -> RefreshToken_Pydantic:
    refresh = await RefreshToken.create(
        user_id=user_id,
        expires_in=int(time()),
    )
    return RefreshToken_Pydantic.from_tortoise_orm(refresh)


async def generate_tokens(user_id: int) -> dict:
    access = generate_access_token(user_id)
    refresh = await generate_refresh_token(user_id)
    return {'access': access, 'refresh': refresh}


async def get_password_hash_for_user(user_id: int) -> str:
    password_hash = await User.get(id=user_id).values('password_hash', )
    return password_hash[0]['password_hash']


async def authenticate(request):
    request.user = None

    if auth_header := request.headers.get('Authorization'):
        try:
            payload = jwt.decode(auth_header.decode('utf-8'), settings.SECRET_KEY, settings.JWT_ALGORITHM)
        except:
            raise Exception('Invalid authentication. Could not decode token.')

        if payload['expires_in'] < time():
            raise Exception('Invalid authentication.')

        try:
            user = await User.get(id=payload['id'])
        except:
            raise Exception('No user matching this token was found.')

        if not user.is_active:
            raise Exception('This user has been deactivated.')

        request.user = user

from fastapi import APIRouter

from apps.words.routers import words_router
from apps.users.routers import users_router

api_router = APIRouter()

api_router.include_router(words_router, prefix='/words', tags=['words'])
api_router.include_router(users_router, prefix='/users', tags=['users'])

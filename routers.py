from fastapi import APIRouter

from words.routers import words_router
from users.routers import users_router

api_router = APIRouter()

api_router.include_router(words_router, prefix='/words', tags=['words'])
api_router.include_router(users_router, prefix='/users', tags=['users'])

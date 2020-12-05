from fastapi import APIRouter

from app.words.routers import words_router

api_router = APIRouter()

api_router.include_router(words_router, prefix='/words', tags=['words'])

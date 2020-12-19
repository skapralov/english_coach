from typing import List

from fastapi import APIRouter

from words import schemas, service

words_router = APIRouter()


@words_router.get('/translator', response_model=List[schemas.TranslatorRusEngPydantic])
async def get_translator_rus_eng_list():
    return await service.translator_rus_eng_service.all()


@words_router.post('/study-words', response_model=List[schemas.StudyWordRusEngPydantic])
async def get_translator_rus_eng_list():
    return await service.study_word_rus_eng_service.update()

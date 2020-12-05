from typing import List

from fastapi import APIRouter

from app.words import schemas, models, service


words_router = APIRouter()


@words_router.get('/', response_model=List[schemas.GetTranslatorRusEngModel])
async def get_translator_rus_eng_list():
    return await service.transl_ru_en_service.all()

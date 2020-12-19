from words import schemas
from words import models
from core.service import BaseService


class TranslatorRusEngService(BaseService):
    model = models.TranslatorRusEngModel
    get_schema = schemas.TranslatorRusEngPydantic


translator_rus_eng_service = TranslatorRusEngService()


class StudyWordRusEngService(BaseService):
    model = models.StudyWordRusEngModel
    get_schema = schemas.StudyWordRusEngPydantic


study_word_rus_eng_service = StudyWordRusEngService()

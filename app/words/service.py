from app.words import schemas, models
from app.core.service import BaseService


class TranslatorRusEngService(BaseService):
    model = models.TranslatorRusEngModel
    get_schema = schemas.GetTranslatorRusEngModel


transl_ru_en_service = TranslatorRusEngService()

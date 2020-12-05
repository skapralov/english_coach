from pydantic.main import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator, PydanticModel

from app.words import models


CreateWordRusModel = pydantic_model_creator(models.WordRusModel, exclude_readonly=True)
GetWordRusModel = pydantic_model_creator(models.WordRusModel)

CreateWordEngModel = pydantic_model_creator(models.WordEngModel, exclude_readonly=True)
GetWordEngModel = pydantic_model_creator(models.WordEngModel)

GetTranslatorRusEngModel = pydantic_model_creator(models.TranslatorRusEngModel)

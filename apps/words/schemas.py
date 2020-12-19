from tortoise.contrib.pydantic import pydantic_model_creator

from apps.words import models


WordRusPydantic = pydantic_model_creator(models.WordRusModel)

WordEngPydantic = pydantic_model_creator(models.WordEngModel)

TranslatorRusEngPydantic = pydantic_model_creator(models.TranslatorRusEngModel)

StudyWordRusEngPydantic = pydantic_model_creator(models.StudyWordRusEngModel)

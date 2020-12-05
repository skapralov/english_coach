from abc import abstractmethod

from tortoise import fields, Tortoise

from app.core.models import BaseModel
from app.words.enums import PartSpeechEnum, TranslationFrequencyEnum


class WordBaseModel(BaseModel):
    title = fields.CharField(max_length=40, index=True)
    transcription = fields.CharField(max_length=40)
    part_speech = fields.IntEnumField(enum_type=PartSpeechEnum, description='Part of Speech')
    # TODO use FileField
    # sound = fields.BinaryField()

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f'{self.id} {self.title} {self.part_speech}'


class WordRusModel(WordBaseModel):

    class Meta:
        table = 'word_rus'


class WordEngModel(WordBaseModel):

    class Meta:
        table = 'word_eng'


class TranslatorBaseModel(BaseModel):
    frequency = fields.IntEnumField(
        enum_type=TranslationFrequencyEnum, description='How common is the translation variant')

    class Meta:
        abstract = True

    @property
    @abstractmethod
    def word(self):
        pass

    @property
    @abstractmethod
    def translation(self):
        pass

    def __str__(self) -> str:
        return f'{self.id} "{self.word.title}" to "{self.translation.title}"'


class TranslatorRusEngModel(BaseModel):
    word_rus = fields.ForeignKeyField(model_name='words.WordRusModel')
    word_eng = fields.ForeignKeyField(model_name='words.WordEngModel')

    class Meta:
        table = 'translator_rus_eng'

    @property
    def word(self):
        return self.word_rus

    @property
    def translation(self):
        return self.word_eng


Tortoise.init_models(['app.words.models'], 'words')

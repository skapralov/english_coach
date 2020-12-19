from abc import abstractmethod

from tortoise import fields

from core.models import BaseModel
from users.models import UserModel
from words.enums import PartSpeechEnum, TranslationFrequencyEnum


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


class StudyWordBaseModel(BaseModel):
    user: fields.ForeignKeyRelation[UserModel] = fields.ForeignKeyField('users.UserModel', on_delete=fields.CASCADE)
    progress = fields.SmallIntField(description='knowledge of the word')
    word = fields.ForeignKeyField('words.WordBaseModel')

    @property
    def status(self) -> bool:
        return self.progress >= 5

    # async def check_answer(self, answer: int) -> bool:
    #     status_of_answer = self.word.id == answer
    #     self.progress = self.progress + 1 if status_of_answer else self.progress - 2
    #     self.progress = 0 if self.progress < 0 else self.progress
    #     await self.save()
    #     return status_of_answer

    def __str__(self) -> str:
        if self.status:
            return f'user {self.user.id} learned the word {self.word.title}'
        return f'user {self.user.id} progress {self.progress} word {self.word.title}'

    class Meta:
        abstract = True


class StudyWordRusEngModel(StudyWordBaseModel):
    word = fields.ForeignKeyField('words.WordEngModel')

    class Meta:
        table = 'study_word_rus_eng'


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


# Tortoise.init_models(['apps.words.models'], 'words')

from enum import IntEnum

from apps.core.enums import EnumMixin


class PartSpeechEnum(EnumMixin, IntEnum):
    verb = 1
    noun = 2
    adjective = 3
    pronoun = 4
    numerals = 5
    adverb = 6

    @classmethod
    def choices(cls):
        return {
            cls.verb: 'Verb',
            cls.noun: 'Noun',
            cls.adjective: 'Adjective',
            cls.pronoun: 'Pronoun',
            cls.numerals: 'Numerals',
            cls.adverb: 'Adverb',
        }


class TranslationFrequencyEnum(EnumMixin, IntEnum):
    more_often = 1
    often = 2
    less_often = 3
    seldom = 4
    hardly_ever = 5

    @classmethod
    def choices(cls):
        return {
            cls.more_often: 'More often',
            cls.often: 'Often',
            cls.less_often: 'Less often',
            cls.seldom: 'Seldom',
            cls.hardly_ever: 'Hardly ever',
        }

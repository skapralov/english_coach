from tortoise.models import Model
from tortoise import fields


class BaseModel(Model):
    id = fields.IntField(pk=True)
    created = fields.DatetimeField(auto_now_add=True)
    modified = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True

from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
from tortoise import fields

from app.core.models import BaseModelTortoise


class User(BaseModelTortoise):
    username = fields.CharField(max_length=128, unique=True)
    email = fields.CharField(max_length=128, unique=True)
    password_hash = fields.CharField(max_length=128)
    is_active = fields.BooleanField(default=True)
    is_admin = fields.BooleanField(default=False)

    refresh_tokens: fields.ReverseRelation['RefreshToken']

    class PydanticMeta:
        exclude = ["password_hash"]

    def __str__(self) -> str:
        return f'ID {self.id} {self.username}'


User_Pydantic = pydantic_model_creator(User, name='User')
UserIn_Pydantic = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)


class RefreshToken(Model):
    uuid = fields.UUIDField(pk=True)
    expires_in = fields.IntField()
    user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField('models.User', related_name='refresh_tokens')

    def __str__(self) -> str:
        return f'refresh for user_id {self.user}'


RefreshToken_Pydantic = pydantic_model_creator(RefreshToken, name='RefreshToken')

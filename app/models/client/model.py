from tortoise.fields import BooleanField, CharField, DatetimeField, ReverseRelation

from app.application.abstracts.database.base_model import BaseModel


class Client(BaseModel):
    full_name = CharField(max_length=255)
    email = CharField(max_length=100, unique=True)
    password = CharField(max_length=100)
    is_juridical = BooleanField(default=False)
    is_active = BooleanField(default=True)
    verification_code = CharField(min_length=6, max_length=6, null=True)
    expiration_code_time = DatetimeField(null=True, use_tz=True)
    email_is_verified = BooleanField(default=False)
    address = ReverseRelation["Address"]

    class Meta:
        table = "client"
        ordering = ["-id"]

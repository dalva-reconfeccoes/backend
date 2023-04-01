from tortoise.fields import BooleanField, CharField, IntField

from app.models.base_model import BaseModel


class Client(BaseModel):
    id = IntField(pk=True)
    uuid = CharField(max_length=32)
    full_name = CharField(max_length=255)
    email = CharField(max_length=100, unique=True)
    password = CharField(max_length=100)
    is_juridical = BooleanField(default=False)
    is_active = BooleanField(default=True)

    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        table = "client"
        ordering = ["-id"]

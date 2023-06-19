from tortoise.fields import CharField, ForeignKeyField, IntField, BooleanField

from app.application.abstracts.database.base_model import BaseModel


class Address(BaseModel):
    district = CharField(max_length=128, null=True)
    cep = CharField(max_length=128, null=True)
    city = CharField(max_length=128, null=True)
    street = CharField(max_length=128, null=True)
    uf = CharField(max_length=128, null=True)
    complement = CharField(max_length=128, null=True)
    neighborhood = CharField(max_length=128, null=True)
    number = IntField(null=True)
    is_active = BooleanField(default=False)
    client = ForeignKeyField("models.Client", related_name="address")

    class Meta:
        table = "address"
        ordering = ["-id"]

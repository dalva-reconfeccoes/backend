from tortoise.fields import CharField, BooleanField, ForeignKeyField

from app.application.abstracts.database.base_model import BaseModel


class Image(BaseModel):
    uuid = CharField(max_length=120)
    filename = CharField(max_length=255)
    content_type = CharField(max_length=255)
    bucket = CharField(max_length=255)
    is_active = BooleanField(default=True)
    product = ForeignKeyField("models.Product", related_name="images")

    class Meta:
        table = "image"
        ordering = ["-filename"]

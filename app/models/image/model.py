from tortoise.fields import CharField, BooleanField, ForeignKeyField

from app.models.base_model import BaseModel


class Image(BaseModel):
    filename = CharField(max_length=255)
    content_type = CharField(max_length=255)
    uuid = CharField(max_length=120)
    bucket = CharField(max_length=255)
    is_active = BooleanField(default=True)
    product = ForeignKeyField("models.Product", related_name="images")

    class Meta:
        table = "image"
        ordering = ["-id"]

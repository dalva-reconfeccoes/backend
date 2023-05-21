from tortoise.fields import (
    IntField,
    CharEnumField,
    ForeignKeyField,
)

from app.application.enums.product.size import ProductSizeEnum
from app.application.abstracts.database.base_model import BaseModel


class Quantity(BaseModel):
    size = CharEnumField(ProductSizeEnum)
    available = IntField(default=0, null=True)
    purchased = IntField(default=0, null=True)
    product = ForeignKeyField("models.Product", related_name="quantities")

    class Meta:
        table = "quantity"
        ordering = ["-size"]

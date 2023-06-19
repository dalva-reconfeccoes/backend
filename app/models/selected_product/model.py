from tortoise.fields import (
    ForeignKeyField,
    IntField,
    CharEnumField,
)

from app.application.abstracts.database.base_model import BaseModel
from app.application.enums.product.size import ProductSizeEnum


class SelectedProduct(BaseModel):
    size = CharEnumField(ProductSizeEnum)
    quantity = IntField()
    product = ForeignKeyField("models.Product", related_name="product", null=False)
    cart = ForeignKeyField("models.Cart", related_name="selected_products", null=False)

    class Meta:
        table = "selected_product"
        ordering = ["-id"]

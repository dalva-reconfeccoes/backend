from tortoise.fields import (
    CharField,
    FloatField,
    CharEnumField,
    BooleanField,
    ReverseRelation,
)

from app.application.enums.product.sex import ProductSexEnum
from app.application.enums.product.status import ProductStatusEnum
from app.application.enums.product.sub_type import ProductSubTypeEnum
from app.application.enums.product.type import ProductTypeEnum
from app.application.abstracts.database.base_model import BaseModel


class Product(BaseModel):
    header = CharField(max_length=255)
    color = CharField(max_length=255)
    knitted = CharField(max_length=255)
    price = FloatField()
    type = CharEnumField(ProductTypeEnum)
    sub_type = CharEnumField(ProductSubTypeEnum)
    sex = CharEnumField(ProductSexEnum)
    status = CharEnumField(ProductStatusEnum)
    is_active = BooleanField(default=True)
    description = CharField(max_length=1000, null=True)
    images = ReverseRelation["Image"]
    quantities = ReverseRelation["Quantity"]

    async def verify_available_quantity_size(self, size: str):
        for quantity in self.quantities:
            if quantity.size == size and quantity.available > 0:
                return True
        return False

    class Meta:
        table = "product"
        ordering = ["-id"]

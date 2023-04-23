from tortoise.fields import (
    IntField,
    CharField,
    FloatField,
    CharEnumField,
    BooleanField,
    ReverseRelation,
)
from app.application.enums.product.product_sex import ProductSexEnum
from app.application.enums.product.product_status import ProductStatusEnum
from app.application.enums.product.product_sub_type import ProductSubTypeEnum
from app.application.enums.product.product_type import ProductTypeEnum
from app.models.base_model import BaseModel


class Product(BaseModel):
    header = CharField(max_length=255)
    color = CharField(max_length=255)
    knitted = CharField(max_length=255)
    price = FloatField()
    quantity = IntField()
    type = CharEnumField(ProductTypeEnum)
    sub_type = CharEnumField(ProductSubTypeEnum)
    sex = CharEnumField(ProductSexEnum)
    status = CharEnumField(ProductStatusEnum)
    is_active = BooleanField(default=True)
    images = ReverseRelation["Image"]

    class Meta:
        table = "product"
        ordering = ["-id"]

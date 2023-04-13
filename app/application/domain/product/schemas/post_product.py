from fastapi_camelcase import CamelModel

from app.application.enums.product.product_sex import ProductSexEnum
from app.application.enums.product.product_status import ProductStatusEnum
from app.application.enums.product.product_sub_type import ProductSubTypeEnum
from app.application.enums.product.product_type import ProductTypeEnum


class PostProductSchema(CamelModel):
    header: str
    color: str
    knitted: str
    price: float
    quantity: int
    type: ProductTypeEnum
    sub_type: ProductSubTypeEnum
    sex: ProductSexEnum
    status: ProductStatusEnum

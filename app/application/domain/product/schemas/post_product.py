from typing import Optional

from fastapi_camelcase import CamelModel

from app.application.enums.product.sex import ProductSexEnum
from app.application.enums.product.status import ProductStatusEnum
from app.application.enums.product.sub_type import ProductSubTypeEnum
from app.application.enums.product.type import ProductTypeEnum


class PostProductSchema(CamelModel):
    header: str
    color: str
    knitted: str
    price: float
    type: ProductTypeEnum
    sub_type: ProductSubTypeEnum
    sex: ProductSexEnum
    status: ProductStatusEnum
    description: Optional[str]

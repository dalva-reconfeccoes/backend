from datetime import datetime
from typing import Optional, List

from fastapi_camelcase import CamelModel

from app.application.domain.image.schemas.get_image_url import GetImageUrlSchema
from app.application.enums.product.product_sex import ProductSexEnum
from app.application.enums.product.product_status import ProductStatusEnum
from app.application.enums.product.product_sub_type import ProductSubTypeEnum
from app.application.enums.product.product_type import ProductTypeEnum


class GetProductSchema(CamelModel):
    id: int
    uuid: str
    header: str
    color: str
    knitted: str
    price: float
    quantity: int
    type: ProductTypeEnum
    sub_type: ProductSubTypeEnum
    sex: ProductSexEnum
    status: ProductStatusEnum
    images: Optional[List[GetImageUrlSchema]]
    is_active: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

from datetime import datetime
from typing import Optional, List

from fastapi_camelcase import CamelModel

from app.application.domain.image.schemas.get_image_url import GetImageUrlSchema
from app.application.domain.quantity.schemas.get_quantity import GetQuantitySchema
from app.application.enums.product.sex import ProductSexEnum
from app.application.enums.product.status import ProductStatusEnum
from app.application.enums.product.sub_type import ProductSubTypeEnum
from app.application.enums.product.type import ProductTypeEnum


class GetProductSchema(CamelModel):
    id: int
    uuid: str
    header: str
    color: str
    knitted: str
    price: float
    type: ProductTypeEnum
    sub_type: ProductSubTypeEnum
    sex: ProductSexEnum
    status: ProductStatusEnum
    description: Optional[str]
    images: Optional[List[GetImageUrlSchema]]
    quantities: Optional[List[GetQuantitySchema]]
    is_active: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

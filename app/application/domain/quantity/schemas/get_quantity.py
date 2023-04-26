from datetime import datetime
from typing import Optional
from fastapi_camelcase import CamelModel
from app.application.enums.product.size import ProductSizeEnum


class GetQuantitySchema(CamelModel):
    id: int
    size: ProductSizeEnum
    available: int
    purchased: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

from typing import Optional

from fastapi_camelcase import CamelModel

from app.application.enums.product.size import ProductSizeEnum


class CreateSelectedProductSchema(CamelModel):
    size: ProductSizeEnum
    quantity: int
    product_id: int
    cart_id: Optional[int]

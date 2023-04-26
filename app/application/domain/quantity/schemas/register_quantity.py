from app.application.enums.product.size import ProductSizeEnum
from fastapi_camelcase import CamelModel


class RegisterQuantitySchema(CamelModel):
    size: ProductSizeEnum
    available: int
    product_id: int

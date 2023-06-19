from fastapi_camelcase import CamelModel

from app.application.domain.product.schemas.get_product import GetProductSchema
from app.application.enums.product.size import ProductSizeEnum


class GetSelectedProductSchema(CamelModel):
    uuid: str
    size: ProductSizeEnum
    quantity: int
    product: GetProductSchema

from fastapi_camelcase import CamelModel

from app.application.enums.product.type import ProductTypeEnum


class CalculateFreightOptionsSchema(CamelModel):
    cep: str
    quantity: int
    product_type: ProductTypeEnum

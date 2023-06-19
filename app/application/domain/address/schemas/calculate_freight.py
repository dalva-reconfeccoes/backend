from fastapi_camelcase import CamelModel
from app.application.enums.address.delivery_type import DeliveryTypeEnum
from app.application.enums.product.type import ProductTypeEnum


class CalculateFreightSchema(CamelModel):
    cep: str
    quantity: int
    product_type: ProductTypeEnum
    delivery_type: DeliveryTypeEnum

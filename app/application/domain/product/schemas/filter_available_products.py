from typing import Optional

from fastapi_camelcase import CamelModel

from app.application.enums.product.size import ProductSizeEnum
from app.application.enums.product.sub_type import ProductSubTypeEnum


class FilterAvailableProductSchema(CamelModel):
    colors: Optional[list[str]]
    sub_types: Optional[list[ProductSubTypeEnum]]
    sizes: Optional[list[ProductSizeEnum]]

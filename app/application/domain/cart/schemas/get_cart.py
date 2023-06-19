from datetime import datetime
from typing import Optional, List

from fastapi_camelcase import CamelModel

from app.application.domain.client.schemas import GetClientSchema
from app.application.domain.selected_product.schema.get_selected_product import (
    GetSelectedProductSchema,
)


class GetCartSchema(CamelModel):
    id: int
    uuid: str
    total_value: float
    client: Optional[GetClientSchema]
    selected_products: Optional[List[GetSelectedProductSchema]]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

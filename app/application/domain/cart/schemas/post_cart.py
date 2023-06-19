from typing import Optional

from fastapi_camelcase import CamelModel

from app.application.domain.selected_product.schema.create_selected_product import (
    CreateSelectedProductSchema,
)


class PostCartSchema(CamelModel):
    selected_product: CreateSelectedProductSchema
    client_uuid: Optional[str]

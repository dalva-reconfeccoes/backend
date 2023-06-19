from uuid import uuid4

from app.application.domain.selected_product.abstracts.base_selected_product_usecase import (
    BaseSelectedProductUseCase,
)
from app.application.domain.selected_product.schema.create_selected_product import (
    CreateSelectedProductSchema,
)


class CreateSelectedProductUseCase(BaseSelectedProductUseCase):
    def __init__(self, payload: CreateSelectedProductSchema):
        super().__init__(payload)
        self._payload = payload

    async def _create_selected_product_db(self):
        selected_product_dict = self._payload.dict()
        selected_product_dict["uuid"] = uuid4().hex
        selected_product = await self._repository.create(selected_product_dict)
        return selected_product

    async def execute(self):
        selected_product = await self._create_selected_product_db()
        return await self._serializer(selected_product)

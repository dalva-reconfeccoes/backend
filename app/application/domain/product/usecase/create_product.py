from uuid import uuid4

from app.application.domain.product.schemas.post_product import PostProductSchema
from app.application.domain.product.abstracts.base_product_usecase import (
    BaseProductUseCase,
)
from app.application.helpers.utils import format_name
from app.models.product import Product


class CreateProductUseCase(BaseProductUseCase):
    def __init__(self, payload: PostProductSchema):
        super().__init__(payload)
        self._payload = payload

    async def _create_product_db(self) -> Product:
        self._payload.header = format_name(self._payload.header)
        product_dict = self._payload.dict()
        product_dict["uuid"] = uuid4().hex
        product = await self._repository.create(product_dict)
        return product

    async def execute(self):
        await self._validate_already_exists_db(header=self._payload.header)
        product = await self._create_product_db()
        return await self._serializer(product)

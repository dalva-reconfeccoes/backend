from app.application.domain.product.abstracts.base_product_usecase import (
    BaseProductUseCase,
)
from app.application.domain.product.schemas.filter_product import FilterProductSchema


class GetProductUseCase(BaseProductUseCase):
    def __init__(self, payload: FilterProductSchema):
        super().__init__(payload)

    async def execute(self):
        await self._validate_values_payload()
        product = await self._validate_db(**self._payload_clean)
        return await self._serializer(product)

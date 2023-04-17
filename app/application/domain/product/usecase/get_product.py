from app.application.domain.product.schemas.filter_product import FilterProductSchema
from app.application.domain.product.usecase.base_product import BaseProductUseCase
from app.application.helpers.utils import validate_values_payload


class GetProductUseCase(BaseProductUseCase):
    def __init__(self, payload: FilterProductSchema):
        super().__init__(payload)

    async def execute(self):
        data = await validate_values_payload(self._payload.dict())
        product = await self._validate_db(**data)
        return await self._serializer(product)

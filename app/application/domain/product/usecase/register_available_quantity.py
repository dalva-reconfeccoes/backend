from typing import List

from app.application.domain.product.abstracts.base_product_usecase import (
    BaseProductUseCase,
)
from app.application.domain.quantity.schemas.register_quantity import (
    RegisterQuantitySchema,
)
from app.application.domain.quantity.usecase.register_quantity import (
    RegisterOrUpdateQuantityUseCase,
)


class RegisterAvailableQuantity(BaseProductUseCase):
    def __init__(self, payload: List[RegisterQuantitySchema]):
        super().__init__(None)
        self._list_payload = payload

    async def execute(self):
        result = []
        for quantity_schema in self._list_payload:
            await self._validate_db(id=quantity_schema.product_id)
            await RegisterOrUpdateQuantityUseCase(quantity_schema).execute()
            updated_product = await self._serializer(
                await self._filter_db(id=quantity_schema.product_id)
            )
            result.append(updated_product)
        return result

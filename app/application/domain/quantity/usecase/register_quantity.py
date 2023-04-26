from uuid import uuid4

from app.application.domain.quantity.schemas.get_quantity import GetQuantitySchema
from app.application.domain.quantity.schemas.register_quantity import (
    RegisterQuantitySchema,
)
from app.application.domain.quantity.usecase.base_quantity import BaseQuantityUseCase
from app.models.quantity import Quantity


class RegisterOrUpdateQuantityUseCase(BaseQuantityUseCase):
    def __init__(self, payload: RegisterQuantitySchema):
        super().__init__(payload)
        self._payload = payload

    async def _register_db(self) -> Quantity:
        quantity_dict = self._payload.dict()
        quantity_dict["uuid"] = uuid4().hex
        quantity = await self._repository.create(quantity_dict)
        return quantity

    async def _update_db(self, quantity: Quantity):
        update_available = quantity.available + self._payload.available
        return await self._repository.update(
            dict(available=update_available), quantity.id
        )

    async def _register_or_update(self, quantity):
        if not quantity:
            quantity = await self._register_db()
        else:
            quantity = await self._update_db(quantity)
        return quantity

    async def execute(self) -> GetQuantitySchema:
        quantity = await self._filter_db(
            product_id=self._payload.product_id, size=self._payload.size
        )
        quantity = await self._register_or_update(quantity)
        return await self._serializer(quantity)

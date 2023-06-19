from app.application.domain.cart.abstracts.base_cart_usecase import BaseCartUseCase
from app.application.domain.cart.schemas.filter_cart import FilterCartSchema


class GetCartUseCase(BaseCartUseCase):
    def __init__(self, payload: FilterCartSchema):
        super().__init__(payload)

    async def execute(self):
        await self._validate_values_payload()
        cart = await self._validate_db(**self._payload_clean)
        return await self._serializer(cart)

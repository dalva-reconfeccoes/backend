from app.application.domain.cart.abstracts.base_cart_usecase import BaseCartUseCase
from app.application.domain.cart.schemas.filter_cart import FilterCartSchema
from app.application.helpers.utils import validate_values_payload


class GetCartUseCase(BaseCartUseCase):
    def __init__(self, payload: FilterCartSchema):
        super().__init__(payload)

    async def execute(self):
        data = await validate_values_payload(self._payload.dict())
        cart = await self._validate_db(**data)
        return await self._serializer(cart)

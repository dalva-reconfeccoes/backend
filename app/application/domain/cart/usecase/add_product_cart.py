from uuid import uuid4

from fastapi import HTTPException, status

from app.application.domain.cart.abstracts.base_cart_usecase import BaseCartUseCase
from app.application.domain.cart.schemas.post_cart import PostCartSchema
from app.application.domain.product.schemas.filter_product import FilterProductSchema
from app.application.domain.product.usecase.get_product import GetProductUseCase
from app.application.domain.selected_product.schema.create_selected_product import (
    CreateSelectedProductSchema,
)
from app.application.domain.selected_product.usecase.create_selected_product import (
    CreateSelectedProductUseCase,
)
from app.application.enums.messages_enum import MessagesEnum


class AddProductCartUseCase(BaseCartUseCase):
    _payload: PostCartSchema

    def __init__(self, uuid_cart: str, payload: PostCartSchema):
        super().__init__(payload)
        self._payload = payload
        self._uuid_cart = uuid_cart

    async def execute(self):
        await self._validate_product(
            FilterProductSchema(id=self._payload.selected_product.product_id),
            self._payload.selected_product,
        )
        cart = await self._validate_db(uuid=self._uuid_cart)
        self._payload.selected_product.cart_id = cart.id
        await CreateSelectedProductUseCase(self._payload.selected_product).execute()
        await self._calculate_total_value(cart)
        return await self._serializer(cart)

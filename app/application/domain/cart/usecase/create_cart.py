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


class CreateCartUseCase(BaseCartUseCase):
    _payload: PostCartSchema

    def __init__(self, payload: PostCartSchema):
        super().__init__(payload)
        self._payload = payload

    async def _create_cart_db(self):
        cart_dict = self._payload.dict()
        cart_dict["uuid"] = uuid4().hex
        cart = await self._repository.create(cart_dict)
        return cart

    async def execute(self):
        await self._validate_product(
            FilterProductSchema(id=self._payload.selected_product.product_id),
            self._payload.selected_product,
        )
        cart = await self._create_cart_db()
        self._payload.selected_product.cart_id = cart.id
        await CreateSelectedProductUseCase(self._payload.selected_product).execute()
        await self._calculate_total_value(cart)
        return await self._serializer(cart)

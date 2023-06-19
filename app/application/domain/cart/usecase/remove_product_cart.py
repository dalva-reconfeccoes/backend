from fastapi import HTTPException, status

from app.application.domain.cart.abstracts.base_cart_usecase import BaseCartUseCase
from app.application.enums.messages_enum import MessagesEnum


class RemoveProductCartUseCase(BaseCartUseCase):
    def __init__(self, uuid_cart: str, selected_product_uuid: str):
        super().__init__()
        self._uuid_cart = uuid_cart
        self._selected_product_uuid = selected_product_uuid

    async def _remove_selected_product(self, cart):
        selected = await cart.selected_products.filter(uuid=self._selected_product_uuid)
        if not selected:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=MessagesEnum.PRODUCT_NOT_FOUND,
            )
        await selected.pop().delete()

    async def execute(self):
        cart = await self._validate_db(uuid=self._uuid_cart)
        await self._remove_selected_product(cart)
        await self._calculate_total_value(cart)
        return await self._serializer(cart)

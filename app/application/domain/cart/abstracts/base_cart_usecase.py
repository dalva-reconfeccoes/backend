from fastapi import HTTPException, status
from fastapi_camelcase import CamelModel
from tortoise.contrib.pydantic import pydantic_model_creator

from app.application.abstracts.usecase.base_usecase import BaseUseCase
from app.application.domain.cart.schemas.get_cart import GetCartSchema
from app.application.domain.product.schemas.filter_product import FilterProductSchema
from app.application.domain.product.usecase.get_product import GetProductUseCase
from app.application.domain.selected_product.schema.create_selected_product import (
    CreateSelectedProductSchema,
)
from app.application.enums.messages_enum import MessagesEnum
from app.infra.database.repositories.cart.repository import CartRepository
from app.infra.database.repositories.selected_product.repository import (
    SelectedProductRepository,
)
from app.models.cart import Cart


class BaseCartUseCase(BaseUseCase):
    _repository: CartRepository

    def __init__(self, payload: CamelModel = None):
        super().__init__("Cart", payload, CartRepository())
        self._payload = payload
        self._pydantic_model = pydantic_model_creator(Cart)
        self._selected_product_repository = SelectedProductRepository()

    async def _serializer(self, model: Cart):
        pyd_model = await self._pydantic_model.from_tortoise_orm(model)
        model_schema = GetCartSchema(**pyd_model.dict())
        return model_schema

    async def _validate_product(
        self,
        filter_schema: FilterProductSchema,
        selected_product: CreateSelectedProductSchema,
    ):
        product = await GetProductUseCase(filter_schema).get_model()
        product_quantities = await product.quantities.filter(
            size=selected_product.size,
            available__gte=selected_product.quantity,
        )
        if not product_quantities:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=MessagesEnum.PRODUCT_NOT_AVAILABLE,
            )

    async def _calculate_total_value(self, cart: Cart):
        cart.total_value = 0
        for selected in await cart.selected_products:
            product = await selected.product
            cart.total_value += product.price * selected.quantity
        await cart.save()

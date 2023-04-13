from fastapi import HTTPException, status

from app.application.domain.product.schemas.get_product import GetProductSchema
from app.application.enums.messages_enum import MessagesEnum
from app.infra.database.repositories.product.repository import ProductRepository
from app.models.product import Product


class BaseProductUseCase:
    def __init__(self, payload):
        self._payload = payload
        self._repository = ProductRepository()

    async def _validate_db(self, **kwargs) -> Product:
        product = await self._repository.get_or_none(**kwargs)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=MessagesEnum.PRODUCT_NOT_FOUND,
            )
        return product

    async def _validate_already_existing_db(self, **kwargs):
        product = await self._repository.get_or_none(**kwargs)
        if product:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=MessagesEnum.PRODUCT_ALREADY_EXIST,
            )

    async def _serializer(self, product: Product) -> GetProductSchema:
        return GetProductSchema.from_orm(product)

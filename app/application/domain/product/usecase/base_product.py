from fastapi_camelcase import CamelModel
from tortoise.contrib.pydantic import pydantic_model_creator

from app.application.abstracts.usecase.base_usecase import BaseUseCase
from app.application.domain.product.schemas.get_product import GetProductSchema
from app.infra.database.repositories.product.repository import ProductRepository
from app.infra.file_storage.minio import get_minio_storage
from app.models.product import Product


class BaseProductUseCase(BaseUseCase):
    _repository: ProductRepository

    def __init__(self, payload: CamelModel = None):
        super().__init__("Product", payload, ProductRepository())
        self._payload = payload
        self._filestorage = get_minio_storage()
        self._pydantic_model = pydantic_model_creator(Product)

    async def _serializer(self, product: Product):
        pyd_model = await self._pydantic_model.from_tortoise_orm(product)
        products_schema = GetProductSchema(**pyd_model.dict())
        return await self._set_images_url(products_schema)

    async def _set_images_url(self, products_schema: GetProductSchema):
        for image in products_schema.images:
            url = await self._filestorage.get_file_url(image.filename)
            image.url = url
        return products_schema

    async def _serializer_and_remove_duplicate_available_products(
        self, products: [Product]
    ) -> [GetProductSchema]:
        result = []
        verification = set()
        for prod in products:
            if prod.id not in verification:
                verification.add(prod.id)
                result.append(await self._serializer(prod))
        return result

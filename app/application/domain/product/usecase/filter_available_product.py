from fastapi import HTTPException

from app.application.domain.product.schemas.filter_available_products import (
    FilterAvailableProductSchema,
)
from app.application.domain.product.schemas.get_product import GetProductSchema
from app.application.domain.product.abstracts.base_product_usecase import (
    BaseProductUseCase,
)


class FilterAvailableProductUseCase(BaseProductUseCase):
    def __init__(self, payload: FilterAvailableProductSchema):
        super().__init__(payload)
        self._payload = payload

    async def _filter_products(self):
        filter_products = {}
        if "sub_types" in self._payload_clean.keys():
            filter_products["sub_type__in"] = self._payload_clean["sub_types"]
        if "colors" in self._payload_clean.keys():
            filter_products["color__in"] = self._payload_clean["colors"]
        if "sizes" in self._payload_clean.keys():
            filter_products["quantities__size__in"] = self._payload_clean["sizes"]
            filter_products["quantities__available__gt"] = 0
        products = await self._repository.filter(**filter_products)
        return products

    async def execute(self) -> [GetProductSchema]:
        try:
            await self._validate_values_payload()
            products = await self._filter_products()
        except HTTPException:
            products = await self._repository.get_all()

        return await self._serializer_and_remove_duplicate_available_products(products)

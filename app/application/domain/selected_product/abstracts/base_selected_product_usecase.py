from fastapi_camelcase import CamelModel
from tortoise.contrib.pydantic import pydantic_model_creator

from app.application.abstracts.usecase.base_usecase import BaseUseCase
from app.application.domain.selected_product.schema.get_selected_product import (
    GetSelectedProductSchema,
)
from app.infra.database.repositories.selected_product.repository import (
    SelectedProductRepository,
)
from app.models.selected_product import SelectedProduct


class BaseSelectedProductUseCase(BaseUseCase):
    _repository: SelectedProductRepository

    def __init__(self, payload: CamelModel = None):
        super().__init__("SelectedProduct", payload, SelectedProductRepository())
        self._payload = payload
        self._pydantic_model = pydantic_model_creator(SelectedProduct)

    async def _serializer(self, model: SelectedProduct):
        pyd_model = await self._pydantic_model.from_tortoise_orm(model)
        model_schema = GetSelectedProductSchema(**pyd_model.dict())
        return model_schema

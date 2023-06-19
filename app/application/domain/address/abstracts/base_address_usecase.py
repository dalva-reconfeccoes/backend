from fastapi_camelcase import CamelModel
from tortoise.contrib.pydantic import pydantic_model_creator

from app.application.abstracts.usecase.base_usecase import BaseUseCase
from app.application.domain.address.schemas.get_address import GetAddressSchema
from app.infra.database.repositories.address.repository import AddressRepository
from app.models.address import Address


class BaseAddressUseCase(BaseUseCase):
    _repository: AddressRepository

    def __init__(self, payload: CamelModel = None):
        super().__init__("Address", payload, AddressRepository())
        self._payload = payload
        self._pydantic_model = pydantic_model_creator(Address)

    async def _serializer(self, model: Address):
        pyd_model = await self._pydantic_model.from_tortoise_orm(model)
        model_schema = GetAddressSchema(**pyd_model.dict())
        return model_schema

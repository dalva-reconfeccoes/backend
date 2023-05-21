from fastapi_camelcase import CamelModel
from tortoise.contrib.pydantic import pydantic_model_creator

from app.application.abstracts.usecase.base_usecase import BaseUseCase
from app.application.domain.client.schemas import GetClientSchema
from app.infra.database.repositories.client.repository import ClientRepository
from app.infra.file_storage.minio import get_minio_storage
from app.models.client import Client


class BaseClientUseCase(BaseUseCase):
    _repository: ClientRepository

    def __init__(self, payload: CamelModel = None):
        super().__init__("Client", payload, ClientRepository())
        self._payload = payload
        self._filestorage = get_minio_storage()
        self._pydantic_model = pydantic_model_creator(Client)

    async def _serializer(self, client: Client):
        pyd_model = await self._pydantic_model.from_tortoise_orm(client)
        client_schema = GetClientSchema(**pyd_model.dict())
        return client_schema

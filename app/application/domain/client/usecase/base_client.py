from fastapi import HTTPException, status

from app.application.domain.client.schemas import GetClientSchema
from app.application.enums.messages_enum import MessagesEnum
from app.infra.database.repositories.client.repository import ClientRepository
from app.models.client import Client


class BaseClientUseCase:
    def __init__(self, payload):
        self._payload = payload
        self._repository = ClientRepository()

    async def _validate_db(self, **kwargs) -> Client:
        client = await self._repository.get_or_none(**kwargs)
        if not client:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=MessagesEnum.CLIENT_NOT_FOUND,
            )
        return client

    async def _filter_db(self, **kwargs) -> Client:
        client = await self._repository.get_or_none(**kwargs)
        if client:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=MessagesEnum.EMAIL_ALREADY_EXIST,
            )
        return client

    async def _serializer(self, client: Client) -> GetClientSchema:
        return GetClientSchema.from_orm(client)

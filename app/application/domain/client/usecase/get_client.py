from fastapi import HTTPException

from app.application.domain.client.schemas import GetClientSchema
from app.application.enums.messages_enum import MessagesEnum
from app.infra.database.repositories.client import repository


class GetClientUseCase:
    def __init__(self, uuid: str):
        self._uuid = uuid
        self._repository = repository.ClientRepository()

    async def _validate(self):
        client = await self._repository.get_or_none(uuid=self._uuid)
        if not client:
            raise HTTPException(status_code=400, detail=MessagesEnum.CLIENT_NOT_FOUND)
        return client

    async def execute(self):
        client = await self._validate()
        return GetClientSchema.from_orm(client)

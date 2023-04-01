from fastapi import HTTPException

from app.application.domain.client.schemas import GetClientSchema
from app.application.enums.messages_enum import MessagesEnum
from app.infra.database.repositories.client import repository


class GetClientByEmailUseCase:
    def __init__(self, email: str):
        self._email = email
        self._repository = repository.ClientRepository()

    async def _validate(self):
        client = await self._repository.get_by_email(self._email)
        if not client:
            raise HTTPException(status_code=404, detail=MessagesEnum.CLIENT_NOT_FOUND)
        return client

    async def execute(self):
        client = await self._validate()
        return GetClientSchema.from_orm(client)

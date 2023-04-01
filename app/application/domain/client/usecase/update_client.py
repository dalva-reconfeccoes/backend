from fastapi import HTTPException
from passlib.hash import pbkdf2_sha256

from app.application.domain.client.schemas import GetClientSchema, UpdateClientSchema
from app.application.enums.messages_enum import MessagesEnum
from app.infra.database.repositories.client import repository


class UpdateClientUseCase:
    def __init__(self, payload: UpdateClientSchema, id: int):
        self._id = id
        self._payload = payload
        self._repository = repository.ClientRepository()

    async def _validate(self):
        client = await self._repository.get_by_id(self._id)
        if not client:
            raise HTTPException(status_code=404, detail=MessagesEnum.CLIENT_NOT_FOUND)

    async def _validate_email(self):
        client = await self._repository.get_by_email(self._payload.email)
        if client and client.id != self._id:
            raise HTTPException(
                status_code=400, detail=MessagesEnum.EMAIL_ALREADY_EXIST
            )

    async def execute(self):
        await self._validate()
        await self._validate_email()

        client_payload = self._payload.dict()
        client_payload["password"] = pbkdf2_sha256.hash(self._payload.password)

        updated = await self._repository.update(client_payload, self._id)
        if not updated:
            raise HTTPException(status_code=400, detail=MessagesEnum.CLIENT_NOT_FOUND)
        result = await self._repository.get_by_id(self._id)

        return GetClientSchema.from_orm(result)

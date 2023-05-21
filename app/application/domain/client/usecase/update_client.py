from fastapi import HTTPException, status
from passlib.hash import pbkdf2_sha256

from app.application.domain.client.abstracts.base_client_usecase import (
    BaseClientUseCase,
)
from app.application.domain.client.schemas import GetClientSchema, UpdateClientSchema
from app.application.enums.messages_enum import MessagesEnum


class UpdateClientUseCase(BaseClientUseCase):
    def __init__(self, payload: UpdateClientSchema, id: int):
        super().__init__(payload)
        self._payload = payload
        self._id = id

    async def _validate_email(self):
        client = await self._repository.get_by_email(self._payload.email)
        if client and client.id != self._id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=MessagesEnum.EMAIL_ALREADY_EXIST,
            )

    async def _update_data(self):
        client_payload = self._payload.dict()
        client_payload["password"] = pbkdf2_sha256.hash(self._payload.password)
        client = await self._repository.update(client_payload, self._id)
        return client

    async def execute(self):
        await self._validate_db(id=self._id)
        await self._validate_email()
        client = await self._update_data()
        return GetClientSchema.from_orm(client)

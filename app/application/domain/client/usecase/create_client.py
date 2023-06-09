from fastapi import HTTPException
from passlib.hash import pbkdf2_sha256
from uuid import uuid4

from app.application.domain.client.schemas import GetClientSchema, PostClientSchema
from app.application.enums.messages_enum import MessagesEnum
from app.infra.database.repositories.client import repository


class CreateClientUseCase:
    def __init__(self, payload: PostClientSchema):
        self._payload = payload
        self._repository = repository.ClientRepository()

    async def _validate_email(self):
        client = await self._repository.get_by_email(self._payload.email)
        if client:
            raise HTTPException(
                status_code=400, detail=MessagesEnum.EMAIL_ALREADY_EXIST
            )

    async def execute(self):
        await self._validate_email()

        self._payload.password = pbkdf2_sha256.hash(self._payload.password)
        client_dict = self._payload.dict()
        client_dict["uuid"] = uuid4().hex
        client = await self._repository.create(client_dict)
        return GetClientSchema.from_orm(client)

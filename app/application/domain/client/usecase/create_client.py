from fastapi import HTTPException, status
from passlib.hash import pbkdf2_sha256
from uuid import uuid4

from app.application.domain.client.schemas import GetClientSchema, PostClientSchema
from app.application.domain.client.usecase.base_client import BaseClientUseCase
from app.application.enums.messages_enum import MessagesEnum
from app.application.helpers.utils import format_client_name
from app.infra.database.repositories.client import repository


class CreateClientUseCase(BaseClientUseCase):
    def __init__(self, payload: PostClientSchema):
        super().__init__(payload)
        self._payload = payload

    async def _create_client_db(self):
        self._payload.password = pbkdf2_sha256.hash(self._payload.password)
        self._payload.full_name = format_client_name(self._payload.full_name)
        client_dict = self._payload.dict()
        client_dict["uuid"] = uuid4().hex
        client = await self._repository.create(client_dict)
        return client

    async def execute(self):
        await self._filter_db(email=self._payload.email)
        client = await self._create_client_db()
        return await self._serializer(client)

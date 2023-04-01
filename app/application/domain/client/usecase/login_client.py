from fastapi import HTTPException
from fastapi_jwt_auth import AuthJWT
from passlib.hash import pbkdf2_sha256

from app.application.domain.client.schemas import JWTClientSchema, LoginClientSchema
from app.application.enums.messages_enum import MessagesEnum
from app.infra.database.repositories.client import repository


class LoginUseCase:
    def __init__(self, payload: LoginClientSchema, authorize: AuthJWT):
        self._payload = payload
        self._repository = repository.ClientRepository()
        self._authorize = authorize

    async def _validate(self):
        client = await self._repository.get_by_email(self._payload.email)
        if not client:
            raise HTTPException(status_code=404, detail=MessagesEnum.CLIENT_NOT_FOUND)
        return client

    async def _serializer(self, client):
        access_token = self._authorize.create_access_token(subject=client.email)
        return {
            "email": client.email,
            "access_token": access_token,
        }

    async def execute(self):
        client = await self._validate()
        if not pbkdf2_sha256.verify(self._payload.password, client.password):
            raise HTTPException(status_code=400, detail=MessagesEnum.INVALID_PASSWORD)
        client_serialized = await self._serializer(client)
        return JWTClientSchema(**client_serialized)

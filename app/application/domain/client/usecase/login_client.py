from fastapi import HTTPException, status
from fastapi_jwt_auth import AuthJWT
from passlib.hash import pbkdf2_sha256

from app.application.domain.client.schemas import JWTClientSchema, LoginClientSchema
from app.application.domain.client.abstracts.base_client_usecase import (
    BaseClientUseCase,
)
from app.application.enums.messages_enum import MessagesEnum


class LoginUseCase(BaseClientUseCase):
    def __init__(self, payload: LoginClientSchema, authorize: AuthJWT):
        super().__init__(payload)
        self._payload = payload
        self._authorize = authorize

    async def _serializer_token(self, client):
        access_token = self._authorize.create_access_token(subject=client.email)
        return JWTClientSchema(email=client.email, access_token=access_token)

    async def _verify_password(self, client):
        if not pbkdf2_sha256.verify(self._payload.password, client.password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=MessagesEnum.INVALID_PASSWORD,
            )

    async def execute(self):
        client = await self._validate_db(email=self._payload.email)
        await self._verify_password(client)
        return await self._serializer_token(client)

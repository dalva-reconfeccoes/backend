from fastapi import HTTPException, status

from app.application.domain.client.schemas.verification_code import (
    VerificationCodeSchema,
)
from app.application.domain.client.usecase.base_client import BaseClientUseCase
from app.application.enums.messages_enum import MessagesEnum
from app.application.helpers.utils import (
    valid_verification_code,
)
from app.application.schemas.simple_message_schema import SimpleMessageSchema
from app.infra.database.repositories.client import repository
from app.models.client import Client


class ValidateVerificationCodeUseCase(BaseClientUseCase):
    def __init__(self, payload: VerificationCodeSchema):
        super().__init__(payload)
        self.__payload = payload

    async def __verify_code(self, client):
        valid_verification_code(
            self.__payload.code, client.verification_code, client.expiration_code_time
        )
        client.email_is_verified = True
        await client.save()

    async def execute(self):
        client = await self._validate_db(email=self.__payload.email)
        await self.__verify_code(client)
        return SimpleMessageSchema(message=MessagesEnum.VERIFICATION_SENT)

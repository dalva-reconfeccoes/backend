from fastapi import HTTPException, status

from app.application.domain.client.schemas.filter_client import FilterClientSchema
from app.application.domain.client.schemas.send_verification_code import (
    SendVerificationCodeSchema,
)
from app.application.enums.messages_enum import MessagesEnum
from app.application.helpers.utils import (
    clean_none_values_dict,
    generate_verification_code,
    validate_values_payload,
)
from app.application.schemas.simple_message_schema import SimpleMessageSchema
from app.infra.database.repositories.client import repository
from app.models.client import Client


class GenerateVerificationCodeUseCase:
    def __init__(self, payload: SendVerificationCodeSchema):
        self._repository = repository.ClientRepository()
        self.__payload = payload

    async def _validate_db(self) -> Client:
        client = await self._repository.get_by_email(self.__payload.email)
        if not client:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=MessagesEnum.CLIENT_NOT_FOUND,
            )
        return client

    async def __update_verification_code(self):
        client = await self._validate_db()
        code, expiration = generate_verification_code()
        client.verification_code = code
        client.expiration_code_time = expiration
        await client.save()

    async def execute(self) -> SimpleMessageSchema:
        await self.__update_verification_code()
        # TODO: Send email with verification code.
        return SimpleMessageSchema(message=MessagesEnum.VERIFICATION_SENT)

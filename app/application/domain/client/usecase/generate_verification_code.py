from fastapi import HTTPException, status

from app.application.domain.client.schemas.filter_client import FilterClientSchema
from app.application.enums.messages_enum import MessagesEnum
from app.application.helpers.utils import (
    clean_none_values_dict,
    generate_verification_code,
)
from app.application.schemas.simple_message_schema import SimpleMessageSchema
from app.infra.database.repositories.client import repository
from app.models.client import Client


class GenerateVerificationCode:
    def __init__(self, payload: FilterClientSchema):
        self.__payload = payload
        self._repository = repository.ClientRepository()

    async def __validate_values_payload(self):
        clean_dict = await clean_none_values_dict(self.__payload.dict())
        if len(clean_dict.keys()) == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=MessagesEnum.PARAMETERS_NOT_FOUND,
            )

    async def _validate_db(self) -> Client:
        client = await self._repository.get_or_none(**self.__payload.dict())
        if not client:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=MessagesEnum.CLIENT_NOT_FOUND,
            )
        return client

    async def execute(self) -> SimpleMessageSchema:
        await self.__validate_values_payload()
        client = await self._validate_db()
        code, expiration = generate_verification_code()
        client.verification_code = code
        client.expiration_code_time = expiration
        await client.save()
        return SimpleMessageSchema(details=MessagesEnum.VERIFICATION_SENT)

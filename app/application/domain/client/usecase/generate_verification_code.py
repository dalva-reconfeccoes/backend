from app.application.domain.client.schemas.send_verification_code import (
    SendVerificationCodeSchema,
)
from app.application.domain.client.usecase.base_client import BaseClientUseCase
from app.application.enums.messages_enum import MessagesEnum
from app.application.helpers.utils import (
    generate_verification_code,
)
from app.application.schemas.simple_message_schema import SimpleMessageSchema


class GenerateVerificationCodeUseCase(BaseClientUseCase):
    def __init__(self, payload: SendVerificationCodeSchema):
        super().__init__(payload)
        self._payload = payload

    async def __update_verification_code(self):
        client = await self._validate_db(email=self._payload.email)
        code, expiration = generate_verification_code()
        client.verification_code = code
        client.expiration_code_time = expiration
        await client.save()

    async def execute(self) -> SimpleMessageSchema:
        await self.__update_verification_code()
        # TODO: Send email with verification code.
        return SimpleMessageSchema(message=MessagesEnum.VERIFICATION_SENT)

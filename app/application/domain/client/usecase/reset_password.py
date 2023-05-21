from passlib.handlers.pbkdf2 import pbkdf2_sha256

from app.application.domain.client.schemas.reset_password import ResetPasswordSchema
from app.application.domain.client.abstracts.base_client_usecase import (
    BaseClientUseCase,
)
from app.application.enums.messages_enum import MessagesEnum
from app.application.schemas.simple_message_schema import SimpleMessageSchema
from app.models.client import Client


class ResetPasswordUseCase(BaseClientUseCase):
    def __init__(self, payload: ResetPasswordSchema):
        super().__init__(payload)
        self._payload = payload

    async def _update_password(self, client: Client):
        client.password = pbkdf2_sha256.hash(self._payload.password)
        await client.save()

    async def execute(self):
        client = await self._validate_db(email=self._payload.email)
        await self._update_password(client)
        return SimpleMessageSchema(message=MessagesEnum.UPDATED_PASSWORD)

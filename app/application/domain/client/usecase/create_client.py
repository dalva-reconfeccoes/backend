from uuid import uuid4

from passlib.hash import pbkdf2_sha256

from app.application.domain.client.abstracts.base_client_usecase import (
    BaseClientUseCase,
)
from app.application.domain.client.schemas import PostClientSchema
from app.application.helpers.utils import format_name


class CreateClientUseCase(BaseClientUseCase):
    def __init__(self, payload: PostClientSchema):
        super().__init__(payload)
        self._payload = payload

    async def _create_client_db(self):
        self._payload.password = pbkdf2_sha256.hash(self._payload.password)
        self._payload.full_name = format_name(self._payload.full_name)
        client_dict = self._payload.dict()
        client_dict["uuid"] = uuid4().hex
        client = await self._repository.create(client_dict)
        return client

    async def execute(self):
        await self._validate_already_exists_db(email=self._payload.email)
        client = await self._create_client_db()
        return await self._serializer(client)

from app.application.domain.client.schemas.filter_client import FilterClientSchema
from app.application.domain.client.abstracts.base_client_usecase import (
    BaseClientUseCase,
)
from app.application.helpers.utils import validate_values_payload


class GetClientUseCase(BaseClientUseCase):
    def __init__(self, payload: FilterClientSchema):
        super().__init__(payload)
        self._payload = payload

    async def execute(self):
        data = await validate_values_payload(self._payload.dict())
        client = await self._validate_db(**data)
        return await self._serializer(client)

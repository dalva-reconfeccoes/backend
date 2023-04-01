from app.application.domain.client.schemas import GetClientSchema
from app.infra.database.repositories.client import repository


class GetClientsUseCase:
    def __init__(self):
        self._repository = repository.ClientRepository()

    async def _serializer(self, client):
        return GetClientSchema.from_orm(client)

    async def execute(self):
        clients = await self._repository.get_all()
        return [await self._serializer(client) for client in clients]

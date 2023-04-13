from app.application.domain.client.usecase.base_client import BaseClientUseCase


class GetClientsUseCase(BaseClientUseCase):
    def __init__(self):
        super().__init__(None)

    async def execute(self):
        clients = await self._repository.get_all()
        return [await self._serializer(client) for client in clients]

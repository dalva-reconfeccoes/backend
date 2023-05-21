from app.application.domain.client.abstracts.base_client_usecase import (
    BaseClientUseCase,
)


class GetClientsUseCase(BaseClientUseCase):
    def __init__(self):
        super().__init__(None)

    async def execute(self):
        clients = await self._repository.get_all()
        return [await self._serializer(client) for client in clients]

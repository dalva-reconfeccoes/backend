from app.models.client import Client
from app.application.abstracts.database.base_repository import BaseRepository


class ClientRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.entity = Client

    async def get_by_email(self, email: str) -> [dict, None]:
        return await self.get_or_none(email=email)

from app.infra.database.repositories.base_repository import BaseRepository
from app.models.product import Product


class ProductRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.entity = Product

    async def get_or_none(self, **kwargs):
        return await self.entity.get_or_none(**kwargs)

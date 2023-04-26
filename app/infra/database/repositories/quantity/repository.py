from app.infra.database.repositories.base_repository import BaseRepository
from app.models.quantity import Quantity


class QuantityRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.entity = Quantity

from app.application.abstracts.database.base_repository import BaseRepository
from app.models.address import Address


class AddressRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.entity = Address

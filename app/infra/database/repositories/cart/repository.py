from app.application.abstracts.database.base_repository import BaseRepository
from app.models.cart import Cart


class CartRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.entity = Cart

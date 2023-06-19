from app.application.abstracts.database.base_repository import BaseRepository
from app.models.selected_product import SelectedProduct


class SelectedProductRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.entity = SelectedProduct

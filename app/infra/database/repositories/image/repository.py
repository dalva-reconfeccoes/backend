from app.application.abstracts.database.base_repository import BaseRepository
from app.models.image import Image


class ImageRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.entity = Image

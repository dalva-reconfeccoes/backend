from app.application.abstracts.usecase.base_usecase import BaseUseCase
from app.application.domain.image.schemas.get_image import GetImageSchema
from app.infra.database.repositories.image.repository import ImageRepository
from app.models.image import Image


class BaseImageUseCase(BaseUseCase):
    def __init__(self, payload):
        super().__init__("Image", payload, ImageRepository())
        self._payload = payload

    async def _serializer(self, product: Image) -> GetImageSchema:
        return GetImageSchema.from_orm(product)

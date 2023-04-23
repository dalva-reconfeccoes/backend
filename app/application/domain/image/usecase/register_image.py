from uuid import uuid4

from app.application.domain.image.schemas.register_image import RegisterImageSchema
from app.application.domain.image.usecase.base_image import BaseImageUseCase
from app.models.image import Image


class CreateImageUseCase(BaseImageUseCase):
    def __init__(self, payload: RegisterImageSchema):
        super().__init__(payload)
        self._payload = payload

    async def _register_image_db(self) -> Image:
        image_dict = self._payload.dict()
        image_dict["uuid"] = uuid4().hex
        image = await self._repository.create(image_dict)
        return image

    async def execute(self):
        await self._validate_already_exists_db(filename=self._payload.filename)
        image = await self._register_image_db()
        return await self._serializer(image)

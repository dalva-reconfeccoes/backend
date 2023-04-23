from typing import List

from fastapi import File, UploadFile, HTTPException
from loguru import logger

from app.application.domain.image.schemas.register_image import RegisterImageSchema
from app.application.domain.image.usecase.register_image import CreateImageUseCase
from app.application.domain.product.usecase.base_product import BaseProductUseCase


class RegisterProductImageUseCase(BaseProductUseCase):
    def __init__(
        self,
        product_uuid,
        images: List[UploadFile] = File(),
    ):
        super().__init__()
        self._product_uuid = product_uuid
        self._images = images

    async def _register_image_db(self, product_id: int):
        async def register_db(image: UploadFile):
            new_image_schema = RegisterImageSchema(
                filename=image.filename,
                content_type=image.content_type,
                bucket=self._filestorage.bucket_name,
                product_id=product_id,
            )
            await CreateImageUseCase(new_image_schema).execute()

        async def register_filestorage(image: UploadFile):
            await self._filestorage.save_binary_file(
                filename=image.filename,
                content_type=image.content_type,
                file_content=image.file.read(),
            )

        for img in self._images:
            try:
                await register_db(img)
                await register_filestorage(img)
            except HTTPException as exc:
                logger.error(exc.detail)

    async def execute(self):
        product = await self._validate_db(uuid=self._product_uuid)
        await self._register_image_db(product.id)
        return await self._serializer(product)

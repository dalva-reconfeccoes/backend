import io
from functools import lru_cache

from loguru import logger
from minio import Minio
from app.infra.settings import get_settings

settings = get_settings()


class MinioStorage:
    def __init__(self):
        self._url = settings.MINIO_URL
        self._access_key = settings.MINIO_ACCESS_KEY
        self._secret_key = settings.MINIO_SECRET_KEY
        self.bucket_name = settings.MINIO_BUCKET_NAME
        self._client = self._init_client()

    def _init_client(self):
        logger.info("Initialize filestorage Minio...")
        return Minio(
            endpoint=self._url,
            access_key=self._access_key,
            secret_key=self._secret_key,
            secure=False,
        )

    async def bucket_exists(self, name: str):
        return self._client.bucket_exists(name)

    async def create_bucket(self):
        if not await self.bucket_exists(self.bucket_name):
            self._client.make_bucket(self.bucket_name)

    async def save_binary_file(
        self, filename: str, content_type: str, file_content: bytes
    ):
        self._client.put_object(
            bucket_name=self.bucket_name,
            object_name=filename,
            content_type=content_type,
            data=io.BytesIO(file_content),
            length=len(file_content),
        )

    async def save_file_in_bucket(self, filename: str, file_path: str):
        self._client.fput_object(
            bucket_name=self.bucket_name, object_name=filename, file_path=file_path
        )

    async def get_document_output(self, filename, file_path):
        self._client.fget_object(self.bucket_name, filename, file_path)
        return file_path

    async def get_file_url(self, filename: str):
        return self._client.get_presigned_url(
            method="GET", bucket_name=self.bucket_name, object_name=filename
        )


@lru_cache()
def get_storage_minio():
    return MinioStorage()

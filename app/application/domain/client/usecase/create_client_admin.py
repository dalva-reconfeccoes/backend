from uuid import uuid4
from decouple import config
from passlib.hash import pbkdf2_sha256

from app.application.domain.client.schemas import PostClientSchema
from app.infra.database.repositories.client import repository


class CreateClientAdminUseCase:
    def __init__(self):
        self._repository = repository.ClientRepository()
        self._create_admin_client = config("CREATE_ADMIN", default=False, cast=bool)

    async def _validate(self):
        if self._create_admin_client and not await self._repository.get_by_email(
            config("EMAIL_ADMIN")
        ):
            return PostClientSchema(
                email=config("EMAIL_ADMIN"),
                full_name=config("NAME_ADMIN"),
                password=pbkdf2_sha256.hash(config("PASSWORD_ADMIN")),
                is_active=True,
            ).dict()
        return None

    async def execute(self):
        client_dict = await self._validate()
        if client_dict:
            client_dict["uuid"] = uuid4().hex
            await self._repository.create(client_dict)

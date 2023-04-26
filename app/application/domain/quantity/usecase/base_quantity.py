from app.application.abstracts.usecase.base_usecase import BaseUseCase
from app.application.domain.quantity.schemas.get_quantity import GetQuantitySchema
from app.infra.database.repositories.quantity.repository import QuantityRepository
from app.models.quantity import Quantity


class BaseQuantityUseCase(BaseUseCase):
    def __init__(self, payload):
        super().__init__("Quantity", payload, QuantityRepository())
        self._payload = payload

    async def _serializer(self, quantity: Quantity) -> GetQuantitySchema:
        return GetQuantitySchema.from_orm(quantity)

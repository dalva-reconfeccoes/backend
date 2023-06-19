from app.application.domain.address.abstracts.base_address_usecase import (
    BaseAddressUseCase,
)
from app.application.domain.address.schemas.calculate_freight import (
    CalculateFreightSchema,
)

from app.application.domain.address.schemas.calculate_freight_options import (
    CalculateFreightOptionsSchema,
)
from app.application.domain.address.usecase.calculate_freight import (
    CalculateFreightUseCase,
)
from app.application.enums.address.delivery_type import DeliveryTypeEnum
from app.infra.settings import get_settings

setting = get_settings()


class CalculateFreightOptionsUseCase(BaseAddressUseCase):
    _payload: CalculateFreightOptionsSchema

    def __init__(self, payload):
        super().__init__(payload)

    async def execute(self):
        return [
            await CalculateFreightUseCase(
                CalculateFreightSchema(
                    cep=self._payload.cep,
                    quantity=self._payload.quantity,
                    product_type=self._payload.product_type,
                    delivery_type=delivery_type.value,
                )
            ).execute()
            for delivery_type in DeliveryTypeEnum
        ]

from datetime import datetime, timedelta

import pytz
from fastapi import status, HTTPException
from pycorreios import Correios

from app.application.domain.address.abstracts.base_address_usecase import (
    BaseAddressUseCase,
)
from app.application.domain.address.schemas.calculate_freight import (
    CalculateFreightSchema,
)
from app.application.domain.address.schemas.calculated_freight_correios import (
    CalculatedFreightCorreiosSchema,
)
from app.application.enums.product.type import ProductTypeEnum
from app.application.enums.product.weight import ProductWeightEnum
from app.application.helpers.utils import (
    get_correios_delivery_code,
    calculate_from_correios,
)
from app.infra.settings import get_settings

setting = get_settings()


class CalculateFreightUseCase(BaseAddressUseCase):
    _payload: CalculateFreightSchema

    def __init__(self, payload):
        super().__init__(payload)

    async def _calculate_wight(self):
        product_wight = ProductWeightEnum.DEFAULT
        if self._payload.product_type == ProductTypeEnum.T_SHIRT:
            product_wight = ProductWeightEnum.T_SHIRT
        elif self._payload.product_type == ProductTypeEnum.SWEATSHIRT:
            product_wight = ProductWeightEnum.SWEATSHIRT
        return (product_wight * self._payload.quantity) / 1000

    async def _calculate_freight(self):
        correios_code = await get_correios_delivery_code(self._payload.delivery_type)
        result = await calculate_from_correios(
            correios_code,
            setting.SHIPPING_POSTAL_CODE,
            self._payload.cep,
            await self._calculate_wight(),
        )
        value = float(result.get("Valor").replace(",", "."))
        deadline = int(result.get("PrazoEntrega"))
        datetime_now = pytz.UTC.localize(datetime.now())
        estimated_delivery_date = datetime_now + timedelta(days=deadline)
        return value, deadline, estimated_delivery_date

    async def execute(self):
        value, deadline, estimated_delivery_date = await self._calculate_freight()
        return CalculatedFreightCorreiosSchema(
            value=value,
            deadline=deadline,
            estimated_delivery_date=estimated_delivery_date,
            delivery_type=self._payload.delivery_type,
        )

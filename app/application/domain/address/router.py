from fastapi import APIRouter, status
from fastapi_pagination import paginate, Page

from app.application.domain.address.schemas.calculate_freight import (
    CalculateFreightSchema,
)
from app.application.domain.address.schemas.calculate_freight_options import (
    CalculateFreightOptionsSchema,
)
from app.application.domain.address.schemas.calculated_freight_correios import (
    CalculatedFreightCorreiosSchema,
)
from app.application.domain.address.usecase.calculate_freight import (
    CalculateFreightUseCase,
)
from app.application.domain.address.usecase.calculate_freight_options import (
    CalculateFreightOptionsUseCase,
)
from app.infra.settings import get_settings

router = APIRouter()
setting = get_settings()


@router.post(
    "/calculate-freight",
    status_code=status.HTTP_200_OK,
    description="This router is to calculate price of the freight.",
    response_model=CalculatedFreightCorreiosSchema,
)
async def calculate_freight(payload: CalculateFreightSchema):
    return await CalculateFreightUseCase(payload).execute()


@router.post(
    "/calculate-freight-options",
    status_code=status.HTTP_200_OK,
    description="This router is to calculate price of the all freight options.",
    response_model=Page[CalculatedFreightCorreiosSchema],
)
async def calculate_freight_options(payload: CalculateFreightOptionsSchema):
    freight_options = await CalculateFreightOptionsUseCase(payload).execute()
    return paginate(freight_options)

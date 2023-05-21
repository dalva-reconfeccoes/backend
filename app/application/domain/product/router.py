from typing import List

from fastapi import APIRouter, Depends, File, UploadFile, status
from fastapi_pagination import Page, paginate

from app.application.domain.product.schemas.filter_available_products import (
    FilterAvailableProductSchema,
)
from app.application.domain.product.schemas.filter_product import FilterProductSchema
from app.application.domain.product.schemas.get_available_filter_product import (
    GetAvailableFilterProductSchema,
)
from app.application.domain.product.schemas.get_product import GetProductSchema
from app.application.domain.product.schemas.post_product import PostProductSchema
from app.application.domain.product.usecase.create_product import CreateProductUseCase
from app.application.domain.product.usecase.create_product_image import (
    RegisterProductImageUseCase,
)
from app.application.domain.product.usecase.filter_products import (
    FilterAvailableProductUseCase,
)
from app.application.domain.product.usecase.get_all_products import GetAllProductUseCase
from app.application.domain.product.usecase.get_available_filter_products import (
    GetAvailableFilterProductsUseCase,
)
from app.application.domain.product.usecase.get_product import GetProductUseCase
from app.application.domain.product.usecase.register_available_quantity import (
    RegisterAvailableQuantity,
)
from app.application.domain.quantity.schemas.register_quantity import (
    RegisterQuantitySchema,
)
from app.infra.jwt.jwt_bearer import JWTBearer
from app.infra.settings import get_settings

router = APIRouter()
setting = get_settings()


@router.post(
    "/",
    description="Router to register a new product",
    response_model=GetProductSchema,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(JWTBearer())],
)
async def register_product(payload: PostProductSchema):
    return await CreateProductUseCase(payload).execute()


@router.get(
    "/",
    description="Router to get all registered products",
    response_model=Page[GetProductSchema],
    status_code=status.HTTP_200_OK,
)
async def get_products():
    products = await GetAllProductUseCase().execute()
    return paginate(products)


@router.get(
    "/{uuid}",
    description="Router to one product by uuid",
    response_model=GetProductSchema,
    status_code=status.HTTP_200_OK,
)
async def get_client(uuid: str):
    payload = FilterProductSchema(uuid=uuid)
    return await GetProductUseCase(payload).execute()


@router.post(
    "/image",
    description="Router to register a new product image",
    response_model=GetProductSchema,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(JWTBearer())],
)
async def register_product_image(
    product_uuid: str,
    files: List[UploadFile] = File(),
):
    return await RegisterProductImageUseCase(product_uuid, files).execute()


@router.post(
    "/quantity",
    description="Router to register available quantity of a product",
    response_model=Page[GetProductSchema],
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(JWTBearer())],
)
async def available_quantity_product(payload: List[RegisterQuantitySchema]):
    products = await RegisterAvailableQuantity(payload).execute()
    return paginate(products)


@router.get(
    "/available/filter",
    description="Router to get available filter of a products",
    response_model=GetAvailableFilterProductSchema,
    status_code=status.HTTP_200_OK,
)
async def available_filter_products():
    return await GetAvailableFilterProductsUseCase().execute()


@router.post(
    "/filter",
    description="Router to filter products",
    response_model=Page[GetProductSchema],
    status_code=status.HTTP_200_OK,
)
async def filter_products(payload: FilterAvailableProductSchema):
    products = await FilterAvailableProductUseCase(payload).execute()
    return paginate(products)

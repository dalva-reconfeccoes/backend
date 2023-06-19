from fastapi import APIRouter, status

from app.application.domain.cart.schemas.filter_cart import FilterCartSchema
from app.application.domain.cart.schemas.get_cart import GetCartSchema
from app.application.domain.cart.schemas.post_cart import PostCartSchema
from app.application.domain.cart.usecase.add_product_cart import AddProductCartUseCase
from app.application.domain.cart.usecase.create_cart import CreateCartUseCase
from app.application.domain.cart.usecase.get_cart import GetCartUseCase
from app.application.domain.cart.usecase.remove_product_cart import (
    RemoveProductCartUseCase,
)
from app.infra.settings import get_settings

router = APIRouter()
setting = get_settings()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    description="This router is to register a new cart.",
    response_model=GetCartSchema,
)
async def create_cart(payload: PostCartSchema):
    return await CreateCartUseCase(payload).execute()


@router.get(
    "/{uuid}",
    description="Router to one cart by uuid",
    response_model=GetCartSchema,
    status_code=status.HTTP_200_OK,
)
async def get_cart(uuid: str):
    payload = FilterCartSchema(uuid=uuid)
    return await GetCartUseCase(payload).execute()


@router.post(
    "/{uuid_cart}/add-product/",
    status_code=status.HTTP_200_OK,
    description="This router is to add a product in an existing cart.",
    response_model=GetCartSchema,
)
async def add_product_cart(uuid_cart: str, payload: PostCartSchema):
    return await AddProductCartUseCase(uuid_cart, payload).execute()


@router.delete(
    "/{uuid_cart}/remove-product/{selected_product_uuid}",
    status_code=status.HTTP_200_OK,
    description="This router is to remove a product in an existing cart.",
    response_model=GetCartSchema,
)
async def remove_product_cart(uuid_cart: str, selected_product_uuid: str):
    return await RemoveProductCartUseCase(uuid_cart, selected_product_uuid).execute()

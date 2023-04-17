from fastapi import APIRouter, status, Depends
from fastapi_pagination import Page, paginate

from app.application.domain.product.schemas.filter_product import FilterProductSchema
from app.application.domain.product.schemas.get_product import GetProductSchema
from app.application.domain.product.schemas.post_product import PostProductSchema
from app.application.domain.product.usecase.create_product import CreateProductUseCase
from app.application.domain.product.usecase.get_all_products import GetAllProductUseCase
from app.application.domain.product.usecase.get_product import GetProductUseCase
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
    dependencies=[Depends(JWTBearer())],
)
async def get_products():
    products = await GetAllProductUseCase().execute()
    return paginate(products)


@router.get(
    "/{uuid}",
    description="Router to one product by uuid",
    response_model=GetProductSchema,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
)
async def get_client(uuid: str):
    payload = FilterProductSchema(uuid=uuid)
    return await GetProductUseCase(payload).execute()

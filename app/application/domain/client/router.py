from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page, paginate

from app.application.domain.client import usecase
from app.application.domain.client.schemas import (
    GetClientSchema,
    JWTClientSchema,
    LoginClientSchema,
    PostClientSchema,
    UpdateClientSchema,
)
from app.infra.jwt.jwt_bearer import JWTBearer
from app.infra.settings import get_settings

router = APIRouter()
setting = get_settings()


@router.get(
    "/",
    description="Router to list all clients registered",
    response_model=Page[GetClientSchema],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
)
async def get_clients():
    clients = await usecase.GetClientsUseCase().execute()
    return paginate(clients)


@router.get(
    "/{id}",
    description="Router to one client by id",
    response_model=GetClientSchema,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
)
async def get_client(id: int):
    return await usecase.GetClientUseCase(id).execute()


@router.post(
    "/",
    description="This router is to create new client",
    status_code=status.HTTP_201_CREATED,
    response_model=GetClientSchema,
)
async def post_client(payload: PostClientSchema):
    return await usecase.CreateClientUseCase(payload).execute()


@router.get(
    "/email/{email}",
    description="This router is to get one client by email",
    status_code=status.HTTP_200_OK,
    response_model=GetClientSchema,
    dependencies=[Depends(JWTBearer())],
)
async def get_client_by_email(email: str):
    return await usecase.GetClientByEmailUseCase(email).execute()


@router.put(
    "/{id}",
    description="This router is to update client",
    status_code=status.HTTP_200_OK,
    response_model=GetClientSchema,
    dependencies=[Depends(JWTBearer()), Depends(JWTBearer())],
)
async def put_client(id: int, payload: UpdateClientSchema):
    return await usecase.UpdateClientUseCase(payload, id).execute()


@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    response_model=JWTClientSchema,
    description="This router is to login client",
)
async def login(payload: LoginClientSchema, Authorize: AuthJWT = Depends()):
    return await usecase.LoginUseCase(payload, Authorize).execute()


@router.post(
    "/create-admin",
    status_code=status.HTTP_201_CREATED,
    description="This router is to create admin client",
)
async def create_admim():
    await usecase.CreateClientAdminUseCase().execute()
    return {"message": "Admin client created"}

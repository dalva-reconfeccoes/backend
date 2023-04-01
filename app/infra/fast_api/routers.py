from fastapi import FastAPI
from fastapi_pagination import add_pagination


async def init_routers(app: FastAPI):
    """
    This function is to load all routers in application.
    Here you can add routers from your modules.
    :param app:
    :return:
    """
    from app.application.domain.client import router as client_router
    from app.application.routes import healthcheck_router

    app.include_router(healthcheck_router.router)
    app.include_router(client_router.router, prefix="/clients", tags=["Client"])

    add_pagination(app)

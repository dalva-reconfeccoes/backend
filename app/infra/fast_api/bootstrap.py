import warnings

from fastapi import FastAPI
from fastapi_pagination.utils import FastAPIPaginationWarning

from app.infra.middlewares.middlewares import init_middlewares
from app.infra.settings import get_settings

settings = get_settings()
warnings.simplefilter("ignore", FastAPIPaginationWarning)


def create_app() -> FastAPI:
    """This function is to initialize the application and all configurations."""
    application = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description=settings.APP_DESCRIPTION,
        root_path=settings.ROOT_PATH,
    )
    init_middlewares(application)
    return application

from fastapi import FastAPI

from app.infra.settings import get_settings

settings = get_settings()


def create_app() -> FastAPI:
    """This function is to initialize the application and all configurations."""
    application = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description=settings.APP_DESCRIPTION,
        root_path=settings.ROOT_PATH,
    )

    return application

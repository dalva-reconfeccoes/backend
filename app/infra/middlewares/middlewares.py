from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.infra.settings import get_settings

settings = get_settings()


def init_middlewares(app: FastAPI):
    """
    This module initializes the middlewares from application
    :param app
    """

    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=settings.ORIGINS,
        allow_methods=settings.ALLOW_METHODS,
        allow_headers=settings.ALLOW_HEADERS,
    )

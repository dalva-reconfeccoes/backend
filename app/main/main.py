from loguru import logger

from app.infra.database.db import (close_connection_database,
                                   connect_to_database)
from app.infra.fast_api.bootstrap import create_app
from app.infra.fast_api.routers import init_routers
from app.infra.jwt.jwt import exception_jwt, init_jwt
from app.infra.middlewares.middlewares import init_middlewares

app = create_app()


@app.on_event("startup")
async def startup_db():
    logger.info("Starting up database...")
    await connect_to_database()


@app.on_event("startup")
async def startup_routers():
    logger.info("Starting up routers...")
    await init_routers(app)


@app.on_event("startup")
async def startup_middlewares():
    logger.info("Starting up middlewares...")
    await init_middlewares(app)


@app.on_event("startup")
async def startup_jwt():
    logger.info("Starting up JWT...")
    await init_jwt()


@app.on_event("startup")
async def startup_exception_jwt():
    logger.info("Starting up exceptions JWT...")
    await exception_jwt(app)


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")
    await close_connection_database()

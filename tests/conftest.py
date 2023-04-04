import asyncio

import pytest
from starlette.testclient import TestClient
from tortoise.contrib.starlette import register_tortoise

from app.infra.database.db import connect_to_database
from app.infra.fast_api import create_app, init_routers
from app.infra.jwt import init_jwt
from app.infra.middlewares.middlewares import init_middlewares
from app.infra.settings import Setting, get_settings

setting = get_settings()


def get_settings_override():
    return Setting(TESTING=True, DB_URL=setting.DB_TEST_URL)


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.dependency_overrides[get_settings] = get_settings_override()
    init_middlewares(app)
    asyncio.run(init_routers(app))
    asyncio.run(init_jwt())
    asyncio.run(connect_to_database())

    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="module")
def test_app_with_db():
    app = create_app()
    app.dependency_overrides[get_settings] = get_settings_override
    register_tortoise(
        app,
        db_url=setting.DB_TEST_URL,
        modules={"models": setting.MODELS},
        generate_schemas=True,
    )
    init_middlewares(app)
    asyncio.run(init_routers(app))
    asyncio.run(init_jwt())
    asyncio.run(connect_to_database())
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="module")
def access_token(test_app_with_db):
    test_app_with_db.post("/api/clients/create-admin")
    response = test_app_with_db.post(
        "/api/clients/login",
        json={"email": setting.EMAIL_ADMIN, "password": setting.PASSWORD_ADMIN},
    )

    payload = response.json()

    return {"Authorization": f"Bearer {payload.get('accessToken')}"}

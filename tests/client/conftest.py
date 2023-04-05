from uuid import uuid4
from fastapi import status
import pytest
from faker import Factory

faker = Factory.create("pt_BR")


@pytest.fixture(scope="session")
def client_fake_dict():
    return {
        "id": faker.random_int(min=1, max=9999),
        "uuid": uuid4().hex,
        "full_name": faker.name(),
        "email": faker.email(),
        "password": faker.password(),
        "is_juridical": False,
        "email_is_verified": False,
    }


@pytest.fixture(scope="session")
def client_post_fake_dict():
    return {
        "full_name": faker.name(),
        "email": faker.email(),
        "password": faker.password(),
        "is_juridical": True,
    }


@pytest.fixture(scope="session")
def client_put_fake_dict():
    return {
        "full_name": faker.name(),
        "email": faker.email(),
        "password": faker.password(),
        "is_active": False,
        "is_juridical": True,
    }


@pytest.fixture(scope="session")
def client_login_fake_dict():
    return {
        "email": faker.email(),
        "password": faker.password(),
    }


@pytest.fixture(scope="module")
def client_created(test_app_with_db, client_post_fake_dict, access_token):
    response = test_app_with_db.post(
        "/api/clients/", json=client_post_fake_dict, headers=access_token
    )
    assert response.status_code == status.HTTP_201_CREATED
    return response.json()

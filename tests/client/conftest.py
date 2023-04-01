from uuid import uuid4

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
    }


@pytest.fixture(scope="session")
def client_post_fake_dict():
    return {
        "full_name": faker.name(),
        "email": faker.email(),
        "password": faker.password(),
        "is_active": True,
    }


@pytest.fixture(scope="session")
def client_put_fake_dict():
    return {
        "full_name": faker.name(),
        "email": faker.email(),
        "password": faker.password(),
        "is_active": False,
    }


@pytest.fixture(scope="session")
def client_login_fake_dict():
    return {
        "email": faker.email(),
        "password": faker.password(),
    }

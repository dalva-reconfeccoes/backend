from uuid import uuid4

import pytest
from faker import Factory

faker = Factory.create("pt_BR")


@pytest.fixture(scope="session")
def image_fake_dict():
    return {
        "id": faker.random_int(min=1, max=9999),
        "uuid": uuid4().hex,
        "filename": faker.name(),
        "content_type": faker.email(),
        "bucket": faker.name(),
        "is_active": True,
    }

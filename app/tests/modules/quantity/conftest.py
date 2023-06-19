from uuid import uuid4

import pytest
from faker import Factory

from app.application.enums.product.size import ProductSizeEnum

faker = Factory.create("pt_BR")


@pytest.fixture(scope="session")
def quantity_fake_dict():
    return {
        "id": faker.random_int(min=1, max=9999),
        "uuid": uuid4().hex,
        "size": ProductSizeEnum.SIZE_G,
        "available": faker.random_int(min=1, max=9999),
        "purchased": faker.random_int(min=1, max=9999),
        "product_id": faker.random_int(min=1, max=9999),
    }

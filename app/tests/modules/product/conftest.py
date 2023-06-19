import pytest
from faker import Factory

from app.application.enums.product.size import ProductSizeEnum

faker = Factory.create("pt_BR")


@pytest.fixture()
def new_quantity_fake_dict(product_created):
    return {
        "size": ProductSizeEnum.SIZE_G,
        "available": faker.random_int(min=1, max=9999),
        "product_id": product_created.get("id"),
    }

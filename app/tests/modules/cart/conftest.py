from uuid import uuid4
from fastapi import status
import pytest
from faker import Factory

from app.application.enums.product.size import ProductSizeEnum

faker = Factory.create("pt_BR")


@pytest.fixture()
def cart_fake_dict():
    return {
        "id": faker.random_int(min=1, max=9999),
        "uuid": uuid4().hex,
        "total_value": faker.pyfloat(min_value=30, max_value=100),
    }


@pytest.fixture()
def post_cart_fake_dict(product_created):
    return {
        "selectedProduct": {
            "size": ProductSizeEnum.SIZE_G,
            "quantity": faker.random_int(min=1, max=10),
            "product_id": product_created.get("id"),
        }
    }


@pytest.fixture()
def cart_created(test_app_with_db, post_cart_fake_dict):
    response = test_app_with_db.post(
        "/api/cart/",
        json=post_cart_fake_dict,
    )
    assert response.status_code == status.HTTP_201_CREATED
    return response.json()

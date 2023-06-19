from uuid import uuid4

import pytest
from faker import Factory
from fastapi import status

from app.application.enums.product.sex import ProductSexEnum
from app.application.enums.product.size import ProductSizeEnum
from app.application.enums.product.status import ProductStatusEnum
from app.application.enums.product.sub_type import ProductSubTypeEnum
from app.application.enums.product.type import ProductTypeEnum

faker = Factory.create("pt_BR")


@pytest.fixture(scope="session")
def product_fake_dict():
    return {
        "id": faker.random_int(min=1, max=9999),
        "uuid": uuid4().hex,
        "header": faker.name(),
        "color": faker.safe_color_name(),
        "knitted": faker.name(),
        "price": faker.pyfloat(min_value=30, max_value=100),
        "type": ProductTypeEnum.T_SHIRT,
        "sub_type": ProductSubTypeEnum.REGULAR,
        "sex": ProductSexEnum.MALE,
        "status": ProductStatusEnum.AVAILABLE,
        "is_active": True,
    }


@pytest.fixture(scope="module")
def product_created(test_app_with_db, access_token, product_fake_dict):
    response = test_app_with_db.post(
        "/api/products/", json=product_fake_dict, headers=access_token
    )
    assert response.status_code == status.HTTP_201_CREATED
    product = response.json()
    resp_quantity = test_app_with_db.post(
        "/api/products/quantity",
        json=[
            {
                "size": ProductSizeEnum.SIZE_G,
                "available": faker.random_int(min=100, max=9999),
                "product_id": product.get("id"),
            }
        ],
        headers=access_token,
    )
    assert resp_quantity.status_code == status.HTTP_201_CREATED
    return product

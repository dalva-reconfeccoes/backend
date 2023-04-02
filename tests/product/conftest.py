from uuid import uuid4

import pytest
from faker import Factory

from app.application.enums.product.product_sex import ProductSexEnum
from app.application.enums.product.product_status import ProductStatusEnum
from app.application.enums.product.product_sub_type import ProductSubTypeEnum
from app.application.enums.product.product_type import ProductTypeEnum

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
        "quantity": faker.random_int(min=10, max=999),
        "type": ProductTypeEnum.T_SHIRT,
        "sub_type": ProductSubTypeEnum.REGULAR,
        "sex": ProductSexEnum.MALE,
        "status": ProductStatusEnum.AVAILABLE,
        "is_active": True,
    }

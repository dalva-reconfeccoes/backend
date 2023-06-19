from datetime import datetime
from uuid import uuid4

import pytest
from faker import Factory

from app.application.enums.address.delivery_type import DeliveryTypeEnum
from app.application.enums.product.type import ProductTypeEnum

faker = Factory.create("pt_BR")


@pytest.fixture()
def address_fake_dict():
    return {
        "id": faker.random_int(min=1, max=9999),
        "uuid": uuid4().hex,
        "district": faker.street_name(),
        "cep": faker.postcode(),
        "city": faker.city(),
        "street": faker.street_address(),
        "uf": faker.state_abbr(),
        "complement": faker.neighborhood(),
        "neighborhood": faker.neighborhood(),
        "number": faker.random_int(min=1, max=100),
        "is_active": True,
    }


@pytest.fixture()
def address_calculate_freight_fake_dict():
    return {
        "cep": faker.postcode(),
        "quantity": faker.random_int(min=1, max=100),
        "productType": ProductTypeEnum.T_SHIRT,
        "deliveryType": DeliveryTypeEnum.CORREIOS_PAC,
    }


@pytest.fixture()
def address_calculated_freight_correios_fake_dict():
    return {
        "value": faker.pyfloat(min_value=20, max_value=90),
        "deadline": faker.random_int(min=1, max=10),
        "delivery_type": DeliveryTypeEnum.CORREIOS_PAC,
        "estimated_delivery_date": datetime.now(),
    }

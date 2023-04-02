from tortoise import Model

from app.application.enums.product.product_sex import ProductSexEnum
from app.application.enums.product.product_status import ProductStatusEnum
from app.application.enums.product.product_sub_type import ProductSubTypeEnum
from app.application.enums.product.product_type import ProductTypeEnum
from app.models.product import Product


def test_product_model_should_return_valid_instance_when_valid_data_is_passed(
    product_fake_dict,
):
    product = Product(**product_fake_dict)
    assert isinstance(product, Model)


def test_product_model_should_return_valid_fields_when_valid_data_is_passed(
    product_fake_dict,
):
    product = Product(**product_fake_dict)
    assert isinstance(product.header, str)
    assert isinstance(product.color, str)
    assert isinstance(product.knitted, str)
    assert isinstance(product.price, float)
    assert isinstance(product.quantity, int)
    assert isinstance(product.type, ProductTypeEnum)
    assert isinstance(product.sub_type, ProductSubTypeEnum)
    assert isinstance(product.sex, ProductSexEnum)
    assert isinstance(product.status, ProductStatusEnum)
    assert isinstance(product.is_active, bool)

from app.application.domain.product.schemas.filter_product import FilterProductSchema
from app.application.domain.product.schemas.get_product import GetProductSchema
from app.application.domain.product.schemas.post_product import PostProductSchema
from app.application.enums.product.sex import ProductSexEnum
from app.application.enums.product.status import ProductStatusEnum
from app.application.enums.product.sub_type import ProductSubTypeEnum
from app.application.enums.product.type import ProductTypeEnum


def test_get_product_schema_should_return_valid_instance_fields_when_valid_data_is_passed(
    product_fake_dict,
):
    product_schema = GetProductSchema(**product_fake_dict)

    assert isinstance(product_schema.id, int)
    assert isinstance(product_schema.header, str)
    assert isinstance(product_schema.color, str)
    assert isinstance(product_schema.knitted, str)
    assert isinstance(product_schema.price, float)
    assert isinstance(product_schema.type, ProductTypeEnum)
    assert isinstance(product_schema.sub_type, ProductSubTypeEnum)
    assert isinstance(product_schema.sex, ProductSexEnum)
    assert isinstance(product_schema.status, ProductStatusEnum)
    assert isinstance(product_schema.is_active, bool)


def test_post_product_schema_should_return_valid_instance_fields_when_valid_data_is_passed(
    product_fake_dict,
):
    product_schema = PostProductSchema(**product_fake_dict)

    assert isinstance(product_schema.header, str)
    assert isinstance(product_schema.color, str)
    assert isinstance(product_schema.knitted, str)
    assert isinstance(product_schema.price, float)
    assert isinstance(product_schema.type, ProductTypeEnum)
    assert isinstance(product_schema.sub_type, ProductSubTypeEnum)
    assert isinstance(product_schema.sex, ProductSexEnum)
    assert isinstance(product_schema.status, ProductStatusEnum)


def test_filter_product_schema_should_return_valid_instance_fields_when_valid_data_is_passed(
    product_fake_dict,
):
    product_schema = FilterProductSchema(**product_fake_dict)

    assert isinstance(product_schema.id, int)
    assert isinstance(product_schema.uuid, str)
    assert isinstance(product_schema.header, str)

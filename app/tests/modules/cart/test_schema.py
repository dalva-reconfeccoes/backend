from fastapi_camelcase import CamelModel
from pydantic import BaseModel

from app.application.domain.cart.schemas.filter_cart import FilterCartSchema
from app.application.domain.cart.schemas.get_cart import GetCartSchema
from app.application.domain.cart.schemas.post_cart import PostCartSchema


def test_post_cart_schema_should_return_valid_instance_when_valid_data_is_passed(
    post_cart_fake_dict,
):
    schema = PostCartSchema(**post_cart_fake_dict)
    assert isinstance(schema, PostCartSchema)
    assert isinstance(schema, CamelModel)
    assert isinstance(schema, BaseModel)


def test_get_cart_schema_should_return_valid_instance_when_valid_data_is_passed(
    cart_fake_dict,
):
    schema = GetCartSchema(**cart_fake_dict)
    assert isinstance(schema, GetCartSchema)
    assert isinstance(schema, CamelModel)
    assert isinstance(schema, BaseModel)


def test_filter_cart_schema_should_return_valid_instance_when_valid_data_is_passed(
    cart_fake_dict,
):
    schema = FilterCartSchema(**cart_fake_dict)
    assert isinstance(schema, FilterCartSchema)
    assert isinstance(schema, CamelModel)
    assert isinstance(schema, BaseModel)


def test_filter_cart_schema_should_return_valid_instance_when_no_data_is_passed():
    schema = FilterCartSchema()
    assert isinstance(schema, FilterCartSchema)
    assert isinstance(schema, CamelModel)
    assert isinstance(schema, BaseModel)

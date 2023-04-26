from fastapi_camelcase import CamelModel
from pydantic import BaseModel

from app.application.domain.image.schemas.get_image import GetImageSchema
from app.application.domain.quantity.schemas.get_quantity import GetQuantitySchema
from app.application.domain.quantity.schemas.register_quantity import (
    RegisterQuantitySchema,
)
from app.application.enums.product.size import ProductSizeEnum


def test_get_quantity_schema_should_return_valid_instance_when_valid_data_is_passed(
    quantity_fake_dict,
):
    image_schema = GetQuantitySchema(**quantity_fake_dict)

    assert isinstance(image_schema, GetQuantitySchema)
    assert isinstance(image_schema, CamelModel)
    assert isinstance(image_schema, BaseModel)
    assert isinstance(image_schema.id, int)
    assert isinstance(image_schema.size, ProductSizeEnum)
    assert isinstance(image_schema.available, int)
    assert isinstance(image_schema.purchased, int)


def test_register_quantity_schema_should_return_valid_instance_fields_when_valid_data_is_passed(
    quantity_fake_dict,
):
    image_schema = RegisterQuantitySchema(**quantity_fake_dict)

    assert isinstance(image_schema, RegisterQuantitySchema)
    assert isinstance(image_schema, CamelModel)
    assert isinstance(image_schema, BaseModel)

    assert isinstance(image_schema.size, ProductSizeEnum)
    assert isinstance(image_schema.available, int)
    assert isinstance(image_schema.product_id, int)

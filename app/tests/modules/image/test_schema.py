from fastapi_camelcase import CamelModel
from pydantic import BaseModel

from app.application.domain.image.schemas.get_image import GetImageSchema


def test_image_schema_should_return_valid_instance_when_valid_data_is_passed(
    image_fake_dict,
):
    image_schema = GetImageSchema(**image_fake_dict)

    assert isinstance(image_schema, GetImageSchema)
    assert isinstance(image_schema, CamelModel)
    assert isinstance(image_schema, BaseModel)


def test_image_schema_should_return_valid_instance_fields_when_valid_data_is_passed(
    image_fake_dict,
):
    image_schema = GetImageSchema(**image_fake_dict)

    assert isinstance(image_schema.uuid, str)
    assert isinstance(image_schema.filename, str)
    assert isinstance(image_schema.content_type, str)
    assert isinstance(image_schema.bucket, str)
    assert isinstance(image_schema.is_active, bool)
